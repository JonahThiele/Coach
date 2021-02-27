import CoachYacc as cyacc
from CoachYacc import yacc

while True:
    try:
        s = input('> ')
    except EOFError:
        break
    cyacc.yacc.parse(s)