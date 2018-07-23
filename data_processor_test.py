import unittest

from data_processor import DataProcessor, DictTypeException


class TestDataProcessor(unittest.TestCase):

    """Test load_file method"""
    def test_load_file_when_file_is_empty(self):
        data = DataProcessor.load_file("")
        self.assertEqual(None, data)

    def test_load_file_when_file_not_exist(self):
        data = DataProcessor.load_file("not_exist.csv")
        self.assertEqual(None, data)

    """Test filter_info method"""
    def test_filter_info_wrong_data_format(self):
        data = '16983624@#!$@#$@#$'
        test_processor = DataProcessor()
        with self.assertRaises(TypeError):
            test_processor.filter_info(data)

    def test_filter_info_empty_data(self):
        data = []
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_empty_string_data(self):
        data = ['']
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_not_long_enough(self):
        data = [1, 1]
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_extra_column(self):
        data = ['RecordId,EmployID,Name,Age,Year,Salary,Type', '10021,1,Rob,23,2008,65580,Sport,ExtraData']
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_no_header(self):
        data = ['10021,1,Rob,23,2008,65580,Sport']
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_double_header(self):
        data = ['RecordId,EmployID,Name,Age,Year,Salary,Type', 'RecordId,EmployID,Name,Age,Year,Salary,Type']
        test_processor = DataProcessor()
        with self.assertRaises(ValueError):
            test_processor.filter_info(data)

    def test_filter_info_right_data_double_empty_header(self):
        data = ['', '']
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_all_int(self):
        data = [0, 0, 0, 0, 0, 0, 0]
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_nest_list(self):
        data = [[], 0, [], [], 0, 0, 0]
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data_nest_list_but_right_employid_and_salary(self):
        data = [[], 0, [], [], 0, 0, 0]
        test_processor = DataProcessor()
        self.assertEqual({}, test_processor.filter_info(data))

    def test_filter_info_right_data(self):
        data = ['RecordId,EmployID,Name,Age,Year,Salary,Type', '10021,1,Rob,23,2008,65580,Sport']
        test_processor = DataProcessor()
        self.assertEqual({'1': '10021,1,Rob,23,2008,65580,Sport'}, test_processor.filter_info(data))

    """Test export_result method"""
    def test_export_file_when_file_is_empty(self):
        with self.assertRaises(TypeError):
            DataProcessor.export_result({}, "")

    def test_export_file_when_file_not_exist(self):
        with self.assertRaises(TypeError):
            DataProcessor.export_result({}, "not_exist.csv")

    def test_export_file_when_not_dict(self):
        with self.assertRaises(DictTypeException):
            DataProcessor.export_result("wrong_data", "./test_filteredOutput.csv")

    def test_export_file_when_dict_right_value(self):
        DataProcessor.export_result({'1': '10021,1,Rob,23,2008,65580,Sport'}, "./test_filteredOutput.csv")
