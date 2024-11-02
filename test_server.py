import requests
import unittest

class FlaskAppTestCase(unittest.TestCase):
    def test_hello(self):
        response = requests.get('http://localhost:8080/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, World!")

if __name__ == '__main__':
    unittest.main()