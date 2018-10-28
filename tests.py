import unittest
import random
import string
import asteval
from myobfuscator import ob


class TestObfuscator(unittest.TestCase):
    @staticmethod
    def fill_dict(count, names):
        _dict = {}
        for i in range(count):
            name = random.choice(names)
            _dict[name] = random.randint(0, 100)
            names.remove(name)
        return _dict

    def test_accuracy(self):
        known_count = random.randint(1, 10)
        unknown_count = random.randint(1, 10)
        for i in range(1000):
            var_names = list(string.ascii_letters)
            known_vars = self.fill_dict(known_count, var_names)
            unknown_vars = self.fill_dict(unknown_count, var_names)

            aeval = asteval.Interpreter()
            aeval.symtable.update(known_vars)
            aeval.symtable.update(unknown_vars)

            value = random.randint(-1000, 1000)
            expr = ob(value, known_vars, list(unknown_vars.keys()))
            res = round(aeval(expr))

            with self.subTest(res=res, value=value, vars=known_vars, vars1=unknown_vars):
                self.assertEqual(res, value)

    def test_empty_vars(self):
        self.assertRaises(ValueError, ob, 0, {}, [])

    def test_wrong_types(self):
        with self.subTest():
            self.assertRaises(TypeError, ob, None, '', [])
            self.assertRaises(TypeError, ob, 1.25, [], {})

    def test_intersected_vars(self):
        self.assertRaises(ValueError, ob, 100, {'a': 1, 'b': 10}, ['a'])


if __name__ == '__main__':
    unittest.main()
