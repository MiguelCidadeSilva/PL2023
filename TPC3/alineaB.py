import re
#o dataset tem linhas invalidas mas nao as filtrei
def seculo(ano):
    if ano % 100 == 0:
        seculo = ano // 100
    else:
        seculo = (ano // 100) + 1
    return seculo

def alineaB():
    with open("processos.txt","r",encoding="utf8") as f:
        lines = f.readlines()
        regexAno = re.compile(r"\d+::(\d{4})")
        regexNomes = re.compile(r":([a-zA-Z]+)\b.*?([a-zA-Z]+)[:,]") #([a-zA-Z]+)\b -> obtem o primeiro nome, o : antes é necessario para ficar apenas pelos nomes;.*?-> caracteres entre os nomes (não greedy para apenas consumir os espaços), ([a-zA-Z]+)[:,]-> apanha restantes nomes podendo estes terminar com : ou , consoante a linha
        dseculos = {}
        for linha in lines:
            correspondenciaAno = regexAno.match(linha)
            nomes_correspondencia = re.findall(regexNomes,linha)
            for nome in nomes_correspondencia:
                if(correspondenciaAno):
                    ano = correspondenciaAno.group(1)
                    century = seculo(int(ano))
                    if century not in dseculos:
                        dseculos[century] = {}
                        (dseculos[century])['nomes'] = {}
                        (dseculos[century])['apelidos'] = {}
                nomeP, apelido = nome
                if nomeP in ((dseculos[century])['nomes']):
                    ((dseculos[century])['nomes'])[nomeP]+=1
                else:
                    ((dseculos[century])['nomes'])[nomeP]=1
                if apelido in ((dseculos[century])['apelidos']):
                    ((dseculos[century])['apelidos'])[apelido]+=1
                else:
                    ((dseculos[century])['apelidos'])[apelido]=1
        return dseculos

def sortD(dicionario):
    sorted_dict = dict(sorted(dicionario.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict

def topn(n,d):
    for key in d:
        print("Top "+str(n)+" no século "+str(key)+":")
        nomes = (d[key])['nomes']
        apelidos = (d[key])['apelidos']
        sortedNomes = sortD(nomes)
        sortedApelidos = sortD(apelidos)
        contaN = 0
        for nome, ocorrenciasN in sortedNomes.items():
            print("   | Nome = "+nome+" | Ocorrências = "+str(ocorrenciasN)+"|")
            contaN += 1
            if contaN == 5:
                break
        contaA = 0
        for apelido, ocorrenciasA in sortedApelidos.items():
            print("   | Apelido = "+apelido+" | Ocorrências = "+str(ocorrenciasA)+"|")
            contaA += 1
            if contaA == 5:
                break

def main():
    d = alineaB()
    topn(5,d)
main()