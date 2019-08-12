from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        tester.environ_base['HTTP_X_FORWARDED_PROTO'] = 'HTTPS'
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')
    def test_create_qr(self):
        tester = app.test_client(self)
        tester.environ_base['HTTP_X_FORWARDED_PROTO'] = 'HTTPS'
        response = tester.get('/SampleImg')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'PNG',response.data)
    def test_index_https_check(self):
        tester = app.test_client(self)
        tester.environ_base['HTTP_X_FORWARDED_PROTO'] = 'HTTP'
        self.assertEqual(tester.get('/').status_code, 404)
        
if __name__ == '__main__':
    unittest.main()