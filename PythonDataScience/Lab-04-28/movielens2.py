
from mrjob.job import MRJob

class RatingsCount(MRJob):

    def mapper(self, _, line):
        movies = line.split("::")
        yield movies[1], 1

    def reducer(self, key, values):
        yield key, sum(values)
        

if __name__ == '__main__':
    RatingsCount.run()