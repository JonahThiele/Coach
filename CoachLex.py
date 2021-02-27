import ply.lex as lex

# all of our tokens
tokens = (
    'FILEIN',
    'NAME',
    'NUMBER',
    'VAR',
    'VARINT',
    'MULT',
    'DIV',
    'ADDA',
    'ADDB',
    'ADDC',
    'ADDD',
    'SUBA',
    'SUBB',
    'SUBC',
    'INCREMENT',
    'TRUE',
    'FALSE',
    'WHILEA',
    'WHILEB',
    'IF',
    'OUTPUT',
    'COMPARISON',
    'FUNC'
    )

# regular expressions basic definitions
def t_ADDA(t): r'laps'; return t
def t_ADDB(t): r'have'; return t
def t_ADDC(t): r'increased'; return t
def t_ADDD(t): r'by:'; return t
def t_SUBA(t): r'completed'; return t
def t_SUBB(t): r'out'; return t
def t_SUBC(t): r'of'; return t
def t_DIV(t): r'split'; return t
def t_MULT(t): r'by'; return t
def t_INCREMENT(t): r'Jaccoby'; return t
def t_VARINT(t): r'lap'; return t
#t_NAME = r'[a-zA-Z0-9_][a-zA-Z0-9_ ]*'
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_FILEIN(t): r'workout'; return t
def t_TRUE(t): r'TRUE'; return t
def t_FALSE(t): r'FALSE'; return t
def t_OUTPUT(t): r'coach:'; return t
def t_IF(t): r'if'; return t
def t_WHILEA(t): r'mile'; return t
def t_WHILEB(t): r'repeats'; return t
def t_FUNC(t): r'func'; return t



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
