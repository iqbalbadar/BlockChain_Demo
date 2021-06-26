import hashlib
import datetime

class Block:
    def __init__(self, prev_hash, transactions , timestamp):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self._nonce = 0
        self.hash = self.make_hash()

    def __str__(self):
        return str({"previous hash": self.prev_hash , "Hash" : self.hash, "Transactions": str(self.transactions), "Timestamp" : self.timestamp})
    
    def make_hash(self):
        rawData = str(self.prev_hash) + str(self.timestamp) + str(self.transactions) + str(self._nonce)
        return hashlib.sha256(rawData.encode()).hexdigest()

    def mine_block(proof_of_work_diff, miner, reward):
        hash_valid_temp = " " * proof_of_work_diff
        print("going through proof of work algo")
        while( hash[:proof_of_work_diff] != hash_valid_temp ):
            _nonce += 1
            hash = self.make_hash
        print("{0} this hash was mined" , hash )
        return true

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
    transaction_1 = Transaction("iqbal", "her", 11.56)
    transaction_2 = Transaction("her", "iqbal", 12.56 )

    b1 = Block("", transaction_1, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    b2 = Block(b1.hash, transaction_2, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    print(b2)

if __name__ == "__main__":
    main()








        
        