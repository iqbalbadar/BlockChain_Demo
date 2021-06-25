import hashlib
from datetime import date

class Block:
    def __init__(self, prev_hash, transactions , timestamp):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self._nonce = 0
        hash = self.make_hash()

    def __str__(self):
        return str({"previous hash": self.prev_hash , "Transactions": str(self.transactions), "Timestamp" : self.timestamp})
    
    def make_hash(self):
        rawData = str(self.prev_hash) + str(self.timestamp) + str(self.transactions) + str(self._nonce)
        return hashlib.sha256(rawData.encode())

    def mine_block(proof_of_work_diff):
        hash_valid_temp = " " * proof_of_work_diff
        print("going through proof of work algo")
        while( hash[:proof_of_work_diff] != hash_valid_temp ):
            _nonce += 1
            hash = self.make_hash
        print("{0} this hash was mined" , hash )

class Transaction :
    def __init__(self, from_person, to_person, amount):
        self.from_person = from_person
        self.to_person = to_person
        self.amount = amount
    
    def __str__(self):
        return str({"From Person": self.from_person , "To Person": self.to_person, "Amount" : self.amount})

class BlockChain (object):
    def _init_(proof_of_work_diff, reward):
        proof_of_work_diff = self.proof_of_work_diff
        reward = self.reward
        transactions = []
        chain = list(self.create_first_block) 
    
    def make_transaction(transaction):
        transactions.append(transaction)

    def create_first_block():
        return Block("", [], datetime.today())


def main():
    print("hello")
    transaction_1 = Transaction("iqbal", "her", 11.56)


    b = Block("", transaction_1, date.today())
    print(b)

if __name__ == "__main__":
    main()

fdafad






        
        