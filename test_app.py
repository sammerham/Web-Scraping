from app import app
from unittest import TestCase

BASE_URL = 'https://www.lendingtree.com/reviews/personal/'
lender_name='freedomplus'
lender_id= 51697094
invalid_id=111111


class ShowReviewsTestCase(TestCase):
    """Examples of integration tests: testing Flask app."""

    def test_show_reviews(self):
        """test get review works and return a list of reviews if provided a valid url."""
        with app.test_client() as client:
            # can now make get request to flask via `client`
            resp = client.get(f"/reviews/{lender_name}/{lender_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Reviews', html)

    def test_show_reviews_invalidurl(self):
        """test get review works and return err message if provided invalid url."""
        with app.test_client() as client:
            # can now make get request to flask via `client`
            resp = client.get(f"/reviews/{lender_name}/{invalid_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Errors", html)
