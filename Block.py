import hashlib
import datetime
import json
import sys

class Block:
    def __init__(self, prev_hash="", transactions=[], timestamp=""):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.make_hash()

    def __str__(self):
        return str({"previous hash": self.prev_hash , "Hash" : self.hash, "Transactions": str(self.transactions), "Timestamp" : self.timestamp})
    
    def __repr__(self):
        return str(self)

    def make_hash(self):
        rawData = str(self.prev_hash) + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        encoded = json.dumps(rawData, sort_keys=True).encode()
        return hashlib.sha256(rawData).hexdigest()

    def mine_block(self, proof_of_work_diff):
        hash_valid_temp = "0" * proof_of_work_diff
        while( self.hash[:proof_of_work_diff] != hash_valid_temp ):
            self.nonce += 1
            if(self.nonce == sys.maxint):
                print("too large of proof of work diff for this computer, max nonce reached")
                return False

            self.hash = self.make_hash()
           # print(self.hash)
        print("this hash was mined" , self.hash )
        return True

