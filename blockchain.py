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
INDEX_OF_TRANSACTIONS_ID = 1


class BlockChain:
    def __init__(self, proof_of_work_diff=3):
        self.sql = SqlWrapper()
        self.proof_of_work_diff = proof_of_work_diff
        self.pending_transactions = self.get_pending_transactions()
        self.reward = BLOCKCHAIN_REWARD_FACTOR / self.get_blockchain_length()

    def get_pending_transactions(self):
        pending_transactions_sql = self.sql.get_pending_transactions()
        pending_transactions = []

        for pending_transaction_sql in pending_transactions_sql:
             pending_transactions.append( Transaction(pending_transaction_sql[0], pending_transaction_sql[1], pending_transaction_sql[2], pending_transaction_sql[3]))
        return pending_transactions

    def get_num_trans(self):
        num_trans = self.sql.get_num_trans()
        return num_trans

    def get_transaction(self ,id):
        return self.sql.get_transaction(id)

    def add_transaction(self, from_person, to_person, amount):
        id_of_trans = self.sql.get_num_trans()
        new_transaction = Transaction(from_person, to_person, amount, id_of_trans)
        self.pending_transactions.append(new_transaction)
        self.sql.insert_pending_transaction(new_transaction)
       # print("added pending transaction ", new_transaction)

    def get_blockchain_length(self):
        block_chain_length = self.sql.get_blockchain_length()
        # if blockchain length is zero, create the genensis block
        if(block_chain_length == 0):
            self.create_first_block()
            block_chain_length = 1

        return block_chain_length
        
    def create_first_block(self):
        # since its the first transaction insert it into sql but make sure to 
        # update its processed field = 1 since itll become apart of a block
        first_transaction = Transaction("" , "", 0, 0)
        self.sql.insert_pending_transaction(first_transaction)
        self.sql.update_pending_to_processed_transactions()        

        first_block = Block("", [first_transaction], datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))      
        self.sql.insert_into_blockchain_table(first_block)

    def get_prev_hash(self):
        return self.sql.get_prev_hash()

    def mine(self, miner_name):
        # if the transaction length is 0 then we cant make a block
        if(len(self.pending_transactions) == 0 ):
            print("No block can be made since there are no pending transactions")
            return

        transaction_for_miner = Transaction("Iqbal_Coin", miner_name, self.reward, self.sql.get_num_trans())
        self.sql.insert_pending_transaction(transaction_for_miner)

        self.pending_transactions.append(transaction_for_miner)

        prev_hash = self.get_prev_hash()
        block_to_mine = Block(prev_hash, self.pending_transactions, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        print("block_to_mine: ", block_to_mine)

        # if its mined we, insert the block into the chain, 
        # update the transactions as processed, update the reward since the 
        # blockchain length increased and we have no more pending transactions :)
        if(block_to_mine.mine_block(self.proof_of_work_diff)):
            print("Block is mined, moving to the chain!")
            
            self.sql.insert_into_blockchain_table(block_to_mine)
            self.sql.update_pending_to_processed_transactions()

            self.reward =  BLOCKCHAIN_REWARD_FACTOR / self.get_blockchain_length()
            self.pending_transactions = []
            
        else:
           print("Block was not mined, not allowed on the chain")
    
    def get_all_transactions(self):
        return self.sql.get_all_transactions()

    def get_blockchain(self):
        blockchain_li_sql = self.sql.get_blockchain()
        print("block chain: ", blockchain_li_sql)

        print(json.loads(blockchain_li_sql[0][INDEX_OF_TRANSACTIONS_ID]))
        
        blockchain = []
        id = blockchain_li_sql[0][INDEX_OF_TRANSACTIONS_ID][0]
        # creating block objects out of the sql query info
        for block in blockchain_li_sql:
            # need to create objects out of the transactions 
            #as well by getting their ids and querying them from the transaction sql table
             transaction_li = []
             transaction_ids = json.loads(block[1])
             
             for trans_id in transaction_ids: 
                sql_trans = self.get_transaction(trans_id)[0] 
                trans_to_add = Transaction(sql_trans[0], sql_trans[1], sql_trans[2], sql_trans[3])
                transaction_li.append(trans_to_add)
            
            # adding to blockchain
             block_to_add = Block(block[0], transaction_li, block[2])
             block_to_add.hash = block[3]
            
             blockchain.append( block_to_add ) 
        
        return blockchain
                

    def __repr__(self):
        return str(self)

  #  def validate_blockchain(self):
  #      block_chain = self.get_blockchain()
  #      size_of_chain = len(self.block_chain)
  #      if( size_of_chain == 1 ):
  #          return True
  #      chain_index = 1
        
  #      while(chain_index >= size_of_chain):
  #          if(self.block_chain[chain_index].prev_hash != self.block_chain[chain_index - 1].hash):
  #              return False
  #      return True








        
        