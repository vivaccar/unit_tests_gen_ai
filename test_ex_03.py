import unittest
import threading
import requests

class TestSecurityVulnerabilities(unittest.TestCase):

    def setUp(self):
        self.server_thread = threading.Thread(target=app.run)
        self.server_thread.start()

    def tearDown(self):
        requests.post('http://127.0.0.1:5000/shutdown')
        self.server_thread.join()

    def test_path_traversal_vulnerability(self):
        response = requests.get('http://127.0.0.1:5000/files/../app.py')
        self.assertNotIn('flask', response.text)  # Verifica se a resposta não contém parte do código-fonte
    
    def test_insecure_file_upload(self):
        files = {'file': open('test_files/test.txt', 'rb')}
        response = requests.post('http://127.0.0.1:5000/upload', files=files)
        self.assertEqual(response.text, "File uploaded successfully!")
        
        # Verifica se o arquivo enviado é acessível
        response_file = requests.get('http://127.0.0.1:5000/uploaded_files/test.txt')
        self.assertIn('Test data', response_file.text)  # Conteúdo do arquivo test.txt
        
    def test_protected_file_access(self):
        response = requests.get('http://127.0.0.1:5000/files/protected_file.txt')
        self.assertNotIn('Sensitive Data', response.text)  # Verifica se a resposta não contém dados confidenciais

if __name__ == '__main__':
    unittest.main()
