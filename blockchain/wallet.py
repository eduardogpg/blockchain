import Crypto
import binascii
from Crypto.PublicKey import RSA

class Wallet:
    def __init__(self):
        self.public_key = None
        self.private_key = None

        self.generate_keys()

    def generate_keys(self):
        if self.public_key is not None and self.private_key is not None:
            return False
            
        random_gen = Crypto.Random.new().read

        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()

        self.private_key = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
        self.public_key = binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')

        return {
            'private_key': self.private_key,
            'public_key' : self.public_key
        }

    def add_amount(self, amount):
        pass
