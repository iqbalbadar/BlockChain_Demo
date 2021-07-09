from BlockChain import *
from Transaction import *

def main():


    transaction_1 = Transaction("iqbal", "her", 11.56, 1)
    transaction_2 = Transaction("her", "iqbal", 12.56 ,2)
    transaction_3 = Transaction(" girl", "iqbal", 33.56, 3)
    transaction_4 = Transaction("iqbal", "girl", 55.6, 4)

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

    chain.insert_blockchain_sql()
   

if __name__ == "__main__":
    main()