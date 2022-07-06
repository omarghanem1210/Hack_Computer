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
        self.line = None
        self.lineNumber = 0
        self.advance()

    def hasMoreLines(self):
        """
       Checks if file has more line or if the current line is the end

       Returns:

       more : Boolean

       True if file has more line or false if the current line is the end
       """
        raise RuntimeError('Not implemented')

    def advance(self):
        """
        Advances the reading of the file by one line while jumping over any line that is white space
        or a comment
        """
        raise RuntimeError('Not implemented')

    def instructionType(self):
        """
        Returns the type of instruction in current line

        Returns:
            A_INSTRUCTION if the instruction is of type A
            C_INSTRUCTION if the instruction is of type C
            L_INSTRUCTION if the instruction is of type L
        """
        raise RuntimeError('Not implemented')

    def symbol(self):
        """
        Returns the Symbol xxx if the instruction is of type L or A

        Returns:
            symbol : String
        """
        raise RuntimeError('Not implemented')

    def dest(self):
        """
        Returns the dest part of the current C-instruction

        Returns:
            dest : String
        """
        raise RuntimeError('Not implemented')

    def comp(self):
        """
        Returns the comp part of the current C-instruction

        Returns:
            comp : String
        """
        raise RuntimeError('Not implemented')

    def jump(self):
        """
        Returns the jmp part of the current C-instruction

        Returns:
            jmp : String
        """
        raise RuntimeError('Not implemented')

    def getLineNumber(self):
        """
        The number of the current line

        Returns:
             lineNumber: Integer
        """
        return self.lineNumber
