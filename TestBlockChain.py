import unittest



class TestBlockChain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def tearDown(self):
        print('tearDown\n')

    def setUp(self):
        print('setUp')
        self.blockchain1 = BlockChain()
        self.blockchain2 = BlockChain(4)
    
    def test_pending_transactions():
        self.blockchain1 = BlockChain()
        self.blockchain2 = BlockChain(4)
        self.blockchain1.add_transaction("Iqbal", "Random Dude", 33.56)
        self.blockchain1.add_transaction("liz", "bro", 60.00)
        self.blockchain1.add_transaction("dude", "bro", 50.00)

        transaction_1 = self.blockchain1.pending_transactions[0]
        transaction_2 = self.blockchain1.pending_transactions[1]
        transaction_3 = self.blockchain1.pending_transactions[2]

        self.assertEqual(transaction_1.from_person, 'Iqbal')
        self.assertEqual(transaction_2.to_person, 'bro')
        self.assertEqual(transaction_3.amount, 50.00)
        self.assertEqual(transaction_2.id, 2)

        self.assertEqual(1,2)

    if __name__ == '__main__':
        unittest.main()
        TestBlockChain.test_pending_transactions()






        

    
    
# what to test:
# 