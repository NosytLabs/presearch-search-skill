import test from 'node:test';
import assert from 'node:assert/strict';
import { EventEmitter } from 'node:events';
import https from 'node:https';
import { PresearchSkill } from '../presearch_nodejs.js';

function fakeRequest(t, status, body, timeout = false) {
  const original = https.request;
  let calls = 0;
  https.request = (_url, options, callback) => {
    calls++;
    assert.equal(options.headers.Authorization, 'Bearer fixture-key');
    const request = new EventEmitter();
    request.setTimeout = (ms, fn) => {
      assert.equal(ms, 15000);
      request.onTimeout = fn;
    };
    request.destroy = error => request.emit('error', error);
    request.end = () => queueMicrotask(() => {
      if (timeout) return request.onTimeout();
      const response = new EventEmitter();
      response.statusCode = status;
      callback(response);
      response.emit('data', body);
      response.emit('end');
    });
    return request;
  };
  t.after(() => { https.request = original; });
  return () => calls;
}

test('normalizes a successful response', async t => {
  const calls = fakeRequest(t, 200, JSON.stringify({ data: {
    standardResults: [{ title: 'Result', link: 'https://example.org', description: 'Example' }],
    pagination: { current_page: 2, has_next: true },
  } }));
  const client = new PresearchSkill('fixture-key');
  const result = await client.search({ query: 'example', page: 2 });
  assert.equal(result.results[0].title, 'Result');
  assert.equal(result.current_page, 2);
  assert.equal(result.has_next, true);
  assert.equal(calls(), 1);
});

test('reports rate limiting without retrying forever', async t => {
  const calls = fakeRequest(t, 429, 'rate limited');
  const client = new PresearchSkill('fixture-key');
  await assert.rejects(client.search({ query: 'example' }), /429/);
  assert.equal(calls(), 1);
});

test('reports a request timeout', async t => {
  fakeRequest(t, 0, '', true);
  const client = new PresearchSkill('fixture-key');
  await assert.rejects(client.search({ query: 'example' }), /timed out/);
});
