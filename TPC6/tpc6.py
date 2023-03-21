from ply.lex import lex

# Definição dos padrões de expressão regular para cada token
tokens = (
    'INT',
    'NUMBER',
    'FUNCTION',
    'PROGRAM',
    'ID',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'ASSIGN',
    'IF',
    'WHILE',
    'FOR',
    'PRINT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'EQ',
    'NEQ',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'COMMENT',
    'MULTILINECOMMENTOPEN',
    'MULTILINECOMMENTCLOSE',
    'INLINECOMMENT',
    'RANGE'
)

# Padrões de expressão regular para tokens simples
t_NUMBER = r'\d+(\.\d+)?'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Funções para tokens mais complexos
def t_MULTILINECOMMENTOPEN(t):
    r'\/\*.*\n'
    return t

def t_MULTILINECOMMENTCLOSE(t):
    r'.*\*\/'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

def t_INT(t):
    r'int'
    return t

def t_IF(t):
    r'if'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_COMMENT(t):
    r'\/\/.*\n'
    return t

def t_INLINECOMMENT(t):
    r'--.*\n'
    return t

def t_RANGE(t):
    r'\[\d+..\d+\]'
    return t

def t_ASSIGN(t):
    r'[0-9a-zA-Z]*=[0-9a-zA-Z]*'
    return t

def t_PLUS(t):
    r'[0-9a-zA-Z]*\+[0-9a-zA-Z]*'
    return t

def t_MINUS(t):
    r'[0-9a-zA-Z]*-[0-9a-zA-Z]*'
    return t

def t_TIMES(t):
    r'[0-9a-zA-Z]*\*[0-9a-zA-Z]*'
    return t

def t_DIVIDE(t):
    r'[0-9a-zA-Z]*/[0-9a-zA-Z]*'
    return t

def t_MODULO(t):
    r'[0-9a-zA-Z]*%[0-9a-zA-Z]*'
    return t

def t_EQ(t):
    r'[0-9a-zA-Z]*==[0-9a-zA-Z]*'
    return t

def t_NEQ(t):
    r'[0-9a-zA-Z]*!=[0-9a-zA-Z]*'
    return t

def t_LT(t):
    r'[0-9a-zA-Z]*<[0-9a-zA-Z]*'
    return t

def t_LTE(t):
    r'[0-9a-zA-Z]*<=[0-9a-zA-Z]*'
    return t

def t_GT(t):
    r'[0-9a-zA-Z]*>[0-9a-zA-Z]*'
    return t

def t_GTE(t):
    r'[0-9a-zA-Z]*<=[0-9a-zA-Z]*'
    return t

# Ignora espaços em branco e tabulações
t_ignore = ' \t'

# Define um contador de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define um tratamento para erros léxicos
def t_error(t):
    print(f"Caracter inválido '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Palavras reservadas
reserved = {
    'function': 'FUNCTION',
    'program': 'PROGRAM',
    'int': 'INT',
    'if': 'IF',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT',
}

with open('e1.txt', 'r') as f:
    lines = f.readlines()

#with open('e2.txt', 'r') as f:
#    lines = f.readlines()

lexer = lex()
for l in lines:
    lexer.input(l)
    t = lexer.token()
    while(t):
        print(t)
        t = lexer.token()
        