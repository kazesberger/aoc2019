import unittest
from intcode_five.intcode_five import parse_op
from intcode_five.intcode_five import parse_param_mode
from intcode_five.intcode_five import intcode
from intcode_five.intcode_five import init_program
from intcode_five.intcode_five import program

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
        self.assertEqual(parse_op(10299), (99, 102))
        self.assertEqual(parse_op(10201), (1, 102))
        self.assertEqual(parse_op(1002), (2, 10))
        self.assertEqual(parse_op(102), (2, 1))
        self.assertEqual(parse_op(2), (2, 0))
        self.assertEqual(parse_op(1), (1, 0))

    def test_parse_modes(self):
        self.assertEqual(parse_param_mode(123, 0), 3)
        self.assertEqual(parse_param_mode(123, 1), 2)
        self.assertEqual(parse_param_mode(123, 2), 1)

    def test_day2_part2(self):
        start_index = 0
        input_options = set()

        for x in range(99):
            for y in range(99):
                input_options.add((x, y))

        for i in input_options:
            option = list(i)
            result = intcode(init_program(program, option[0], option[1]), start_index)[0]
            if result == 19690720:
                solution = option[0] * 100 + option[1]
                self.assertEqual(solution, 7870)


if __name__ == '__main__':
    unittest.main()