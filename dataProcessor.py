import os,sys

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

    '''filter each person and get the highest salary record for each person'''
    def filterInfo(self, data):
        pass	    
        
def main(argv):
    dataP1 = DataProcessor("./test.csv")
    dataP1.load_file()

if __name__=="__main__":
    main(sys.argv[1:]) 
