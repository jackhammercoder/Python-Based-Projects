
from mrjob.job import MRJob

class MovieCount(MRJob):

    def mapper(self, _, line):
        split_c = line.split("::")[2]
        for genre in split_c.split('|'):
            yield genre, 1

    def reducer(self, key, values):
        yield key, sum(values)
        

if __name__ == '__main__':
    MovieCount.run()