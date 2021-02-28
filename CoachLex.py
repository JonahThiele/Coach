import ply.lex as lex

# all of our tokens
tokens = (
    'FILEIN',
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
    'WHILE',
    'IFA',
    'IFB',
    'IFC',
    'OUTPUT',
    'LESSTHAN',
    'GREATERTHAN',
    'GREATLESSTHANA',
    'GREATLESSTHANB',
    'EQUALTOA',
    'EQUALTOB',
    'THEN',
    'ELSE'
    )

# regular expressions basic definitions
def t_ADDA(t): r'laps'; return t
def t_ADDB(t): r'have'; return t
def t_ADDC(t): r'increased'; return t
def t_ADDD(t): r'by:'; return t
def t_SUBA(t): r'finished'; return t
def t_SUBB(t): r'out'; return t
def t_SUBC(t): r'of'; return t
def t_DIV(t): r'split'; return t
def t_MULT(t): r'by'; return t
def t_INCREMENT(t): r'Jaccoby'; return t
def t_VARINT(t): r'lap'; return t
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_ ]*'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'
def t_OUTPUT(t): r'Coach:'; return t
def t_LESSTHAN(t): r'slower';return t
def t_GREATLESSTHANA(t): r'was'; return t
def t_GREATERTHAN(t): r'faster'; return t
def t_GREATLESSTHANB(t): r'than'; return t
def t_EQUALTOA(t): r'similar'; return t
def t_EQUALTOB(t): r'to'; return t
def t_IFA(t): r'If'; return t
def t_IFB(t): r'your'; return t
def t_IFC(t): r'time,'; return t
def t_WHILE(t): r'while'; return t
def t_THEN(t): r'then'; return t
def t_ELSE(t): r'elses'; return t
def t_FILEIN(t): r'workout'; return t



# complex definitions 
t_ignore = " \t"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


precedence = (
    ('left', 'IF'),
    ('left', 'ELSE'),
    ('left', 'VARINT'),
    ('left', 'VAR'),
    ('left', 'ADD', 'SUB'),
    ('left', 'TIMES', 'DIVIDE')
    )
    

# Build the lexer
clexer = lex.lex()
