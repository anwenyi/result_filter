import os
import sys
import csv


class DataProcessor(object):
    LEGAL_LINE_LENGTH = 7
    INDEX_OF_SALARY = 5
    INDEX_OF_EMPLOYEE_ID = 1
    DEFAULT_FILE_HEADER = ['RecordId', 'EmployID', 'Name', 'Age', 'Year', 'Salary', 'Type']
    """
    load_file method loads the file from the current folder and check if it's valid , with open will close file if any
    exception happened
    """

    @staticmethod
    def load_file(input_file):
        if os.path.isfile(input_file):
            with open(input_file) as csv_file:
                data = csv_file.readlines()
                return data
        else:
            return None

    """filter each person and get the highest salary record for each person.
        By default , the input records are sorted"""

    def filter_info(self, data):
        result_dict = {}

        if not isinstance(data, list):
            raise TypeError("The type of the data is not list.")

        """skip the header of the file"""
        for line in data[1:]:
            if not isinstance(line, str):
                line = str(line)

            words = line.split(",")

            """if the current line is not long enough or too long then skip the line"""
            if len(words) != self.LEGAL_LINE_LENGTH:
                continue

            """TODO let Bo check"""
            if not self.is_int(words[self.INDEX_OF_EMPLOYEE_ID]):
                raise ValueError("The type of the employee id is not integer.")

            if words[self.INDEX_OF_EMPLOYEE_ID] not in result_dict:
                result_dict[words[self.INDEX_OF_EMPLOYEE_ID]] = line
            else:
                old_words = result_dict.get(words[self.INDEX_OF_EMPLOYEE_ID]).split(",")

                if self.is_int(words[self.INDEX_OF_SALARY]) and self.is_int(old_words[self.INDEX_OF_SALARY]) and \
                        int(words[self.INDEX_OF_SALARY]) > int(old_words[self.INDEX_OF_SALARY]):
                    result_dict[words[self.INDEX_OF_EMPLOYEE_ID]] = line

        return result_dict

    """Export the filtered result to a file"""

    @staticmethod
    def export_result(result_dict, output_file,
                      fieldnames=DEFAULT_FILE_HEADER):
        if os.path.isfile(output_file):
            with open(output_file, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                if not isinstance(result_dict, dict):
                    raise DictTypeException("The type of the result_dict is not dictionary.")

                for key in result_dict:
                    csv_file.write(result_dict.get(key))
        else:
            raise TypeError("The output file is valid.")

    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False


class DictTypeException(Exception):
    pass

def main(argv):
    data_p = DataProcessor()
    data = data_p.load_file("./testInput.csv")
    data_p.export_result(data_p.filter_info(data), "./filteredOutput.csv")


if __name__ == "__main__":
    main(sys.argv[1:])
