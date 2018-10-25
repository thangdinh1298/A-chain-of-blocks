import hashlib as hash
from time import time
class Block:
    def __init__(self, transactions, prev_hash, GoldenNonce):
        # self.timestamp = time()
        ## block header
        self.prev_hash = prev_hash
        self.GoldenNonce = GoldenNonce
        ## block body
        self.transactions = transactions

    # def __str__(self):
    #     return "Block number {} \n hash numer {} \n prev hash number {}".format(self.index, self.hash, self.prev_hash)
        
    def gen_hash(self):
        hasher = hash.sha256()
        string = ""
        for t in self.transactions:
            string += t
        string += self.prev_hash
        string += str(self.GoldenNonce)
        hasher.update(string.encode())
        return hasher.hexdigest()