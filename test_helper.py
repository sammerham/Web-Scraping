from typing import Dict
import helper
from unittest import TestCase

VALID_URL = 'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183'
INVALID_URL = 'https://www.lendingtree.com/reviews/personal/first-midwest-bank/529033'
ERR = {'err': "Please enter a valid lender's name and or id"}
TEST_REVIEW = {
    "Customer_Name": "Brandon from Fayetteville, NC",
    "Review_Date": "Reviewed in December 2021",
    "Review_Rating": "(5 of 5)stars",
    "Review_Text": "Mrs. Navarrete was very professional and streamlined the process to make it easier on me. Highly recommend.Brandon",
    "Review_Title": "Great experience"
}

class ReviewsTestCase(TestCase):
    """Unit tests."""

    def test_get_reviews(self):
        """test get review works and return a list of reviews if provided a valid url."""
        self.assertIsInstance(helper.get_reviews(VALID_URL), list)
        self.assertIsInstance(helper.get_reviews(INVALID_URL), dict)
        self.assertIn(TEST_REVIEW, helper.get_reviews(VALID_URL))
        self.assertEqual(helper.get_reviews(INVALID_URL), ERR)
