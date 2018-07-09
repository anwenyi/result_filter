import os,sys,csv

class DataProcessor(object):
    '''The constructor of the DataProcessor'''
    def __init__(self, input_file):
        self.input_file = input_file

    '''load_file method loads the file from current folder and check if it's valid , with open will close file if any excetption happed '''
    def load_file(self):
        with open(self.input_file) as f:
            data=f.readlines()
            for line in data:
                print(line)
            return data

    '''filter each person and get the highest salary record for each person.
        By default , the input records are sorted.'''
    def filterInfo(self, data):
        resultDict={}
        firstline = True
        for line in data[:-1]:
            if firstline:
                firstline = False
                continue
            
            words = line.split(",")
            print(words[5])
            
            if words[1] not in resultDict:
            	resultDict[str(words[1])]=line
            else:
                print("test value "+words[1])
                print(resultDict.get(''+words[1]))
                oldWords = resultDict.get(words[1]).split(",")
                
                if int(words[5])> int(oldWords[5]):
                    resultDict[''+str(words[1])]=line
            print("Dict: ")
            print(resultDict)
        
    '''Export the filted result to a file'''     
    def export_result(self,resultDict):
        with open('names.csv', 'w') as csvfile:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
           	        
        
def main(argv):
    dataP1 = DataProcessor("./testInput.csv")
    data = dataP1.load_file()
    dataP1.filterInfo(data)
    dataP1.export_result(data)

if __name__=="__main__":
    main(sys.argv[1:]) 
