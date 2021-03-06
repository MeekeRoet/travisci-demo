import unittest,json

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code, 401, 'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data)
        self.assertEqual(resp['answer'], 35, 'Multiply endpoint failed known answer 7*5 = 35')

    def test_touppercase(self):
        expected_output_string = 'HELLOWORLD'
        response = self.app.get('/touppercase?s=helloworld')

        self.assertEqual(response.data.decode('utf-8'),
                         expected_output_string,
                         'Touppercase endpoint failed known answer helloworld > HELLOWORLD')


    # TODO DEFINE TWO MORE TESTS ON THE END POINTS


if __name__ == '__main__':
    unittest.main()
