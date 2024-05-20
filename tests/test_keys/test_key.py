import unittest

from piquantum.keys import Key

class TestKey(unittest.TestCase):
    def test_init(self):
        key = Key()
        self.assertIsInstance(key, Key)

    def test_to_bytes(self):
        key = Key()
        key_bytes = key.to_bytes()
        self.assertIsInstance(key_bytes, bytes)

    def test_from_bytes(self):
        key = Key()
        key_bytes = key.to_bytes()
        key2 = Key.from_bytes(key_bytes)
        self.assertEqual(key, key2)

    def test_repr(self):
        key = Key()
        repr_str = repr(key)
        self.assertIsInstance(repr_str, str)

    def test_str(self):
        key = Key()
        str_str = str(key)
        self.assertIsInstance(str_str, str)

    def test_copy(self):
        key = Key()
        key2 = key.copy()
        self.assertEqual(key, key2)

    def test_equal(self):
        key = Key()
        key2 = Key()
        self.assertEqual(key, key2)

        key3 = Key()
        self.assertNotEqual(key, key3)

        key4 = 123
        self.assertNotEqual(key, key4)

    def test_hash(self):
        key = Key()
        hash_val = hash(key)
        self.assertIsInstance(hash_val, int)

    def test_xor(self):
        key = Key()
        key2 = Key()
        key3 = key ^ key2
        self.assertNotEqual(key, key3)
        self.assertNotEqual(key2, key3)

        key4 = key ^ key3
        self.assertEqual(key, key4)

        key5 = key2 ^ key3
        self.assertEqual(key2, key5)

    def test_inplace_xor(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_xor(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_xor(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_xor(key2)
        self.assertEqual(key, key5)

    def test_inplace_add(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_add(key2)
        self.assertNotEqual(
