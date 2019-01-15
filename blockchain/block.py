import hashlib
import datetime

class Block:
    def __init__(self, index, transactions, previous_block, solved_by, reward):
        self.index = index
        self.transactions = transactions
        self.number_transactions = len(self.transactions)
        self.timestamp = datetime.datetime.now()
        self.previous_block = previous_block
        self.solved_by = solved_by
        self.reward = reward
        self.nonce = 0

    def increment_nonce(self):
        self.nonce += 1

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(self.to_encode())

        self.hash = sha.hexdigest()

        return self.hash

    def transactions_to_hash(self):
        return [transaction.to_hash() for transaction in self.transactions]

    def to_hash(self):
        return {
            'index': self.index,
            'transactions': self.transactions_to_hash(),
            'number_transactions' : str(self.number_transactions),
            'timestamp': str(self.timestamp),
            'previous_block': self.previous_block,
            'solved_by': self.solved_by,
            'reward': self.reward,
            'nonce': str(self.nonce)
        }

    def to_string(self):
        return str(self.to_hash())

    def to_encode(self):
        return self.to_string().encode()

    def __str__(self):
        return self.to_string()

    @classmethod
    def proof_of_work(cls, block, blockchain):

        block.nonce = 0

        hash = block.calculate_hash()

        while not blockchain.is_valid_block(block):
            block.calculate_hash()
            block.increment_nonce()

        return block
