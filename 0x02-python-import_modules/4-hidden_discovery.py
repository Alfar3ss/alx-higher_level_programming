#!/usr/bin/python3

import dis
import types

def print_hidden_names():
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()
    module = types.ModuleType('hidden_4')
    exec(code, module.__dict__)
    
    names = [name for name in dir(module) if not name.startswith('__')]
    names.sort()
    
    for name in names:
        print(name)

if __name__ == "__main__":
    print_hidden_names()
