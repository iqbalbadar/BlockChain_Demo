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

    def mine_block(proof_of_work_diff, reward):
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

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str({"From Person": self.from_person , "To Person": self.to_person, "Amount" : self.amount})

class BlockChain:
    def __init__(proof_of_work_diff, reward):
        self.proof_of_work_diff = proof_of_work_diff
        self.reward = reward
        self.pending_blocks = []
        self.block_chain = []

    def add_block(block, ):
        self.pending_blocks.append(block)

    def create_first_block():
        return Block("", [], datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def validate_blocks():
        while(len(self.pending_blocks) > 0):
            block_to_validate = self.pending_blocks[0]

            if(len(pending_blocks) > 1):
                pending_blocks = pending_blocks[1:]
            else:
                pending_blocks.pop()
            
            if(block.mine_block(self.proof_of_work_diff, self.reward)):
                print("block mined successfully")
                self.block_chain.append(block)


class Miner:
    def __init__(name):
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

    b1 = Block("", transaction_1, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    b2 = Block(b1.hash, transaction_li, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    print(b2)

if __name__ == "__main__":
    main()








        
        