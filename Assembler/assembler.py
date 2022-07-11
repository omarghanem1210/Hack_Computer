from Code import *
from Parser import *
from numpy import binary_repr

import sys

file = ''

try:
    file = sys.argv[1]
except FileNotFoundError:
    print('File not found in that directory')
    sys.exit(1)
file1 = open(file, 'r')
parser = Parser(file1)

symbol_table = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
                'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
rom = 0
while True:
    if parser.instructionType() == L_INSTRUCTION:
        if symbol_table.get(parser.symbol()) == None:
            symbol_table[parser.symbol()] = rom

    if parser.instructionType() == A_INSTRUCTION or parser.instructionType() == C_INSTRUCTION:
        rom +=1
    parser.advance()
    if parser.getLineNumber() == parser.getTotalLines():
        break
file1.close()

file1 = open(file, 'r')
parser = Parser(file1)
output = open(file.replace('asm', 'hack'), 'w')
ram = 16
while True:
    if parser.instructionType() == C_INSTRUCTION:
        s1 = dest(parser.dest())
        s2 = comp(parser.comp())
        s3 = jump(parser.jump())
        output.write('111' + s2 + s1 + s3 + '\n')
    elif parser.instructionType() == A_INSTRUCTION:
        if not parser.symbol().isdigit():
            if symbol_table.get(parser.symbol()) == None:
                symbol_table[parser.symbol()] = ram
                output.write(binary_repr((symbol_table[parser.symbol()]), 16) + '\n')
                ram +=1
            else:
                output.write(binary_repr((symbol_table[parser.symbol()]), 16) + '\n')
        else:
            s1 = binary_repr(int(parser.symbol()), 16)
            output.write(s1 + '\n')
    if parser.getLineNumber() == parser.getTotalLines():
        break
    parser.advance()

file1.close()
output.close()
