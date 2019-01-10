from blockchain import BlockChain, Transaction, Mine
from blockchain import generate_genesis

if __name__ == '__main__':
    generate_genesis()

    transaction1 = Transaction('Alice', 'Bob', 25)
    transaction2 = Transaction('Bob', 'Caroline', 10)

    BlockChain.add_transacction(transaction1)
    BlockChain.add_transacction(transaction2)

    miner = Mine()
    if miner.mine():
        print(miner.last_block_completed())
