import ply.yacc as yacc
from CoachLex import tokens

#enviromental variables
enviro_vars = {}

def p_statement_assign(p):
    'statement : VARINT VAR expression'
    enviro_vars[p[2]] = p[3]

def p_statement_expr(p):
    'statement : expression'

def p_statement_output(p):
    'statement : OUTPUT expression'
    print("Coach says " + str(p[2]) + "!")

def p_statement_if(p):
    '''statement : IFA IFB IFC comparison THEN statement'''
    if p[4]: p[6]

def p_statement_file_in(p):
    'statement : FILEIN VAR'
    file_str = ""
    f = open(p[2] + "." + 'osxc', "r")
    for line in f:
        file_str = '' 
        file_str += line.rstrip('\n')
        yaccer.parse(file_str)

#def p_statement_increment(p):
   # 'statement : INCREMENT expression'
    #enviro_vars[p[2]] = p[2] + 1

#Basic Math
def p_expression_basicop(p):
    '''expression : expression ADDA ADDB ADDC ADDD expression
                  | expression SUBA SUBB SUBC expression
                  | expression MULT expression
                  | expression DIV expression'''
    if p[2] == 'laps' and p[3] == 'have' and p[4] == 'increased' and p[5] == 'by:': p[0] = p[1] + p[6]
    elif p[2] == 'finished' and p[3] == 'out' and p[4] == 'of': p[0] = p[5] - p[1]
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

def p_comparison_binop(p):
    '''comparison : expression GREATLESSTHANA EQUALTOA EQUALTOB expression
                  | expression GREATLESSTHANA GREATERTHAN GREATLESSTHANB expression
                  | expression GREATLESSTHANA LESSTHAN GREATLESSTHANB expression'''
    if p[4] == 'same': p[0] = p[1] == p[6]
    elif p[3] == 'faster': p[0] = p[1] > p[5]
    elif p[3] == 'slower': p[0] = p[1] < p[5]
        
def p_error(p):
    print(f"Synax error  at {p.value!r}")
        
#set up yacc
yaccer = yacc.yacc()

while True:
    try:
        s = input('> ')
    except EOFError:
        break
    yaccer.parse(s)
