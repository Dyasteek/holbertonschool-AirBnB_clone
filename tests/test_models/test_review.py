#!/usr/bin/python3
"""Unittest for models/review.py"""
import unittest
from models.review import Review


class to_Test_Review(unittest.TestCase):
    """Test Review classs"""

    def test_review_is_instance(self):
        """Test Review instance"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_name_str(self):
        """Test Review name"""
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_review_id_str(self):
        """Test Review id"""
        review = Review()
        self.assertIsInstance(review.id, str)

    def test_review_place_id_str(self):
        """Test Review place_id"""
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_review_user_id_str(self):
        """Test Review user_id"""
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_review_text_str(self):
        """Test Review text"""
        review = Review()
        self.assertIsInstance(review.text, str)

class to_Test_Review_save(unittest.TestCase):
    """Test Review save method"""

    def test_review_save_with_arg(self):
        """Test Review save method with arg"""
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

class to_Test_Review_to_dict(unittest.TestCase):
    """Test Review to_dict method"""

    def test_review_to_dict_dict(self):
        """Test Review to_dict method"""
        review = Review()
        self.assertIsInstance(review.to_dict(), dict)
    
    def test_review_to_dict_with_arg(self):
        """Test Review to_dict method with arg"""
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)
