from uuid import uuid4

from datetime import timedelta

from .block import Block
from .transaction import Transaction

class BlockChain:

    DIFFICULTY = 4
    REWARD = 50

    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

        self.transactions = []
        self.blocks = []
        self.nodes = set()
        self.node_id = str(uuid4())

        self.register_node(self.node_id)

    def register_node(self, node_id):
        """
        Any system, such as a server, desktop application, or wallet,
        that participates in the bitcoin network by “speaking” the bitcoin protocol is called a bitcoin node.
        """
        self.nodes.add(node_id)
        return True

    def add_transacction(self, transaction):
        """
        After validating transactions, a bitcoin node will add them to the memory pool,
        or transaction pool, where transactions await until they can be included (mined) into a block.

        Once a transaction is included in a block, it has one confirmation.
        As soon as another block is mined on the same blockchain, the transaction has two confirmations, and so on.
        Six or more confirmations is considered sufficient proof that a transaction cannot be reversed.
        """
        if not self.is_valid_transaction(transaction):
            return False

        self.transactions.append(transaction)
        return True

    def add_block(self, block):
        if not self.is_valid_block(block):
            return False

        self.blocks.append(block)
        self.calculate_reward()
        self.calculate_difficulty()

        self.start_floogding()

        return True

    def start_floogding(self):
        """
        Any bitcoin node that receives a valid transaction
        it has not seen before will immediately forward it to all other nodes to which it is connected,
        a propagation technique known as flooding
        """
        pass

    def is_valid_block(self, block):
        """
        The bitcoin system of trust is based on computation.

        Transactions are bundled into blocks,
        which require an enormous amount of computation to prove, 
        but only a small amount of computation to verify as proven
        """
        if not self.is_valid_proof_of_work(block):
            return False

        if block.previous_block != self.get_hash_last_block():
            return False

        coinbase = block.transactions[0]
        if coinbase.amount != self.get_total_reward(block.transactions):
            return False

        if block.timestamp > (block.timestamp + timedelta(hours=2)):
            return False
        #218

        return True

    def is_valid_transaction(self, transaction):
        return True

    def calculate_reward(self):
        if len(self.blocks) % 210000 == 0:
            BlockChain.REWARD / 2

    def calculate_difficulty(self):
        if len(self.blocks) % 2016 == 0:


    def mine(self):
        block = self.generate_unconfirmed_block()

        if Block.proof_of_work(block, BlockChain):
            if self.add_block(block):
                return block

        return False

    def generate_unconfirmed_block(self):

        unconfirmed_transactions = self.transactions.copy()
        self.transactions.clear()

        coinbase = self.get_coinbase(unconfirmed_transactions)
        unconfirmed_transactions.insert(0, coinbase)

        block = Block(self.get_index_last_block() + 1,
                        unconfirmed_transactions,
                        self.get_hash_last_block(),
                        coinbase.amount)

        return block

    def get_total_reward(self, transactions):
        return BlockChain.REWARD + self.get_total_fees(transactions)

    def get_coinbase(self, transactions):
        """
        The first transaction in any block is a special transaction, called a coinbase transaction.
        This transaction is constructed by Jing’s node and contains his reward for the mining effort
        """
        return Transaction(self.private_key,
                            self.public_key,
                            self.get_total_reward(transactions))

    def get_total_fees(self, transactions):
        """
        Is Each miner includes a special transaction in his block
        one that pays his own bitcoin address the block reward
        plus the sum of transaction fees from all the transactions included in the block.
        """
        return sum([ transaction.fees for transaction in transactions ])

    def get_last_block(self):
        return self.blocks[-1]

    def get_hash_last_block(self):
        return self.get_last_block().hash

    def get_index_last_block(self):
        return self.get_last_block().index

    @classmethod
    def is_valid_proof_of_work(cls, block):
        return block.hash.startswith('0' * BlockChain.DIFFICULTY)

# TODO:
"""
validar firmas
implementra criterios de acpeptación
"""
