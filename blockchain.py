import hashlib
import datetime
import json

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
        encoded = json.dumps(rawData, sort_keys=True).encode()
        return hashlib.sha256(rawData).hexdigest()

    def mine_block(self, proof_of_work_diff):
        hash_valid_temp = "0" * proof_of_work_diff
        print(len(hash_valid_temp))
        print("going through proof of work algo")
        while( self.hash[:proof_of_work_diff] != hash_valid_temp ):
            self._nonce += 1
            self.hash = self.make_hash()
        print("this hash was mined" , self.hash )
        return True

class Transaction :
    def __init__(self, from_person, to_person, amount):
        self.from_person = from_person
        self.to_person = to_person
        self.amount = amount

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str({"From Person": self.from_person , "To Person": self.to_person, "Amount" : self.amount})

class BlockChain:
    def __init__(self, proof_of_work_diff, reward):
        self.proof_of_work_diff = proof_of_work_diff
        self.reward = reward
        self.pending_transactions = []
        self.block_chain = [self.create_first_block()]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def create_first_block(self):
        first_transaction = Transaction("","",0)
        return Block("", [first_transaction], datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def mine(self, miner):
        transaction_for_miner = Transaction("Iqbal_Coin", miner.name, self.reward)
        self.pending_transactions.append(transaction_for_miner)
        print(self.block_chain)

        prev_hash = self.block_chain[-1].hash
        block_to_mine = Block(prev_hash, self.pending_transactions, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        print(block_to_mine)

        if(block_to_mine.mine_block(self.proof_of_work_diff)):
            print("Block is mined, moving to the chain!")
            self.block_chain.append(block_to_mine)
        else:
            print("Block was not mined, not allowed on the chain")

class Miner:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def add_to_wallet(reward):
        self.amount += reward
    

def main():
    transaction_1 = Transaction("iqbal", "her", 11.56)
    transaction_2 = Transaction("her", "iqbal", 12.56 )
    transaction_3 = Transaction("cute girl", "iqbal", 33.56)
    transaction_4 = Transaction("iqbal", "shawty", 55.6)

    transaction_li = [transaction_2,transaction_3, transaction_4] 
    block_chain = BlockChain(5, 10)
    block_chain.add_transaction(transaction_1)
    block_chain.add_transaction(transaction_2)
    block_chain.add_transaction(transaction_3)
    block_chain.add_transaction(transaction_4)
    
    miner = Miner("Jeff Bezos")
    block_chain.mine(miner)

if __name__ == "__main__":
    main()








        
        