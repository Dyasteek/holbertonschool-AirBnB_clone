#!/usr/bin/python3
"""Unittest for models/base_model.py"""
import unittest
from models.base_model import BaseModel


class to_TestBaseModel(unittest.TestCase):
    """Testing base model class"""

    def test_base_model_instance(self):
        """method testing base model instance"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_base_model_name(self):
        """method testing base model name"""
        self.assertIsInstance(__class__.__name__, str)

    def test_base_model_id_str(self):
        """method testing base model id is string"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_base_model_to_dict(self):
        """method testing base model to_dict"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)

    def test_id_is_public(self):
        """method testing id is public"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))

    def test_created_at_is_public(self):
        """method testing created_at is public"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "created_at"))

    def test_updated_at_is_public(self):
        """method testing updated_at is public"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "updated_at"))

class to_TestBaseModel_to_dict(unittest.TestCase):
    """Testing base model to_dict"""

    def test_to_dict_base_model_dict(self):
        """method testing base model to_dict type"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)

    def test_to_dict_base_model_with_arg(self):
        """method testing base model to_dict with arg"""
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)

    def test_to_dict_base_model_created_at(self):
        """method testing base model to_dict created_at"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["created_at"], base.created_at.isoformat())

    def test_to_dict_base_model_updated_at(self):
        """method testing base model to_dict updated_at"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["updated_at"], base.updated_at.isoformat())

    def test_to_dict_base_model_str(self):
        """method testing base model to_dict str"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")

class to_TestBaseModel_save(unittest.TestCase):
    """Testing base model save"""

    def test_save_base_model(self):
        """method testing base model save"""
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_save_base_model_with_arg(self):
        """method testing base model save with arg"""
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)
