from blockchain import BlockChain, Transaction, User, Mine
from blockchain import generate_genesis

if __name__ == '__main__':
    generate_genesis()

    alice = User()
    bob = User()
    caroline = User()

    print(">", alice.public_key)
    print(">", bob.public_key)
    print(">", caroline.public_key)

    transaction1 = Transaction(alice.public_key, bob.public_key, 20)
    transaction2 = Transaction(bob.public_key, caroline.public_key, 20)
    transaction3 = Transaction(caroline.public_key, alice.public_key, 20)

    user_miner = Mine(alice)

    if user_miner.mine():
        print(user_miner.last_block_completed().hash)
