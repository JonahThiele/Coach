import ply.lex 

# all of our tokens
tokens = (
    'NUMBER',
    'VAR',
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
t_SUB   = r'completed'
t_DIV  = r'splits'
t_INCREMENT = r'Jaccoby'
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
    ('left', 'ADD', 'SUB'),
    ('left', 'TIMES', 'DIVIDE')
    )
    

# Build the lexer
clexer = ply.lex.lex()
    
