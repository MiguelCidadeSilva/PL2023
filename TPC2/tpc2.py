import sys

def somanumeros(inicio,nums,nvezes): #soma numeros de uma lista a um valor inicial e imprime nvezes o resultado
    for i in nums:
        inicio += int(i)
    for n in range(0,nvezes): print(inicio)
    return inicio

def parse(linha):
    linha = linha.lower()
    numeros = []
    posicao_on = -1  # posição da última ocorrência de "On"
    posicao = 0
    soma = 0
    while True:
        on = linha.find("on", posicao_on + 1)
        if on == -1:
            break
        off = linha.find("off", on)
        if off == -1:
            break
        conteudo = linha[on + 2:off]
        numero_atual = ""
        for c in conteudo:
            if c.isdigit():
                numero_atual += c
            else:
                if numero_atual:
                    numeros.append(numero_atual)
                    soma += int(numero_atual)
                    numero_atual = ""
                if c == "=":
                    print(soma)
        if numero_atual:
            numeros.append(numero_atual)
        posicao_on = on  # atualiza a posição da última ocorrência de "On"
        posicao = off + 3
    return numeros

def vaiateprimeiraOcur(line,substring): #percorre uma string até à primeira ocurrencia de uma substring
    lineaux = line.lower()
    substringaux = substring.lower()
    pos_on = lineaux.find(substringaux)
    if pos_on >= 0:
        return line[:pos_on]
    else:
        return line

def trataiguaisnoinicio(line): #imprimo 0 até ao primeiro on
    antesdoOn = vaiateprimeiraOcur(line,"On")
    for c in antesdoOn:
        if c == "=":
            print(0)    

def contaiguaisnofim(line): #inverto a lista e procuro por ffo somando iguais até lá
    line.lower()
    iguais = 0
    ateoff = vaiateprimeiraOcur(line[::-1],"ffO")
    for c in ateoff:
        if c == "=":
            iguais+=1
    return iguais


def trataiguaisnofim(line):
    iguaisnofim= contaiguaisnofim(line) #conta iguais no fim
    linha = line[:-iguaisnofim]
    somanumeros(0,parse(linha),iguaisnofim) #trata do conteudo importante, numeros a somar

#Main -> por cada igual até ao primeio On printo 0, pois não se soma nada, e depois processo o que está entre o On e o Off, printando
# n vezes o resultado final consoante o numero de iguais que surjam apos o off
def main():
     for line in sys.stdin:
        trataiguaisnoinicio(line)
        trataiguaisnofim(line)        

main()