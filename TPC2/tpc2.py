import sys

def buscanumerosentreONOFF(line):
    digitos = []
    posicao = 0
    line = line.lower()
    while True:
        on = line.find("on", posicao)
        if on == -1:
            break
        off = line.find("off", on)
        if off == -1:
            break
        posicao_inicio = on + 2
        posicao_fim = off
        numero = line[posicao_inicio:posicao_fim]
        digitos.append(numero)
        posicao = off + 3
    return digitos

def somanumeros(nums):
    soma = 0
    for i in nums:
        soma += int(i)
    return soma

def divide():
    for line in sys.stdin:
        line = line.strip()
        parts = line.split("=")
        return parts

def main():
     sequencias = divide()
     for sequencia in sequencias:
        if len(sequencia)>0:
            numeros = buscanumerosentreONOFF(sequencia)
            print(somanumeros(numeros))
        
main()