import hashlib as hash
from time import time
class Block:
    def __init__(self, index, transactions, prev_hash, PoW):
        self.index = index
        # self.timestamp = time()
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.PoW = PoW
        self.hash = self.gen_hash()

    def __str__(self):
        return "Block number {} \n hash numer {} \n prev hash number {}".format(self.index, self.hash, self.prev_hash)
        
    def gen_hash(self):
        hasher = hash.sha256()
        hasher.update("{}{}{}".format(self.transactions, self.prev_hash, self.PoW).encode("utf-8"))
        return hasher.hexdigest()