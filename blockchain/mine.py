from .block import Block
from .blockchain import BlockChain

class Mine:

    def __init__(self):
        self.blocks_completed = []
        self.rewards = 0

    def mine(self):
        block = Block(BlockChain.index_last_block,
                        BlockChain.transactions,
                        BlockChain.hast_last_block)

        if Block.proof_of_work(block, BlockChain):
            self.blocks_completed.append(block)
            self.rewards += BlockChain.reward

            print("Minado completo!!!")

        return block

    def last_block_completed(self):
        return self.blocks_completed[-1]
