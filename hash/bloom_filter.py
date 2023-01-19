import math
import mmh3
import bitarray

class BloomFilter(object):
    def __init__(self, items_count, fp_prob):
        self.fp_prob = fp_prob
  
        # Size of bit array to use
        self.size = self.get_size(items_count, fp_prob)
  
        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, items_count)
  
        # Bit array of given size
        self.bit_array = bitarray.bitarray(self.size)
  
        # initialize all bits as 0
        self.bit_array.setall(0)
    
    @classmethod
    def get_size(self, n, p):
        return int(-(n * math.log(p))/(math.log(2)**2))
  
    @classmethod
    def get_hash_count(self, m, n):
        k = (m / n) * math.log(2)

        return int(k)

    def add(self, item):
        digests = []

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            self.bit_array[digest] = True
  
    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                return False
            
        return True
