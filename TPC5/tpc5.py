from ply.lex import lex
import sys
import re

saldo = 0

coins = {
    '1c' : 1,
    '2c' : 2,
    '5c' : 5,
    '10c' : 10,
    '20c' : 20,
    '50c' : 50,
    '1e' : 100,
    '2e' : 200
}

numeros = [
    (r'601\d+', -1),
    (r'641\d+', -1),
    (r'00\d+', 150),
    (r'2\d+', 25),
    (r'800\d+', 0),
    (r'808\d+', 10)
]

tokens = [
    'POUSAR',
    'CHAMADA',
    'LEVANTAR',
    'MOEDA',
    'ABORTAR'
]

states = (
    ('MOEDA', 'inclusive'),
    ('CHAMADA', 'inclusive')
)

def t_ANY_ABORTAR(t):
    r'ABORTAR'
    global saldo
    saldo = 0
    print("Retire as moedas.")
    sys.exit()

t_ignore  = ' \t'

def formataSaldo(saldo):
    sts = str(saldo)
    p = ""
    if saldo<100:
        sts+='c'
        p = "saldo = "+sts
    else:
        euros = str(int(saldo/100))
        centimos = str(saldo%100)
        p = "saldo = "+euros+"e"+centimos+"c"
    return p

def t_INITIAL_LEVANTAR(t):
    r'LEVANTAR'
    print("Introduza moedas.")
    t.lexer.begin('MOEDA')

def t_MOEDA_POUSAR(t):
    r'POUSAR'
    print('Volte sempre!')
    t.lexer.begin('INITIAL')

def t_MOEDA_MOEDA(t):
    r'MOEDA(\s*\d+[ce][,.])*'
    global saldo
    moedas = t.value[6:]
    listamoedas = re.findall("\d+[ce]",moedas)
    r = ""
    for moeda in listamoedas:
        if moeda in coins:
            saldo += coins[moeda]
        else:
            r+=f'{moeda} moeda inválida; '
    r+= formataSaldo(saldo)
    print(r)
    t.lexer.begin('CHAMADA')
    return t

def t_CHAMADA_CHAMADA(t):
    r'T\s*=\s*(\d+)'
    global saldo
    numero = re.search('(\d+)',t.value).group(1)
    custo = None
    for valor in numeros:
        if re.match(valor[0],numero):
            custo = valor[1]
    if (custo ==-1):
        print('Esse número não é permitido neste telefone. Queira discar novo número!')
    elif (custo == None):
        print("Número desconhecido")
    elif saldo < custo:
        print('Saldo insuficiente')
    else:
        saldo -= custo
        print(formataSaldo(saldo)) 
    return t

def moedasOrdenadas(coins):
    m = []
    for coin in coins:
        m.append(coins[coin])
    m.reverse()
    return m

moedas = moedasOrdenadas(coins)

def formataTroco(aux):
    m = []
    mOrd=[]
    tr = "troco="
    for key,value in coins.items():
        if aux[value]>0:
            m.append(str(aux[value])+"x"+key)
    m.reverse()
    for i in m:
        if i == m[len(m)-1]:
            tr+=" "+i+"; Volte sempre!"
        else:
            tr+=" "+i+","
    return tr

def troco():
    global saldo
    troco = saldo
    aux = {}
    for moeda in moedas:
        aux[moeda] = 0
    for moeda in moedas:
        c = int(troco/moeda)
        troco = troco - (c*moeda)
        aux[moeda] = c
    return formataTroco(aux)

def t_CHAMADA_POUSAR(t):
    r'POUSAR'
    global saldo
    p =troco()
    saldo = 0
    print(p)
    t.lexer.begin('INITIAL')
    return t

def t_INITIAL_ANY(t):
    r'.+'
    print('Erro ao iniciar a máquina')

def t_MOEDA_ANY(t):
    r'.+'
    print('Erro na introdução de moedas.')

def t_CHAMADA_ANY(t):
    r'.+'
    print('Erro, introduza um número ou pouse o telefone')

def t_ANY_newline(t):
    r'\n+'
    return t

def t_error(t):
    t.lexer.skip(1)

lexer = lex()
for s in sys.stdin:
    lexer.input(s)
    t = lexer.token()
    while(t):
        t = lexer.token()
        