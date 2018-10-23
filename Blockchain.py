from block import *
from Transaction import *
from time import time
import hashlib as hash
class Blockchain: # todo: implement transaction validation
#todo: make each node able to mine, listen for creation of new blocks, verify it and restart the race as soon as possible
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        #appending the genesis block
        self.chain.append(
            Block(len(self.chain), self.current_transactions, "-1", 16))
    def new_block(self, PoW):
        self.chain.append(
            Block(len(self.chain), self.current_transactions, self.last_block().hash, PoW))

    def new_transaction(self, sender, receipient, amount):
        self.current_transactions.append(
            Transaction(sender, recipient, amount))

        # return self.last_block().index + 1

    def last_block(self):
        return self.chain[-1]

    def __str__(self):
        string = ""
        for block in self.chain:
            string += block.__str__()
            string += "\n"
        return string

    def proof_of_work(self):
        last_proof = self.last_block().PoW

        proof = 0 
        while self.valid_proof(last_proof, proof) == False:
            proof+=1
            # print(last_proof, proof)
        return proof

    def valid_proof(self, last_proof, proof):
        hasher = hash.sha256()
        hasher.update("{}{}".format(last_proof, proof).encode())
        hex = hasher.hexdigest()
        print(hex)
        # print(last_proof, proof)
        return hasher.hexdigest()[:4] == "00000000"

blockchain = Blockchain()
print(blockchain.proof_of_work())
# print(hasher.hexdigest())