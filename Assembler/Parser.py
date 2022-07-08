import re

A_INSTRUCTION = 'A'
C_INSTRUCTION = 'C'
L_INSTRUCTION = 'L'


class Parser:

    def __init__(self, file):
        """
        Initialize The parser Object.
            Parameters:

            fileLink: String.

            Location of the file.
        """

        self.file = file
        # Current line in file
        self.lines = file.readlines()
        self.lineNumber = -1
        self.advance()

    def hasMoreLines(self):
        """
       Checks if file has more lines or if the current line is the end

       Returns:

       more : Boolean

       True if file has more line or false if the current line is the end
       """
        if self.lineNumber < len(self.lines) - 1:
            return True
        return False

    def advance(self):
        """
        Advances the reading of the file by one line while jumping over any line that is white space
        or a comment
        """
        while self.hasMoreLines():
            self.lineNumber += 1
            if not (self.lines[self.lineNumber][0] == '/' or self.lines[self.lineNumber] == '\n'):
                break

    def instructionType(self):
        """
        Returns the type of instruction in current line

        Returns:
            A_INSTRUCTION if the instruction is of type A
            C_INSTRUCTION if the instruction is of type C
            L_INSTRUCTION if the instruction is of type L
        """
        instruction = self.lines[self.lineNumber]
        if instruction[0] == '@':
            return A_INSTRUCTION
        elif instruction[0] == '(':
            return L_INSTRUCTION
        return C_INSTRUCTION

    def symbol(self):
        """
        Returns the Symbol xxx if the instruction is of type L or A

        Returns:
            symbol : String
        """

        result = re.search('(\w+)', self.lines[self.lineNumber])
        symbol = result.group()
        return symbol

    def dest(self):
        """
        Returns the dest part of the current C-instruction

        Returns:
            dest : String
            the dest part of the current C-instruction if it exists else dest is an empty string
        """
        if '=' not in self.lines[self.lineNumber]:
            return ''
        result = re.search('\w+=', self.lines[self.lineNumber])
        dest = result.group()
        return dest[0:len(dest) - 1]

    def comp(self):
        """
        Returns the comp part of the current C-instruction

        Returns:
            comp : String
        """
        if '=' not in self.lines[self.lineNumber]:
            result = re.search('[^;]', self.lines[self.lineNumber])
            comp = result.group()
            return comp
        result = re.search('=.*', self.lines[self.lineNumber])
        comp = result.group()
        return comp[1:]

    def jump(self):
        """
        Returns the jmp part of the current C-instruction

        Returns:
            jmp : String
             the jmp part of the current C-instruction if it exists else jmp is an empty string

        """
        if ';' not in self.lines[self.lineNumber]:
            return ''
        result = re.search(';.*', self.lines[self.lineNumber])
        jmp = result.group()
        return jmp[1:].strip()

    def getLineNumber(self):
        """
        The number of the current line

        Returns:
             lineNumber: Integer
        """
        return self.lineNumber
