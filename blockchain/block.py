import datetime

from Crypto.Hash import SHA256

from collections import OrderedDict

class Block:
    def __init__(self, index, transactions, previous_block, reward):
        self.index = index
        self.transactions = transactions
        self.number_transactions = len(self.transactions)
        self.timestamp = datetime.datetime.now()
        self.previous_block = previous_block
        self.reward = reward
        self.nonce = 0

    def increment_nonce(self):
        self.nonce += 1

    def calculate_hash(self):
        sha = SHA256.new(self.to_encode())

        self.hash = sha.hexdigest()

        return self.hash

    def transactions_to_hash(self):
        return [transaction.to_hash() for transaction in self.transactions]

    def to_hash(self):
        return OrderedDict({
            'index': self.index,
            'transactions': self.transactions_to_hash(),
            'number_transactions' : str(self.number_transactions),
            'timestamp': str(self.timestamp),
            'previous_block': self.previous_block,
            'reward': self.reward,
            'nonce': str(self.nonce)
        })

    def to_string(self):
        return str(self.to_hash())

    def to_encode(self):
        return self.to_string().encode('ascii')

    def __str__(self):
        return self.to_string()

    @classmethod
    def proof_of_work(cls, block, blockchain):

        hash = block.calculate_hash()

        while not blockchain.is_valid_proof_of_work(block):
            block.calculate_hash()
            block.increment_nonce()

        return block
