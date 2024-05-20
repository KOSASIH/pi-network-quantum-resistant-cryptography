from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from os import urandom

class NTRU:
    def __init__(self, p=65537, q=3329, d=3):
        self.p = p
        self.q = q
        self.d = d
        self.n = p * q
        self.g = self.find_polynomial(d)
        self.f = self.find_polynomial(0)
        self.df = self.invmod(self.f, self.q)
        self.fg = self.multmod(self.f, self.g, self.n)
        self.fg_inv = self.invmod(self.fg, self.n)
        self.keygen()

    def find_polynomial(self, d):
        """
        Finds a polynomial of degree d.
        """
        coefficients = [0] * self.n
        coefficients[0] = 1
        coefficients[d] = 1
        return coefficients

    @staticmethod
    def invmod(a, b):
        """
        Computes the inverse of a modulo b.
        """
        return pow(a, b - 2, b)

    @staticmethod
    def multmod(a, b, m):
        """
        Computes the product of a and b modulo m.
        """
        return sum(a[i] * b[i] for i in range(len(a))) % m

    def keygen(self):
        """
        Generates a public and private key pair.
        """
        self.private_key = (self.f, self.g)
        self.public_key = (self.h, self.f)

    def encrypt(self, message):
        """
        Encrypts a message using the public key.
        """
        r = [0] * self.n
        for i in range(self.n):
            r[i] = urandom.randint(0, self.q)
        h = self.multmod(self.public_key[0], r, self.n)
        h = self.addmod(h, self.public_key[1], self.n)
        c = self.encode_message(message)
        c = self.addmod(self.multmod(h, c, self.n), r, self.n)
        return c

    def decrypt(self, ciphertext):
        """
        Decrypts a ciphertext using the private key.
        """
        m_prime = self.multmod(self.private_key[1], ciphertext, self.n)
        m_prime = self.multmod(self.fg_inv, m_prime, self.n)
        m_prime = self.multmod(m_prime, self.df, self.n)
        return self.decode_message(m_prime)

    @staticmethod
    def encode_message(message):
        """
        Encodes a message using AES.
        """
        key = urandom.randint(0, 2 ** 128)
        cipher = AES.new(key.to_bytes(16, 'big'), AES.ENCRYPT)
        return [(cipher.encrypt(message.encode()))]

    @staticmethod
    def decode_message(ciphertext):
        """
        Decodes a message using AES.
        """
        key = urandom.randint(0, 2 ** 128)
        cipher = AES.new(key.to_bytes(16, 'big'), AES.DECRYPT)
        return cipher.decrypt(ciphertext[0]).decode()

    @staticmethod
    def addmod(a, b, m):
        """
        Adds two numbers modulo m.
        """
        return (a + b) % m
