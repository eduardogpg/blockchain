from .block import Block
from .blockchain import BlockChain
from .wallet import Wallet

def generate_genesis():
    """
    https://www.blockchain.com/es/btc/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    https://en.bitcoin.it/wiki/Genesis_block#cite_note-block-1
    """
    satoshi = Wallet()
    blockchain = BlockChain(satoshi)

    block = Block(0, [],
                    'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',
                    BlockChain.reward)

    block.calculate_hash()
    blockchain.blocks.append(block)
    
    return blockchain
