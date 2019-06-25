from lexer import Lexer

text = open('teste.txt','r').read()
x = str(text).split()
for strsplit in x:
    lexer = Lexer().getLexer()
    tokens = lexer.lex(strsplit)
    for token in tokens:
        print(token)