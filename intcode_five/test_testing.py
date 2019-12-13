import unittest
from intcode_five.intcode_five import parse_op

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestParameterModeParsing(unittest.TestCase):
    def test_parse_op(self):
        self.assertEquals(parse_op(10299), (99, 102))
        self.assertEquals(parse_op(10201), (1, 102))
        self.assertEquals(parse_op(1002), (2, 10))
        self.assertEquals(parse_op(102), (2, 1))
        self.assertEquals(parse_op(2), (2, 0))
        self.assertEquals(parse_op(1), (1, 0))

if __name__ == '__main__':
    unittest.main()