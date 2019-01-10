from .block import Block

class BlockChain:
    blocks = []
    reward = 50
    difficulty = 2
    transactions = []

    def __inint__(self):
        pass

    @classmethod
    def add_block(cls, block):

        if BlockChain.hast_last_block != block.previous_block:
            return False

        if not BlockChain.valid_block(block):
            return False

        BlockChain.blocks.append(block)

        return True

    @classmethod
    def add_transacction(cls, transaction):
        BlockChain.transactions.append(transaction)

    @classmethod
    def last_block(cls):
        return BlockChain.blocks[-1]

    @classmethod
    def hast_last_block(cls):
        return BlockChain.last_block().hash

    @classmethod
    def index_last_block(cls):
        return BlockChain.last_block().index

    @classmethod
    def valid_block(cls, block):
        return block.hash.startswith('0' * BlockChain.difficulty)

    @classmethod
    def number_of_blocks(cls):
        return len(BlockChain.blocks)

def generate_genesis():
    """
    https://www.blockchain.com/es/btc/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    https://en.bitcoin.it/wiki/Genesis_block#cite_note-block-1
    """

    block = Block(0, [], 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks')
    block.calculate_hash()

    if BlockChain.number_of_blocks() == 0:
        BlockChain.blocks.append(block)
        print(BlockChain.hast_last_block())
