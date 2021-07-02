import hashlib
import datetime
import json
import sys



class Block:
    def __init__(self, prev_hash, transactions , timestamp):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self._nonce = 0
        self.hash = self.make_hash()

    def __str__(self):
        return str({"previous hash": self.prev_hash , "Hash" : self.hash, "Transactions": str(self.transactions), "Timestamp" : self.timestamp})
    
    def __repr__(self):
        return str(self)


    def make_hash(self):
        rawData = str(self.prev_hash) + str(self.timestamp) + str(self.transactions) + str(self._nonce)
        encoded = json.dumps(rawData, sort_keys=True).encode()
        return hashlib.sha256(rawData).hexdigest()

    def mine_block(self, proof_of_work_diff):
        hash_valid_temp = "0" * proof_of_work_diff
        while( self.hash[:proof_of_work_diff] != hash_valid_temp ):
            self._nonce += 1
            if(self._nonce == sys.maxint):
                print("too large of proof of work diff for this computer, max nonce reached")
                return False

            self.hash = self.make_hash()
            print(self.hash)
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

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

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

    def mine(self, miner_name):
        transaction_for_miner = Transaction("Iqbal_Coin", miner_name, self.reward)
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

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str({"BlockChain": self.block_chain })

    def validate_blockchain(self):
        size_of_chain = len(self.block_chain)

        if( size_of_chain == 1 ):
            return True
        chain_index = 1
        
        while(chain_index >= size_of_chain):
            if(self.block_chain[chain_index].prev_hash != self.block_chain[chain_index - 1].hash):
                return False
        return True
    

def main():
    transaction_1 = Transaction("iqbal", "her", 11.56)
    transaction_2 = Transaction("her", "iqbal", 12.56 )
    transaction_3 = Transaction("cute girl", "iqbal", 33.56)
    transaction_4 = Transaction("iqbal", "shawty", 55.6)

    transaction_li = [transaction_2,transaction_3, transaction_4] 
    chain = BlockChain(4, 10)
    chain.add_transaction(transaction_1)
    chain.add_transaction(transaction_2)
    chain.add_transaction(transaction_3)
    chain.add_transaction(transaction_4)



    



    
    
    chain.mine("Jeff Bezos")

    chain.add_transaction(transaction_1)
    chain.add_transaction(transaction_2)
    chain.add_transaction(transaction_3)
    chain.add_transaction(transaction_4)

    chain.mine("Jeff Bezos")



    print(chain.validate_blockchain())


   

if __name__ == "__main__":
    main()








        
        