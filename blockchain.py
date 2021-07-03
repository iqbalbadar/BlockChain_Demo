import hashlib
import datetime
import json
import sys
from Block import * 
from Transaction import * 


BLOCKCHAIN_REWARD_FACTOR = 210000

class BlockChain:

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    def __init__(self, proof_of_work_diff):
        self.proof_of_work_diff = proof_of_work_diff
        self.pending_transactions = []
        self.block_chain = [self.create_first_block()]
        self.reward = reward = BLOCKCHAIN_REWARD_FACTOR / len(self.block_chain)


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
            self.reward = reward = BLOCKCHAIN_REWARD_FACTOR / len(self.block_chain)
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
    chain = BlockChain(4)
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








        
        