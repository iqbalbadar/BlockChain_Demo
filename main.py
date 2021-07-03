from BlockChain import *

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