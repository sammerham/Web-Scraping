import helper
from unittest import TestCase

VALID_URL = 'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183'
INVALID_URL = 'https://www.lendingtree.com/reviews/personal/first-midwest-bank/529033'
ERR = {'err': "Please enter a valid lender's name and or id"}
TEST_REVIEW = {'Customer_Name': 'Patricia from Holly Ridge, NC', 'Review_Title': 'It was a good experience',
       'Review_Text': 'The process was quick and easy.  Christine was very helpful.  Rates were good. I would highly recommend First Midwest Bank', 'Review_Date': 'Reviewed in December 2021', 'Review_Rating': '(5 of 5)stars'}


class AdditionTestCase(TestCase):
    """Unit tests."""

    def test_get_reviews(self):
        """test get review works and return a list of reviews if provided a valid url."""
        self.assertIsInstance(helper.get_reviews(VALID_URL), list)
        self.assertIn(TEST_REVIEW, helper.get_reviews(VALID_URL))
        self.assertEqual(helper.get_reviews(INVALID_URL), ERR)
