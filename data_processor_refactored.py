import os,sys,csv

class DataProcessor(object):

    '''load_file method loads the file from current folder and check if it's valid , with open will close file if any excetption happed '''
    def load_file(self, input_file):
        with open(input_file) as f:
            data=f.readlines()
            return data

    '''filter each person and get the highest salary record for each person.
        By default , the input records are sorted.'''
    def filter_info(self, data):
        resultDict={}

        LEGAL_LINE_LENGTH = 7
        INDEX_OF_SALARY = 5
        INDEX_OF_EMPLOYEE_ID = 1

        '''Skip the header of the file.'''
        for line in data[1:]:            
            words = line.split(",")
            
            if len(words)!=LEGAL_LINE_LENGTH:
                continue 
            
            if words[INDEX_OF_EMPLOYEE_ID] not in resultDict:
            	resultDict[words[INDEX_OF_EMPLOYEE_ID]]=line
            else:
                oldWords = resultDict.get(words[INDEX_OF_EMPLOYEE_ID]).split(",")
                
                if int(words[INDEX_OF_SALARY])> int(oldWords[INDEX_OF_SALARY]):
                    resultDict[str(words[INDEX_OF_EMPLOYEE_ID])]=line
        return resultDict
        
    '''Export the filted result to a file'''     
    def export_result(self,resultDict):
        with open('filteredOutput.csv', 'w') as csvfile:
            fieldnames = ['RecordId','EmployID','Name','Age','Year','Salary','Type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key in resultDict:
                csvfile.write(resultDict.get(key))
           	        
        
def main(argv):
    dataP1 = DataProcessor()
    data = dataP1.load_file("./testInput.csv")
    dataP1.export_result(dataP1.filter_info(data))

if __name__=="__main__":
    main(sys.argv[1:]) 
