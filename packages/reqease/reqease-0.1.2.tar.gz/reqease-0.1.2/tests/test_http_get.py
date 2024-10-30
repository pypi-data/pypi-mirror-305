import unittest
from reqease.http_get import get

class TestHttpGet(unittest.TestCase):
    def test_get_success(self):
        url = "https://www.swimplify.co"
        response = get(url)
        self.assertTrue(response.status_code,f"The value for status_code should not be empty")
        self.assertTrue(response.headers,f"The value for headers should not be empty")
        self.assertTrue(response.body_bytes,f"The value for body_bytes should not be empty")
        self.assertTrue(response.body_str,f"The value for body_str should not be empty")

if __name__ == "__main__":
    unittest.main()