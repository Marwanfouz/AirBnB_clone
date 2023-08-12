#!/usr/bin/python3
"""test base model"""
import models
from time import sleep
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """class test base model"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        i1 = BaseModel()
        i2 = BaseModel()
        self.assertNotEqual(i1.id, i2.id)

    def test_two_models_different_created_at(self):
        i1 = BaseModel()
        sleep(0.05)
        i2 = BaseModel()
        self.assertLess(i1.created_at, i2.created_at)

    def test_two_models_different_updated_at(self):
        i1 = BaseModel()
        sleep(0.05)
        i2 = BaseModel()
        self.assertLess(i1.updated_at, i2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        i = BaseModel()
        i.id = "123456"
        i.created_at = i.updated_at = dt
        istr = i.__str__()
        self.assertIn("[BaseModel] (123456)", istr)
        self.assertIn("'id': '123456'", istr)
        self.assertIn("'created_at': " + dt_repr, istr)
        self.assertIn("'updated_at': " + dt_repr, istr)

    def test_args_unused(self):
        i = BaseModel(None)
        self.assertNotIn(None, i.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        i = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(i.id, "345")
        self.assertEqual(i.created_at, dt)
        self.assertEqual(i.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        i = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(i.id, "345")
        self.assertEqual(i.created_at, dt)
        self.assertEqual(i.updated_at, dt)

    def test_one_save(self):
        i = BaseModel()
        sleep(0.05)
        first_updated_at = i.updated_at
        i.save()
        self.assertLess(first_updated_at, i.updated_at)

    def test_two_saves(self):
        i = BaseModel()
        sleep(0.05)
        first_updated_at = i.updated_at
        i.save()
        second_updated_at = i.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        i.save()
        self.assertLess(second_updated_at, i.updated_at)

    def test_save_with_arg(self):
        i = BaseModel()
        with self.assertRaises(TypeError):
            i.save(None)

    def test_save_updates_file(self):
        i = BaseModel()
        i.save()
        iid = "BaseModel." + i.id
        with open("file.json", "r") as f:
            self.assertIn(iid, f.read())

    def test_kwargs(self):
        """ """
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """ """
        i = BaseModel()
        self.assertEqual(str(i), '[{}] ({}) {}'.format('BaseModel', i.id,
                        i.__dict__))

    def test_todict(self):
        """method test"""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """method test"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_updated_at(self):
        """method test"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at == new.updated_at)

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)
