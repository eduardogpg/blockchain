from blockchain import BlockChain, Transaction, Wallet
from blockchain import generate_genesis

if __name__ == '__main__':
    blockchain = generate_genesis()

    alice = Wallet()
    print(alice.to_string())
