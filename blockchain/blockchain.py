from .block import Block

class BlockChain:

    difficulty = 2
    reward = 2

    def __init__(self, user):
        self.transactions = []
        self.blocks = []
        self.user = user

    def set_user(self, user):
        self.user = user

    def add_transacction(self, transaction):
        self.transactions.append(transaction)
        return True

    def add_block(self, block):

        if self.hash_last_block() != block.previous_block:
            return False

        if not BlockChain.is_valid_block(block):
            return False

        self.blocks.append(block)
        self.transactions.clear()

        self.calculate_reward()
        self.calculate_difficulty()

        return True

    def calculate_reward(self):
        pass

    def calculate_difficulty(self):
        pass

    def mine(self):
        if not self.transactions:
            return False

        block = self.generate_block()

        if Block.proof_of_work(block, BlockChain):
            if self.add_block(block):
                return block

        return False

    def generate_block(self):
        return Block( self.index_last_block() + 1,
                      self.transactions.copy(),
                      self.hash_last_block(),
                      self.user.public_key,
                      BlockChain.reward)

    @classmethod
    def check_blocks_validity(cls, chain):
        pass

    @classmethod
    def is_valid_block(cls, block):
        return block.hash.startswith('0' * BlockChain.difficulty)

    def last_block(self):
        return self.blocks[-1]

    def hash_last_block(self):
        return self.last_block().hash

    def index_last_block(self):
        return self.last_block().index
