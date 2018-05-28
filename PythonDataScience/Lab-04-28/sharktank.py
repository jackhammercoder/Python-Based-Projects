
from mrjob.job import MRJob

class CompanyCount(MRJob):

    def mapper(self, _, line):
        split_line = line.split(",")
        
        if split_line[3] == 'Yes':
            yield (split_line[4], split_line[5], "Funded") , 1
        else: 
            yield (split_line[4], split_line[5],"Funded" ) , 0 
            
        yield (split_line[4], split_line[5],"Total"), 1

    def reducer(self, key, values):
        yield key, sum(values)
        

if __name__ == '__main__':
    CompanyCount.run()