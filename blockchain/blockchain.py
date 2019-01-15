from .block import Block

#registrar nodo
#verificar transacción
#submit transacción
#Crear bloque
#hash
#prueba de trabajo
#validar prueba de trabajo
#validar cadena de bloque
#resolver conflicto

class BlockChain:
    blocks = []
    reward = 50
    difficulty = 4
    transactions = []
    nodes = set()

    def __init__(self):
        pass

    @classmethod
    def add_block(cls, block):

        if BlockChain.hast_last_block != block.previous_block:
            return False

        if not BlockChain.valid_block(block):
            return False

        BlockChain.blocks.append(block)

        BlockChain.transactions.clear()

        BlockChain.calculate_reward()
        BlockChain.calculate_difficulty()

        return True

    @classmethod
    def calculate_reward(cls):
        pass

    @classmethod
    def calculate_difficulty(cls):
        pass

    @classmethod
    def add_transacction(cls, transaction):
        BlockChain.transactions.append(transaction)

    @classmethod
    def last_block(cls):
        return BlockChain.blocks[-1]

    @classmethod
    def hash_last_block(cls):
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
