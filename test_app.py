from unittest import TestCase
from app import app


class FlaskTests(TestCase):

    def setUp(self):
        """ Do before every test """

        # Make Flask errors be real errors, not HTML pages with error info
        app.config['TESTING'] = True
        # Starts server
        self.client = app.test_client()

    def test_home_page(self):
        """Tests home page"""

        with self.client:
            # client makes request to server
            response = self.client.get("/")
            # Get HTML
            html = response.get_data(as_text=True)

            # Test response code
            self.assertEqual(response.status_code, 200)

            # Test HTML
            self.assertIn('<h1>Forex Converter</h1>', html)
            self.assertIn('<label for="cur1">Convert From:</label>', html)
            self.assertIn('<label for="cur2">Convert To:</label>', html)
            self.assertIn('<label for="amount">Amount</label>', html)

    def test_convert_valid(self):
        """Tests converter with valid data"""

        with self.client:
            """1 USD should convert to 1 USD"""
            response = self.client.get("/convert?cur1=usd&cur2=usd&amount=1")
            html = response.get_data(as_text=True)

            # Test Response
            self.assertEqual(response.status_code, 200)

            # Test HTML
            self.assertIn('<h1>Results</h1>', html)
            self.assertIn('<h3>US$ 1.0 equals: </h3>', html)
            self.assertIn('<h3>US$ 1.0</h3>', html)

    def test_convert_invalid(self):
        """Tests if user attempts to convert invalid data"""

        with self.client:
            """Invalid currency should return 500 status response"""
            response = self.client.get("/convert?cur1=www&cur2=http&amount=1")
            html = response.get_data(as_text=True)

            # Test Response
            self.assertEqual(response.status_code, 500)
