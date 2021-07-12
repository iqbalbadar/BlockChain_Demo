import sqlite3
from Block import *
from Transaction import * 

class SqlWrapper:
    def __init__(self):
        self.conn_chain = self.get_chain_db()
        print("HELLO")
        self.conn_trans = self.get_transactions_db()
        self.sql_chain = self.conn_chain.cursor()
        self.sql_trans = self.conn_trans.cursor()

    def get_chain_db(self):
        conn_chain = sqlite3.connect('BlockChain.db')
        print("connecting to blockchain db")
        conn_chain.execute("""CREATE TABLE IF NOT EXISTS BlockChain  (
            prev_hash text,
            transaction_ids text,
            timestamp text,
            hash text
            )""")
        return conn_chain

    def get_transactions_db(self):
        conn_trans = sqlite3.connect('Transactions.db')
        print("connecting to transactions db")

        conn_trans.execute("""CREATE TABLE IF NOT EXISTS Transactions  (
            from_person text,
            to_person text,
            amount float,
            id int,
            processed int
            )""")
        return conn_trans
    
    def get_blockchain_length(self):
        with self.conn_chain:
            return self.sql_chain.execute("SELECT COUNT(*) FROM BlockChain").fetchone()[0]

    def get_num_trans(self):
        with self.conn_trans:
            return self.conn_trans.execute("SELECT COUNT(*) FROM Transactions").fetchone()[0]

    def insert_into_blockchain_table(self, block_to_be_inserted):
        transaction_ids = []

        # insert the transactions into sql as well before the block itself
        for transaction in block_to_be_inserted.transactions:
            print(transaction)
            self.insert_into_transaction_table(transaction)
            transaction_ids.append(transaction.id)

        with self.conn_chain:
            self.sql_chain.execute("INSERT into BlockChain VALUES (?, ?, ?, ?)", (block_to_be_inserted.prev_hash, str(transaction_ids), block_to_be_inserted.timestamp, block_to_be_inserted.hash) )

    def get_prev_hash(self):
        with self.conn_trans:
            prev_hash = self.sql_chain.execute("SELECT prev_hash FROM BlockChain ORDER BY prev_hash DESC LIMIT 1").fetchone()[0]
            print("prev hash: ", prev_hash)
            return prev_hash


    def get_pending_transactions(self):
        with self.conn_trans:
            if(self.get_num_trans() == 0):
                return []
            transaction_li = self.sql_trans.execute("SELECT from_person, to_person, amount, id  FROM Transactions WHERE processed=:processed", {'processed':0}).fetchall() 
            return transaction_li

    def get_blockchain(self):
        with self.conn_trans:
            blockchain_li = self.blockchain.execute("SELECT * FROM BlockChain").fetchall()
            return blockchain_li
                
    def get_num_trans(self):
        return self.sql_trans.execute("SELECT COUNT(*) FROM Transactions").fetchone()[0]

    def insert_into_transaction_table(self, processed_transaction):
        with self.conn_trans:
            self.sql_trans.execute("INSERT into Transactions VALUES (:from_person, :to_person, :amount, :id, :processed)", {'from_person': processed_transaction.from_person, 'to_person': processed_transaction.to_person, 'amount': processed_transaction.amount, 'id': processed_transaction.id, 'processed': 1})

    def insert_pending_transactions(self, unprocessed_transactions):
        print("putting in unprocessed transactions!!!")
        with self.conn_trans:
            for unprocessed_transaction in unprocessed_transactions:
                print("unprocessed Transaction: ", unprocessed_transaction)
                self.sql_trans.execute("INSERT into Transactions VALUES (?, ?, ?, ?, ?)", unprocessed_transaction.from_person, unprocessed_transaction.to_person, unprocessed_transaction.amount, unprocessed_transaction.id, 0)
