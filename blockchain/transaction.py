import datetime
import binascii

from collections import OrderedDict

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Transaction:
    def __init__(self, sender_private_key, recipient_public_key, amount):
        self.sender_private_key = sender_private_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.signature = None

    def to_hash(self):
        return OrderedDict({
            'sender_private_key': self.sender_private_key,
            'recipient_public_key': self.recipient_public_key,
            'amount': self.amount,
            'timestamp': str(self.timestamp),
        })

    def to_string(self):
        return str(self.to_hash())

    def to_encode(self):
        return self.to_string().encode('ascii')

    def __str__(self):
        return self.to_string()

    def get_secret_key(self):
        secret_key = binascii.unhexlify(self.sender_private_key)
        return RSA.importKey(secret_key)

    def sign(self):
        private_key = self.get_secret_key()
        signer = PKCS1_v1_5.new(private_key)

        sha = SHA256.new(self.to_encode())
        self.signature = signer.sign(sha)
        self.signature = binascii.hexlify(self.signature).decode('ascii')

        return self.signature

"""
Most bitcoin transactions requires a valid digital signature to be included in the blockchain,
which can only be generated with a secret key;
therefore, anyone with a copy of that key has control of the bitcoin
"""
