from block import *
from Transaction import *
from time import time
from flask import Flask, jsonify, request
import json
import hashlib as hash
class Blockchain: # todo: implement transaction validation
#todo: make each node able to mine, listen for creation of new blocks, verify it and restart the race as soon as possible
    def __init__(self):
        self.chain = [] #chain of blocks
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

connected_ports = set()
print(connected_ports)

l = []

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return json.dumps(l)

@app.route("/new_block", methods=['GET'])
def mine():
    block = blockchain.mine()
    return json.dumps(block.__dict__)

@app.route("/blockinfo", methods=['GET'])
def blockinfo():
    return json.dumps([b.__dict__ for b in blockchain.chain])

@app.route("/connected_ports", methods=['GET', 'DELETE', 'POST'])
def connected_ports_ops():
    global connected_ports
    if request.method == 'GET':
        return json.dumps(list(connected_ports))
    elif request.method == 'DELETE':
        ports = request.get_json()['port']
        if type(ports) is list:
            if all(type(p) is int for p in ports):
                ports = set(ports)
                initial_size = len(connected_ports) 
                connected_ports = connected_ports - ports
                return "Removed {} port(s)".format(initial_size - len(connected_ports)), 200
                 
        elif type(ports) is int:
            if ports in connected_ports:
                connected_ports.remove(ports)
                return "Removed port {}".format(ports), 200
            return "Requested port has not been connected to yet", 200
        else:
            return "Invalid request", 200
    elif request.method == 'POST':
        ports = request.get_json()['port']
        if type(ports) is list:
            if all(type(p) is int for p in ports):
                ports = set(ports)
                ports = ports - connected_ports
                connected_ports = connected_ports | ports
            else:
                return "Invalid request", 200
        elif type(ports) is int:
            if ports not in connected_ports:
                connected_ports.add(ports)
            else:
                return "Port is already connected"
        else:
            return "Invalid request", 200
        return "Added successfully",200

    

# print(blockchain.validate_block(123))
# todo: fork