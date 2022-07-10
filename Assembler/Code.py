dest_codes = {'null': '000', 'M': '001', 'D': '010', 'DM': '011', 'A': '100', 'AM': '101',
              'AD': '110', 'ADM': '111'}

comp_codes = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', '!D': '0001101',
              '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111',
              'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111',
              'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011',
              'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
              'D&M': '1000000', 'D|M': '1010101'}

jump_codes = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110',
              'JMP': '111'}


def dest(s):
    """

    param s: A string symbolising a dest command


    return:A string consisting of 1s and 0s representing the binary code of a dest part

    """
    return dest_codes[s]


def comp(s):
    """

    param s:A string symbolising a comp command


    return:A string consisting of 1s and 0s representing the binary code of a comp part
    """
    return comp_codes[s]


def jump(s):
    """

    param s: A string symbolising a jump command


    return:A string consisting of 1s and 0s representing the binary code of a jump part
    """
    return jump_codes[s]
