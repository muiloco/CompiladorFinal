from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def addTokens(self):
        self.lexer.add('NUMBER', r'^((-?)(\d+)((\.\d+)?))')
        self.lexer.add('EQUAL', r'^(==)')
        self.lexer.add('LESSEQUAL', r'^(<=)')
        self.lexer.add('GREATEREQUAL', r'^(>=)')
        self.lexer.add('DIFFERENT', r'^(!=)')
        self.lexer.add('OPR_LOG', 'not')
        self.lexer.add('OPR_LOG', 'or')
        self.lexer.add('OPR_LOG', 'and')
        self.lexer.add('IF', 'if')
        self.lexer.add('ELSE', 'else')
        self.lexer.add('WHILE', 'while')
        self.lexer.add('LEIA', 'leia')
        self.lexer.add('ESCREVA', 'escreva')
        self.lexer.add('ID', r'^([a-zA-Z]([a-zA-Z]|\d)*)')
        self.lexer.add('GRE', '>')
        self.lexer.add('LES', '<')
        self.lexer.add('ATRIB', '=')
        self.lexer.add('COM', ',')
        self.lexer.add('SEM', ';')
        self.lexer.add('ADD', r'^(\+)')
        self.lexer.add('SUB', r'^(\-)')
        self.lexer.add('MUL', r'^(\*)')
        self.lexer.add('POW', r'(\^)')
        self.lexer.add('DIV', '/')
        self.lexer.add('MOD', '%')
        self.lexer.add('LPA', r'^(\()')
        self.lexer.add('RPA', r'^(\))')
        self.lexer.add('DOT', '.')

        self.lexer.ignore('\s+')
        
    def getLexer(self):
        self.addTokens()
        return self.lexer.build()