import hashlib
import datetime
import json
import sys
from Block import * 
from Transaction import * 
import sqlite3
from SqlWrapper import *


BLOCKCHAIN_REWARD_FACTOR = 210000
INDEX_OF_AMOUNT = 2
INDEX_OF_TRANSACTIONS = 3
INDEX_OF_SENDER = 0
INDEX_OF_RECIPENT = 1


class BlockChain:
    def __init__(self, proof_of_work_diff=3):
        self.sql = SqlWrapper()
        print("starting blockchain")
        self.proof_of_work_diff = proof_of_work_diff
        self.pending_transactions = self.get_pending_transactions()
        
        self.reward = BLOCKCHAIN_REWARD_FACTOR / self.get_blockchain_length()
        print(self.reward)

    def get_pending_transactions(self):
        pending_transactions = self.sql.get_pending_transactions()
        print(pending_transactions)
        return pending_transactions

    def get_num_trans(self):
        num_trans = self.sql.get_num_trans()
        print(num_trans)
        return num_trans

    def add_transaction(self, from_person, to_person, amount):
        id_of_trans = self.sql.get_num_trans() + 1
        new_transaction = Transaction(from_person, to_person, amount, id_of_trans)
        self.pending_transactions.append(new_transaction)
        print("added pending transaction ", new_transaction)

    def get_blockchain_length(self):
        block_chain_length = self.sql.get_blockchain_length()
        # if blockchain length is zero, create the genensis block
        if(block_chain_length == 0):
            self.create_first_block()
            block_chain_length = 1

        print(block_chain_length)
        return block_chain_length

    def close(self):
        self.sql.insert_pending_transactions(self.pending_transactions)
        
    def create_first_block(self):
        first_transaction = Transaction("" , "", 0, 0)
        first_block = Block("", [first_transaction], datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))       
        self.sql.insert_into_blockchain_table(first_block)
        return Block("", [first_transaction], datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def get_prev_hash(self):
        return self.sql.get_prev_hash()

    def mine(self, miner_name, transaction_id):
        transaction_for_miner = Transaction("Iqbal_Coin", miner_name, self.reward, transaction_id)
        self.pending_transactions.append(transaction_for_miner)

        prev_hash = self.get_prev_hash()
        block_to_mine = Block(prev_hash, self.pending_transactions, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        #print(block_to_mine)

        if(block_to_mine.mine_block(self.proof_of_work_diff)):
            print("Block is mined, moving to the chain!")
            self.sql.insert_into_blockchain_table(block_to_mine)
            self.reward = reward = BLOCKCHAIN_REWARD_FACTOR / self.get_blockchain_length()
            self.pending_transactions = []
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








        
        