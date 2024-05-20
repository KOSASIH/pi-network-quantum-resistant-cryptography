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
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_add(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_add(key2)
        self.assertEqual(key, key5)

    def test_inplace_sub(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_sub(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_sub(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_sub(key2)
        self.assertEqual(key, key5)

    def test_inplace_mul(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_mul(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_mul(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_mul(key2)
        self.assertEqual(key, key5)

    def test_inplace_truediv(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_truediv(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_truediv(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_truediv(key2)
        self.assertEqual(key, key5)

    def test_inplace_floordiv(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_floordiv(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_floordiv(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_floordiv(key2)
        self.assertEqual(key, key5)

    def test_inplace_mod(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_mod(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_mod(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_mod(key2)
        self.assertEqual(key, key5)

    def test_inplace_pow(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_pow(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_pow(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_pow(key2)
        self.assertEqual(key, key5)

    def test_inplace_lshift(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_lshift(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()key2.inplace_lshift(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_lshift(key2)
        self.assertEqual(key, key5)

    def test_inplace_rshift(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_rshift(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_rshift(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_rshift(key2)
        self.assertEqual(key, key5)

    def test_inplace_and(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_and(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_and(key)self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_and(key2)
        self.assertEqual(key, key5)

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

    def test_inplace_or(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_or(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_or(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_or(key2)
        self.assertEqual(key, key5)

    def test_inplace_eq(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_eq(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_eq(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_eq(key2)
        self.assertEqual(key, key5)

    def test_inplace_ne(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_ne(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_ne(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_ne(key2)
        self.assertEqual(key, key5)

    def test_inplace_lt(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_lt(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_lt(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_lt(key2)
        self.assertEqual(key, key5)

    def test_inplace_le(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_le(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_le(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_le(key2)
        self.assertEqual(key, key5)

    def test_inplace_gt(self):
        key = Key()
        key2 = Key()
        key3 = Key()
        key.inplace_gt(key2)
        self.assertNotEqual(key, key2)
        self.assertNotEqual(key, key3)

        key4 = key2.copy()
        key2.inplace_gt(key)
        self.assertEqual(key4, key3)

        key5 = key.copy()
        key.inplace_gt(key2)
        self.assertEqual(key, key5)
