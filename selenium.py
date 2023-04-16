import requests
import unittest
from http.server import HTTPServer, BaseHTTPRequestHandler

class TestWebsite(unittest.TestCase):
    
    def test_website_loads(self):
        url = "https://atg.world/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, msg="Website failed to load")
        print("Website loaded successfully")
        
if __name__ == '__main__':
    unittest.main()


