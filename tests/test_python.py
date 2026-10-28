import unittest
from unittest.mock import Mock, patch

import requests

from presearch_python import PresearchSkill


class ClientTests(unittest.TestCase):
    @patch("presearch_python.requests.get")
    def test_success_and_timeout_configuration(self, get):
        response = Mock(status_code=200)
        response.json.return_value = {"data": {
            "standardResults": [{"title": "Result", "link": "https://example.org"}],
            "pagination": {"current_page": 2, "has_next": True},
        }}
        get.return_value = response
        result = PresearchSkill("fixture-key").search("example", page=2)
        self.assertEqual(result.results[0].title, "Result")
        self.assertEqual(result.current_page, 2)
        self.assertTrue(result.has_next)
        self.assertEqual(get.call_args.kwargs["timeout"], (5, 15))
        self.assertFalse(get.call_args.kwargs["allow_redirects"])

    @patch("presearch_python.requests.get")
    def test_rate_limit_is_not_retried(self, get):
        response = Mock(status_code=429)
        response.raise_for_status.side_effect = requests.exceptions.HTTPError("429")
        get.return_value = response
        with self.assertRaisesRegex(Exception, "429"):
            PresearchSkill("fixture-key").search("example")
        self.assertEqual(get.call_count, 1)

    @patch("presearch_python.requests.get")
    def test_redirect_is_rejected(self, get):
        get.return_value = Mock(status_code=302)
        with self.assertRaisesRegex(Exception, "Unexpected redirect"):
            PresearchSkill("fixture-key").search("example")
        self.assertEqual(get.call_count, 1)

    @patch("presearch_python.requests.get")
    def test_timeout_is_reported(self, get):
        get.side_effect = requests.exceptions.Timeout("timed out")
        with self.assertRaisesRegex(Exception, "timed out"):
            PresearchSkill("fixture-key").search("example")


if __name__ == "__main__":
    unittest.main()
