import Crypto
import binascii

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from collections import OrderedDict

BITS = 1024

class Wallet:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.address = None

        self.generate_keys()
        self.generate_address()

    def generate_address(self):
        """
        A address is a string of digits and characters that can be shared
        with anyone who wants to send you money.

        In order to generate an address is necesarry a double Hash or HASH160
        """
        address = SHA256.new(self.public_key.encode('ascii'))
        self.address = address.hexdigest()

        return self.address

    def generate_keys(self):
        """
        A bitcoin wallet contains a collection of key pairs,
        each consisting of a private key and a public key.

        The private key (k) is a number, usually picked at random.
        From the private key, we use elliptic curve multiplication, a one-way cryptographic function, to generate a public key (K).
        From the public key (K), we use a one-way cryptographic hash function to generate a bitcoin address (A)
        """
        random_generator = Crypto.Random.new().read

        private_key = RSA.generate(BITS, random_generator)
        public_key = private_key.publickey()

        private_key = private_key.exportKey(format='DER')
        public_key = public_key.exportKey(format='DER')

        self.private_key = binascii.hexlify(private_key).decode('ascii')
        self.public_key = binascii.hexlify(public_key).decode('ascii')

        return self.to_hash()

    def to_hash(self):
        return OrderedDict({
            'private_key': self.private_key,
            'public_key' : self.public_key,
            'address': self.address
        })

    def to_string(self):
        return str(self.to_hash())

    def to_encode(self):
        return self.to_string().encode('utf8')

    def __str__(self):
        return self.to_string()
