
from mrjob.job import MRJob

class BabiesCount(MRJob):

    def mapper(self, _, line):
        split_l = line.split(",")
        yield split_l[0][0], 1

    def reducer(self, key, values):
        yield key, sum(values)
        

if __name__ == '__main__':
    BabiesCount.run()