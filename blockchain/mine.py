from .block import Block
from .blockchain import BlockChain

class Mine:

    def __init__(self, user):
        self.blocks_completed = []
        self.user = user

    def mine(self):

        block = self.new_block()

        if Block.proof_of_work(block, BlockChain):
            self.blocks_completed.append(block)
            self.user.add_amount(block.reward)

        return block
        
    def new_block(self):
        return Block(BlockChain.index_last_block() + 1,
                        BlockChain.transactions,
                        BlockChain.hash_last_block(),
                        self.user.public_key,
                        BlockChain.reward)

    def last_block_completed(self):
        return self.blocks_completed[-1]
