from blockchain import BlockChain, Transaction, Wallet
from blockchain import generate_genesis

if __name__ == '__main__':
    blockchain, satoshi = generate_genesis()

    transaction1 = Transaction(satoshi.private_key, satoshi.public_key, 10, 0.80)
    transaction2 = Transaction(satoshi.private_key, satoshi.public_key, 20, 0.90)

    blockchain.add_transacction(transaction1)
    blockchain.add_transacction(transaction2)

    block = blockchain.mine()

    print("Hash : " + block.hash)
    print("Reward : " + str(block.reward))
