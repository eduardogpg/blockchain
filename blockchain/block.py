import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, transactions, previous_block):
        self.index = index
        self.transactions = transactions
        self.timestamp = datetime.now
        self.previous_block = previous_block
        self.nonce = 0

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(self.to_string())

        self.hash = sha.hexdigest()

        return self.hash

    def transactions_to_hash(self):
        return [ transaction.to_hash() for transaction in self.transactions]

    def to_hash(self):
        """
            Do not user __dict__ attr. Is necesary execute transactions_to_hash method.
        """

        return {
            'index': self.index,
            'transactions': self.transactions_to_hash(),
            'timestamp': str(self.timestamp),
            'previous_block': self.previous_block,
            'nonce': str(self.nonce)
        }

    def to_string(self):
        return str(self.to_hash()).encode()

    def increment_nonce(self):
        self.nonce += 1

    def __str__(self):
        return self.to_string()

    @classmethod
    def proof_of_work(cls, block, blockchain):
        block.nonce = 0

        hash = block.calculate_hash()

        while not blockchain.valid_block(block):

            block.increment_nonce()
            block.calculate_hash()

            print(block.hash)

        return block
