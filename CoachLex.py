import ply.lex as lex

# all of our tokens
tokens = (
    'NUMBER',
    'VAR',
    'VARINT',
    'MULT',
    'DIV',
    'ADD',
    'SUB',
    'INCREMENT',
    'TRUE',
    'FALSE',
    'WHILE',
    'IF',
    'OUTPUT',
    'LESSTHAN',
    'GREATERTHAN',
    'FUNC'
    )

# regular expressions basic definitions
t_ADD    = r'number to go'
t_SUB   = r'completed out of'
def t_DIV(t): r'split'; return t
def t_MULT(t): r'by'; return t
def t_INCREMENT(t): r'Jaccoby'; return t
def t_VARINT(t): r'laps'; return t
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'
t_OUTPUT = r'Coach;'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_IF = r'if'
t_WHILE = r'while'
t_FUNC = r'func'



# complex definitions 
t_ignore = " \t"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineo += t.value.count("\n")

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


precedence = (
    ('left', 'VARINT'),
    ('left', 'VAR'),
    ('left', 'ADD', 'SUB'),
    ('left', 'TIMES', 'DIVIDE')
    )
    

# Build the lexer
clexer = lex.lex()
