from .block import Block
from .blockchain import BlockChain
from .wallet import Wallet

def generate_genesis():
    """
    A genesis block is the first block of a block chain.
    The hash of the genesis block, 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    """
    
    satoshi = Wallet()
    blockchain = BlockChain(satoshi.private_key, satoshi.public_key)

    block = Block(0, [],
                    'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',
                    BlockChain.REWARD)

    block.calculate_hash()
    blockchain.blocks.append(block)

    return blockchain, satoshi
