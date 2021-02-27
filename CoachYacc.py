import ply.yacc 
from CoachLex import tokens

#enviromental variables
enviro_vars = {}

def p_statement_assign(p):
    'statement : VAR expression'
    enviro_vars[p[1]] = p[2]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_statement_output(p):
    'statement : OUTPUT expression'
    print("Coach says" + str(p[2]) + "!")    
    
def p_expression_basicop(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MULT expression
                  | expression DIV expression'''
    if p[2] == 'number to go'  : p[0] = p[1] + p[3]
    elif p[2] == 'completed out of': p[0] = p[3] - p[1]
    elif p[2] == 'by': p[0] = p[1] * p[3]
    elif p[2] == 'split': p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_var(p):
    'expression : VAR'
    try:
        p[0] = enviro_vars[p[1]]
    except LookupError:
        print("undefined var, resorting to 0")
        p[0] = 0
        
def p_error(p):
    prt(f"Synax error  at {p.value!r}")
        
#set up yacc
yaccer = ply.yacc.yacc()

while True:
    try:
        s = input('> ')
    except EOFError:
        break
    yaccer.parse(s)
