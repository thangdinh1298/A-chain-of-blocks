from block import *
from Transaction import *
from time import time
from flask import Flask, jsonify
import json
import hashlib as hash
class Blockchain: # todo: implement transaction validation
#todo: make each node able to mine, listen for creation of new blocks, verify it and restart the race as soon as possible
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        #appending the genesis block
        self.chain.append(
            Block(self.current_transactions, "-1", 16))
    def new_block(self, GoldenNonce):
        nb = Block(self.current_transactions, self.last_block().gen_hash(), GoldenNonce) 
        self.chain.append(nb)

        current_transactions = []
        return nb

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

    def mine(self):
        combination = ""
        for t in self.current_transactions:
            combination += str(t)
        combination += self.last_block().gen_hash()
        nonce = 0
        while self.valid_proof(combination, nonce) == False:
            nonce+=1
        return self.new_block(nonce)


    def valid_proof(self, combination, nonce):
        hasher = hash.sha256()
        hasher.update("{}{}".format(combination, nonce).encode())
        hex = hasher.hexdigest()
        # print(hex)
        # print(last_proof, proof)
        if hasher.hexdigest()[:5] == "00000":
            print(hex)
            return True
        return False

    def validate_block(self, block):
        if not isinstance(block, Block):
            print("Object is not a block")
            return False
        if block.prev_hash != self.last_block().gen_hash():
            print("This block is not linked to the last block")
            return False
        # string  = ""
        # for t in block.transactions:
        #     string += str(t)
        # string += block.prev_hash
        # string += str(block.GoldenNonce)
        # hasher = hash.sha256()
        # hasher.update(string.encode())    
        # if hasher.hexdigest()[0:5] != "00000":
        #     print("Block's hash does not satisfy the target")
        #     return False
        # print("Block is valid")
        return True
    
blockchain = Blockchain()
# print(blockchain.mine())
# print(blockchain.validate_block(Block([], "000005dd81520ea6a43a7eb585e5968f173a3113e3bb6d9dfbbb9b6a5ea3e8e8", 3000992)))
# print(blockchain.mine())

app = Flask(__name__)

@app.route("/")
def Hello_World():
    return json.dumps({"123": 123})

@app.route("/mine")
def mine():
    block = blockchain.mine()
    return json.dumps(block.__dict__)

@app.route("/numblocks")
def numblocks():
    return json.dumps([b.__dict__ for b in blockchain.chain])
# @app.route("/add_transaction")
# def add_transaction():
    

# print(blockchain.validate_block(123))
# todo: fork