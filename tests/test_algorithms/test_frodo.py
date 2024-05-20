import unittest

from piquantum.algorithms.frodo import FRODO

class FRODOTestCase(unittest.TestCase):
    def test_encryption(self):
        frodo = FRODO()
        message = b'Hello, world!'
        ciphertext = frodo.encrypt(message)
        decrypted_message = frodo.decrypt(ciphertext)
        self.assertEqual(message, decrypted_message)

    def test_keygen(self):
        frodo = FRODO()
        public_key, private_key = frodo.keygen()
        self.assertIsInstance(public_key, tuple)
        self.assertIsInstance(private_key, tuple)
        self.assertEqual(len(public_key), 2)
        self.assertEqual(len(private_key), 2)
