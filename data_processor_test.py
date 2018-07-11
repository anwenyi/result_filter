import unittest
from mock import Mock
from numpy.core.tests.test_scalarinherit import D

from data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def test_load_file_when_file_is_empty(self):
        data = DataProcessor.load_file("")
        self.assertEqual(None, data)

    def test_load_file_when_file_not_exist(self):
        data = DataProcessor.load_file("not_exist.csv")
        self.assertEqual(None, data)

    def test_filter_info_wrong_data_format(self):
        data = '16983624@#!$@#$@#$'
        test_processor = DataProcessor()
        with self.assertRaises(TypeError):
            test_processor.filter_info(data)

