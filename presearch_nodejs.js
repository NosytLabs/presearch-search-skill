import https from 'https';
import { fileURLToPath } from 'url';
import process from 'process';

/**
 * PresearchSkill - Production-ready Node.js client
 */
export class PresearchSkill {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://na-us-1.presearch.com/v1/search';
    this.lastRequestTime = 0;
    this.rateLimitDelay = 1100; // >1s for Free Tier safety
  }

  async _rateLimit() {
    const now = Date.now();
    const timeSinceLast = now - this.lastRequestTime;
    if (timeSinceLast < this.rateLimitDelay) {
      await new Promise(resolve => setTimeout(resolve, this.rateLimitDelay - timeSinceLast));
    }
    this.lastRequestTime = Date.now();
  }

  /**
   * Search Presearch
   * @param {Object} options
   * @param {string} options.query - Search query
   * @param {string} [options.ip] - User IP (default: 127.0.0.1)
   * @param {string} [options.lang] - Language code (default: en-US)
   * @param {string} [options.time] - Time filter (default: any)
   * @param {number} [options.page] - Page number (default: 1)
   * @param {string} [options.safe] - Safe search (default: 1)
   * @param {string} [options.location] - Location JSON string (e.g. '{"lat":1,"long":1}')
   */
  async search({ query, ip = '127.0.0.1', lang = 'en-US', time = 'any', page = 1, safe = '1', location = null }) {
    await this._rateLimit();

    const params = new URLSearchParams({
      q: query,
      ip: ip,
      lang: lang,
      time: time,
      page: page.toString(),
      safe: safe
    });
    
    if (location) {
      params.append('location', location);
    }

    const url = `${this.baseUrl}?${params.toString()}`;

    return new Promise((resolve, reject) => {
      const req = https.request(url, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      }, (res) => {
        let data = '';

        res.on('data', (chunk) => {
          data += chunk;
        });

        res.on('end', async () => {
          if (res.statusCode === 429) {
            // Rate limit hit, backoff and retry
            await new Promise(r => setTimeout(r, 2000));
            try {
              resolve(await this.search({ query, ip, lang, time, page, safe, location }));
            } catch (e) {
              reject(e);
            }
            return;
          }

          if (res.statusCode !== 200) {
            reject(new Error(`Presearch API Error: ${res.statusCode} - ${data}`));
            return;
          }

          try {
            const json = JSON.parse(data);
            const respData = json.data || {};
            const standardResults = respData.standardResults || [];
            const pagination = respData.pagination || { current_page: 1, has_next: false };
            const infoSection = respData.infoSection;
            const specialSections = respData.specialSections;

            resolve({
              results: standardResults.map(r => ({
                title: r.title || '',
                link: r.link || '',
                description: r.description || ''
              })),
              infoSection,
              specialSections,
              current_page: pagination.current_page || 1,
              has_next: pagination.has_next || false
            });
          } catch (e) {
            reject(new Error(`Failed to parse response: ${e.message}`));
          }
        });
      });

      req.on('error', (e) => {
        reject(new Error(`Network error: ${e.message}`));
      });

      req.end();
    });
  }
}

// CLI Support
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const query = process.argv[2];
  if (!query) {
    console.error('Usage: node presearch_nodejs.js <query>');
    process.exit(1);
  }
  
  const apiKey = process.env.PRESEARCH_API_KEY;
  if (!apiKey) {
    console.error('Error: PRESEARCH_API_KEY environment variable not set.');
    process.exit(1);
  }

  const skill = new PresearchSkill(apiKey);
  skill.search({ query })
    .then(results => console.log(JSON.stringify(results, null, 2)))
    .catch(err => {
      console.error('Error:', err.message);
      process.exit(1);
    });
}