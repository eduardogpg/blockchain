from uuid import uuid4
from .block import Block
from urllib.parse import urlparse

class BlockChain:

    difficulty = 4
    reward = 2

    def __init__(self, user):
        self.transactions = [] #unverified
        self.blocks = []
        self.nodes = set() #One machine, one vote
        self.user = user
        self.node_id = str(uuid4())

    def register_node(self, node):
        self.nodes.append(node)
        return True

    def add_transacction(self, transaction):
        #Es necesario validar la transacció para evitar el doble spend
        #El orden depende de los fees

        self.transactions.append(transaction)
        return True

    def add_block(self, block):

        if self.hash_last_block() != block.previous_block:
            return False

        if not BlockChain.is_valid_block(block):
            return False

        self.blocks.append(block)

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
        self.transactions.clear()

        if Block.proof_of_work(block, BlockChain):
            if self.add_block(block):
                return block

        return False

    def generate_block(self):
        #Cuandoa alguien encuentra un bloque todos los nodos dejan de trabajar
        #y se concentran en lo que sigue

        """
        Is Each miner includes a special transaction in his block
        one that pays his own bitcoin address the block reward
        plus the sum of transaction fees from all the transactions included in the block.
        """

        """
        The first transaction in any block is a special transaction, called a coinbase transac‐ tion. This transaction is constructed by Jing’s node and contains his reward for the mining effort
        """
        self.add_coinbase()

        return Block( self.index_last_block() + 1,
                      self.transactions.copy(),
                      self.hash_last_block(),
                      BlockChain.reward)

    def add_coinbase(self):
        transaction = Transaction('sender_address', 'sender_private_key', 'recipient_address', BlockChain.reward)
        self.transactions.insert(transaction, 0)

    def last_block(self):
        return self.blocks[-1]

    def hash_last_block(self):
        return self.last_block().hash

    def index_last_block(self):
        return self.last_block().index

    @classmethod
    def is_valid_block(cls, block):
        return block.hash.startswith('0' * BlockChain.difficulty)



# TODO:
"""
Firmas
validar firmas
Cada x recalcular
Agregar el coinbase a cada bloque.
Aplicar la prueba de trabajo
implementra criterios de acpeptación
"""
