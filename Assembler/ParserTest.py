import unittest
from Parser import Parser

fileLink = 'Test.asm'


class ParserTest(unittest.TestCase):

    def testAdvance(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        self.assertEqual(8, parser.getLineNumber())
        parser.advance()
        self.assertEqual(9, parser.getLineNumber())

        file.close()

    def testHasMoreLines(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        self.assertTrue(parser.hasMoreLines())
        for i in range(0, 10):
            parser.advance()
        self.assertTrue(parser.hasMoreLines())
        for i in range(0, 50):
            parser.advance()
        self.assertFalse(parser.hasMoreLines())

        file.close()

    def testInstructionType(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        self.assertEqual('A', parser.instructionType())
        parser.advance()
        self.assertEqual('C', parser.instructionType())
        parser.advance()
        self.assertEqual('A', parser.instructionType())
        parser.advance()
        parser.advance()
        self.assertEqual('L', parser.instructionType())

        file.close()

    def testSymbol(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        self.assertEqual('i', parser.symbol())
        parser.advance()
        parser.advance()
        self.assertEqual('product', parser.symbol())
        parser.advance()
        parser.advance()
        self.assertEqual('LOOP', parser.symbol())

        file.close()

    def testComp(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        parser.advance()
        self.assertEqual('1', parser.comp())
        parser.advance()
        parser.advance()
        self.assertEqual('0', parser.comp())
        parser.advance()
        parser.advance()
        parser.advance()
        parser.advance()
        parser.advance()
        self.assertEqual('D-M', parser.comp())
        parser.advance()
        parser.advance()
        self.assertEqual('D', parser.comp())


        file.close()

    def testDest(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        parser.advance()
        self.assertEqual('M', parser.dest())
        parser.advance()
        parser.advance()
        self.assertEqual('M', parser.dest())
        parser.advance()
        parser.advance()
        parser.advance()
        parser.advance()
        parser.advance()
        self.assertEqual('D', parser.dest())
        parser.advance()
        parser.advance()
        self.assertEqual('null', parser.dest())

        file.close()

    def testJump(self):
        file = open(fileLink, 'r')
        parser = Parser(file)

        for i in range(10):
            parser.advance()
        self.assertEqual('JGT', parser.jump())

        for i in range(9):
            parser.advance()
        self.assertEqual('JMP', parser.jump())

        file.close()


if __name__ == '__main__':
    unittest.main()
