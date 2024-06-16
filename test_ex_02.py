import unittest
from flask import Flask
import threading
import requests

class TestXSS(unittest.TestCase):

    def setUp(self):
        self.server_thread = threading.Thread(target=app.run)
        self.server_thread.start()

    def tearDown(self):
        requests.post('http://127.0.0.1:5000/shutdown')
        self.server_thread.join()

    def test_xss_reflected(self):
        malicious_input = '<script>alert("XSS Attack!")</script>'
        response = requests.post('http://127.0.0.1:5000/store', data={'input': malicious_input})
        
        response = requests.get('http://127.0.0.1:5000/get-stored-input')
        self.assertNotIn(malicious_input, response.text)
        self.assertNotIn('<script>', response.text)
        self.assertNotIn('alert("XSS Attack!")', response.text)

class TestApp(unittest.TestCase):

    def setUp(self):
        self.server_thread = threading.Thread(target=app.run)
        self.server_thread.start()

    def tearDown(self):
        requests.post('http://127.0.0.1:5000/shutdown')
        self.server_thread.join()

    def test_store_route(self):
        response = requests.post('http://127.0.0.1:5000/store', data={'input': 'test'})
        self.assertEqual(response.text, "Input stored successfully!")

    def test_get_stored_input_route(self):
        response = requests.get('http://127.0.0.1:5000/get-stored-input')
        self.assertIn(b'<div>test</div>', response.content)

if __name__ == '__main__':
    unittest.main()
