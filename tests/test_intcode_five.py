import unittest
# from Intcode_five import *
from intcode_five import *
# from intcode_five.intcode_five import *
# from Intcode_five.intcode_five import parse_op
# from Intcode_five.intcode_five import parse_param_mode
# from Intcode_five.intcode_five import intcode
# from Intcode_five.intcode_five import init_program
# from Intcode_five.intcode_five import read_program

from io import StringIO
from unittest.mock import patch


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

        solution = 0
        for i in input_options:
            option = list(i)
            result = intcode(init_program(read_program(
                '02/input.txt'), option[0], option[1]), start_index)[0]
            if result == 19690720:
                solution = option[0] * 100 + option[1]
        self.assertEqual(solution, 7870)

    def test_day5_part1_tc1(self):
        program = [1002, 4, 3, 4, 33]
        self.assertEqual(intcode(program, 0), [1002, 4, 3, 4, 99])

    def test_day5_part1_tc2(self):
        program = [1101, 100, -1, 4, 0]
        self.assertEqual(intcode(program, 0), [1101, 100, -1, 4, 99])

    def test_day5_part1(self):
        program = read_program('intcode_five/input.txt')
        intcode(program, 0)
        # print(intcode(program, 0))

    def test_part2_tc1(self):
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode(program, 0, 8)
            intcode(program, 0, 7)
            intcode(program, 0)
            self.assertEqual(fake_out.getvalue(), '1\n0\n0\n')

    def test_part2_tc2(self):
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode(program, 0)
            intcode(program, 0, 8)
            intcode(program, 0, 7)
            intcode(program, 0, 9)
            self.assertEqual(fake_out.getvalue(), '1\n0\n1\n0\n')

    def test_part2_tc3(self):
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode(program, 0, 8)
            intcode(program, 0, 7)
            intcode(program, 0)
            self.assertEqual(fake_out.getvalue(), '1\n0\n0\n')

    def test_part2_tc4(self):
        program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode(program, 0)
            intcode(program, 0, 8)
            intcode(program, 0, 7)
            intcode(program, 0, 9)
            self.assertEqual(fake_out.getvalue(), '1\n0\n1\n0\n')

    def test_part2_jump_tc1(self):
        # program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode([3, 12, 6, 12, 15, 1, 13, 14, 13,
                     4, 13, 99, -1, 0, 1, 9], 0, 0)
            intcode([3, 12, 6, 12, 15, 1, 13, 14, 13,
                     4, 13, 99, -1, 0, 1, 9], 0, 8)
            intcode([3, 12, 6, 12, 15, 1, 13, 14, 13,
                     4, 13, 99, -1, 0, 1, 9], 0, 1)
            # intcode(program, 0, 2)
            self.assertEqual(fake_out.getvalue(), '0\n1\n1\n')

    def test_part2_jump_tc2(self):
        # program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0, 0)
            intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0, 8)
            intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0, 2)
            # intcode(program, 0, 2)
            self.assertEqual(fake_out.getvalue(), '0\n1\n1\n')

    def test_part2_larger_tc(self):
        program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode(program, 0, 0)
            intcode(program, 0, 8)
            intcode(program, 0, 9)
            # intcode(program, 0, 2)
            self.assertEqual(fake_out.getvalue(), '999\n1000\n1001\n')

    def test_day5_part2(self):
        program = read_program('intcode_five/input.txt')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            intcode(program, 0, 5)
            self.assertEqual(int(fake_out.getvalue()), 9217546)


if __name__ == '__main__':
    unittest.main()
