import re

def alineaA():
    with open("processos.txt","r",encoding="utf8") as f:
        lines = f.readlines()
        regexAno = re.compile(r"\d+::(\d{4})")
        dicionarioAnos = {}
        for linha in lines:
            correspondenciaAno = regexAno.match(linha)
            if(correspondenciaAno):
                ano = correspondenciaAno.group(1)
                if ano not in dicionarioAnos:
                    dicionarioAnos[ano] = 1
                else:
                    dicionarioAnos[ano] += 1
        return dicionarioAnos

def printdic(dic):
    for key in dic: print("Ano = "+str(key)+", Frequência de processos: "+str(dic[key]))

def main():
    d = alineaA()
    printdic(d)

main()