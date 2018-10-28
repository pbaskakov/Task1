import sys
from myobfuscator import ob
from random import randint
import asteval


if __name__ == '__main__':
    expected_value = int(input('Enter the expected value (int): '))
    known_vars = (rec.split('=') for rec in
                  input('Enter the known vars and their values(like "a=100, b=200"): ').split(','))
    known_vars = {name.strip(): float(val.strip()) for name, val in known_vars}
    unknown_vars = {name.strip(): randint(0, 100) for name in
                    input('Enter the unknown vars (like "x, y, z"): ').split(',')}

    if not set(known_vars.keys()).isdisjoint(set(unknown_vars)):
        sys.exit("Sets of known adn unknown vars can't be intersected.")

    obfuscated = ob(expected_value, known_vars, list(unknown_vars.keys()))

    aeval = asteval.Interpreter()
    aeval.symtable.update(known_vars)
    aeval.symtable.update(unknown_vars)

    print('\nObfuscated expression:', obfuscated)
    print('Value of this expression:', int(round(aeval(obfuscated))))
