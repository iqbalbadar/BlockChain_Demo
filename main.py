from BlockChain import *
from Transaction import *
import argparse
import sys 
import os


FLAG_INDEX = 1


def restart_blockchain():
    if (os.path.exists("Transactions.db")):
        os.remove("Transactions.db")

    if (os.path.exists("BlockChain.db")):
        os.remove("BlockChain.db")

def create_transaction(blockchain):

    keep_creating_transactions = True

    while(keep_creating_transactions):
        from_person = raw_input("From Person: ")
        to_person = raw_input("To Person: ")
        amount = float(raw_input("Amount: "))

        blockchain.add_transaction(from_person, to_person, amount)

        keep_creating_transactions = raw_input("More transactions? (y \ n): ")

        if(keep_creating_transactions == 'n'):
            keep_creating_transactions = False

    make_block = raw_input("Make a Block? (y \ n): ")
    if(make_block == 'y'):
        create_block(blockchain)

def print_block(blockchain):
    print(blockchain.get_blockchain())
        

def create_block(blockchain):
    miner_to_mine = raw_input("Name of the miner to mine: ")
    blockchain.mine(miner_to_mine)
    
    print("creating block")

def help():
    print("You need one of the following flags to use the blockchain:\n-t: you want to make a transaction, -b: you want to add a new block'\n-h: print this message again\n-r: erase the current blockchain and start new ")


def main():

    # creating blockchain
    block = BlockChain(3)

    if(len(sys.argv) <= 1):
        print("You need one of the following flags to use the blockchain:\n-t: you want to make a transaction, -b: you want to add a new block'\n-h: print this message again\n-r: erase the current blockchain and start new ")


    # map the inputs to the function blocks
    options = {'-t' : create_transaction,
            '-b' : create_block,
            '-r' : restart_blockchain,  
            '-h' : help, 
            '-v' : print_block
    }

    if(sys.argv[FLAG_INDEX] not in options.keys()):
        help()
    
    option_chosen = sys.argv[FLAG_INDEX]

    if(option_chosen == '-t' or option_chosen == '-b' or option_chosen == '-v'):
        options[option_chosen](block)
    else:
        options[option_chosen]()

    if(sys.argv[FLAG_INDEX] not in options.keys()):
        print("You need to enter in a correct flag")
    

    # what should a user be able to do??? 
    # 1. Mine a block => print hash
    # 2. create a transaction 
    # 3. start new blockchain if blockchain.db is not there
    # 4. verify blockchain 
    # 5. Put in proof of work difficultity 

 
   
if __name__ == "__main__":
    main()