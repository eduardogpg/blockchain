from blockchain import BlockChain, Transaction, Wallet
from blockchain import generate_genesis

if __name__ == '__main__':
    blockchain = generate_genesis()

    alice = Wallet()
    bob = Wallet()
    caroline = Wallet()

    """
    print(">", alice.public_key + "\n")
    print(">", bob.public_key + "\n")
    print(">", caroline.public_key + "\n")
    """

    transaction1 = Transaction(alice.public_key, bob.public_key, 20)
    transaction2 = Transaction(bob.public_key, caroline.public_key, 20)
    transaction3 = Transaction(caroline.public_key, alice.public_key, 20)

    blockchain.add_transacction(transaction1)
    blockchain.add_transacction(transaction2)
    blockchain.add_transacction(transaction3)

    result = blockchain.mine()
    print(result)
