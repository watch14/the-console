#!/usr/bin/python3
"""test"""

import unittest
from models.review import Review
from datetime import datetime
from models import storage


class TestReview(unittest.TestCase):
    """test"""

    def setUp(self):
        """test"""
        self.review = Review()

    def tearDown(self):
        """test"""
        pass

    def test_attributes(self):
        """test"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_default_values(self):
        """test"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_save_reload(self):
        """test"""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Great experience!"
        self.review.save()
        key = "{}.{}".format(self.review.__class__.__name__, self.review.id)
        reloaded_review = storage.all()[key]
        self.assertEqual(reloaded_review.place_id, "123")
        self.assertEqual(reloaded_review.user_id, "456")
        self.assertEqual(reloaded_review.text, "Great experience!")

    def test_to_dict(self):
        """test"""
        self.review.place_id = "789"
        self.review.user_id = "012"
        self.review.text = "Amazing view from the balcony"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "789")
        self.assertEqual(review_dict['user_id'], "012")
        self.assertEqual(review_dict['text'], "Amazing view from the balcony")
        self.assertEqual(review_dict['__class__'], "Review")
        self.assertTrue('id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_created_at_updated_at(self):
        """test"""
        self.assertTrue(isinstance(self.review.created_at, datetime))
        self.assertTrue(isinstance(self.review.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
