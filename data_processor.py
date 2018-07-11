import os,sys,csv

class DataProcessor(object):

    '''load_file method loads the file from the current folder and check if it's valid , with open will close file if any
    excetption happend '''
    def load_file(self, input_file):
        with open(input_file) as csv_file:
            data=csv_file.readlines()
            return data

    '''filter each person and get the highest salary record for each person.
        By default , the input records are sorted.'''
    def filter_info(self, data):
        result_dict={}

        LEGAL_LINE_LENGTH = 7
        INDEX_OF_SALARY = 5
        INDEX_OF_EMPLOYEE_ID = 1

        '''Skip the header of the file.'''
        for line in data[1:]:            
            words = line.split(",")

            '''If the current line is not long enough then skip'''
            if len(words) != LEGAL_LINE_LENGTH:
                continue 
            
            if words[INDEX_OF_EMPLOYEE_ID] not in result_dict:
                result_dict[words[INDEX_OF_EMPLOYEE_ID]] = line
            else:
                old_words = result_dict.get(words[INDEX_OF_EMPLOYEE_ID]).split(",")
                
                if int(words[INDEX_OF_SALARY])> int(old_words[INDEX_OF_SALARY]):
                    result_dict[str(words[INDEX_OF_EMPLOYEE_ID])] = line
        return result_dict
        
    '''Export the filted result to a file'''     
    def export_result(self, result_dict, output_path):
        with open(output_path, 'w') as csv_file:
            fieldnames = ['RecordId', 'EmployID', 'Name', 'Age', 'Year', 'Salary', 'Type']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for key in result_dict:
                csv_file.write(result_dict.get(key))


def main(argv):
    dataP1 = DataProcessor()
    data = dataP1.load_file("./testInput.csv")
    dataP1.export_result(dataP1.filter_info(data), "./filteredOutput.csv")


if __name__=="__main__":
    main(sys.argv[1:]) 
