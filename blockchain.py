import hashlib
import datetime
import json
import sys
from Block import * 
from Transaction import * 
import sqlite3


BLOCKCHAIN_REWARD_FACTOR = 210000
INDEX_OF_AMOUNT = 2
INDEX_OF_TRANSACTIONS = 3
INDEX_OF_SENDER = 0
INDEX_OF_RECIPENT = 1


class BlockChain:
    def __init__(self, proof_of_work_diff=3):
        self.conn_chain = self.get_chain_db()
        self.conn_trans = self.get_transactions_db()
        self.sql_chain = self.conn_chain.cursor()
        self.sql_trans = self.conn_trans.cursor()


        self.curr_trans_count = self.get_num_trans()
        self.proof_of_work_diff = proof_of_work_diff
        self.pending_transactions = []
        self.block_chain = self.get_chain()
        self.reward = BLOCKCHAIN_REWARD_FACTOR / len(self.block_chain)



    def get_chain_db(self):
        conn_chain = sqlite3.connect('BlockChain.db')
        conn_chain.execute("""CREATE TABLE IF NOT EXISTS BlockChain  (
            prev_hash text,
            transaction_ids text,
            timestamp text,
            hash text
            )""")
        return conn_chain
            
    def get_num_trans(self):
        return self.sql_trans.execute("SELECT COUNT(*) FROM Transactions")
    
    def get_transactions_db(self):
        conn_trans = sqlite3.connect('Transactions.db')
        conn_trans.execute("""CREATE TABLE IF NOT EXISTS Transactions  (
            from_person text,
            to_person text,
            amount float,
            id int
            )""")
        return conn_trans

    def get_chain(self):
        print("getting chain")
        with self.conn_chain:
            self.sql_chain.execute("SELECT * FROM BlockChain")
            blockchain_list_sql = self.sql_chain.fetchall()

        # if the database is empty create a new blockchain
        if (len(blockchain_list_sql) == 0): 
            return [self.create_first_block()]
        else:
            # create block objects for all the blocks in the sql table
            # get the transaction ids and make objects out of those as well
            for block in blockchain_list_sql:
                print(block)
                transaction_ids = json.loads(block[1])
                print(transaction_ids)
                for id in transaction_ids:
                    print(id)
                    transaction = self.conn_trans.execute("SELECT * FROM Transactions WHERE id=:id", {'id':id}).fetchall()
                    print("transaction!: ",transaction)
                    transaction = Transaction(transaction[INDEX_OF_SENDER] ,transaction[INDEX_OF_RECIPENT], Transaction[INDEX_OF_AMOUNT], Transaction[INDEX_OF_TRANSACTIONS])
                    print(transaction)


    def insert_blockchain_sql(self):
        for block in self.block_chain:
            print(block)
            li_of_ids = []
            for transaction in block.transactions:
                li_of_ids.append(transaction.id)
                with self.conn_trans:
                    self.sql_trans.execute("INSERT into Transactions VALUES (?, ?, ?, ?)", transaction.from_person, transaction.to_person, transaction.amount, transaction.id)
            print(li_of_ids)
            with self.conn_chain:
                self.sql_chain.execute("INSERT into BlockChain VALUES (?, ?, ?, ?)", (block.prev_hash, str(li_of_ids), block.timestamp, block.hash) )
                

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def create_first_block(self):
        first_transaction = Transaction("","",0,0)
        return Block("", [first_transaction], datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def mine(self, miner_name, transaction_id):
        transaction_for_miner = Transaction("Iqbal_Coin", miner_name, self.reward, transaction_id)
        self.pending_transactions.append(transaction_for_miner)
        #print(self.block_chain)

        prev_hash = self.block_chain[-1].hash
        block_to_mine = Block(prev_hash, self.pending_transactions, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        #print(block_to_mine)

        if(block_to_mine.mine_block(self.proof_of_work_diff)):
            print("Block is mined, moving to the chain!")
            self.block_chain.append(block_to_mine)
            self.reward = reward = BLOCKCHAIN_REWARD_FACTOR / len(self.block_chain)
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








        
        