import csv
import re
import json

#obtenho os campos que sao listas ou ocupados pela lista anterior [(posicao do campo,lista)]
def camposLista(campos):
    camposL = []
    camposN = []
    i = 0
    for c in campos:
        if (re.match(r".*{\d+}",c) or c == ""): #[(3, 'Notas{5}'), (4, ''), (5, ''), (6, ''), (7, ''), (8, '')]
            camposL.append((i,c))
        elif (re.match(r".*{\d+",c) or re.match(r"\d+}",c)):
            camposL.append((i,c))
        else: camposN.append((i,c))  #[(0, 'Número'), (1, 'Nome'), (2, 'Curso')]
        i+=1
    return camposN,camposL

def temOperacao(campo):
    operacao = None
    matchObj = re.search(r"::(\w+)",campo)
    if (matchObj != None):
        operacao = matchObj.group(1)
    return operacao

def soma(l):
    r = 0
    for i in l:
        if i:
            r += i
    return r

def naoVazios(l):
    r = 0
    for i in l:
        if i:
            r += 1
    return r

def media(l):
    r = 0
    n = naoVazios(l)
    if(n>0):
        total = soma(l)
        r = total/n
    else:
        r = None
    return r

def abreF(file):
    with open(file, 'r', encoding="utf-8") as ficheiroCSV:
        csvreader = csv.reader(ficheiroCSV)
        campos = next(csvreader)
        camposN, camposL = camposLista(campos)
        l = []
        for linha in csvreader:
            listaOperacoes = []
            d = {}
            tamanhoLinha = len(linha)
            key = None
            for i in range(tamanhoLinha):
                if (i, campos[i]) in camposN:
                    d[campos[i]] = linha[i]
                elif campos[i] != "" and (i,campos[i]) in camposL and not re.match(r"\d+}",campos[i]):
                    key = campos[i].split("{")[0]
                    d[key] = [int(linha[i])]
                elif key is not None:
                    if(temOperacao(campos[i])!=None):
                        listaOperacoes.append((key,temOperacao(campos[i])))
                    if(linha[i]!=""):
                        d[key].append(int(linha[i]))
            if(listaOperacoes):
                for k,o in listaOperacoes:
                    r = 0
                    numeros = d[k]
                    if o == "sum":
                        r = soma(numeros)
                    elif o == "media":
                        r = media(numeros)
                    d.pop(k)
                    d[str(k).lower()+"_"+o] = r
            l.append(d)
        return (l)

def toJson(f):
    nomeJson = re.match("(.*)\.csv",f).group(1)+".json"
    colecao = abreF(f)
    with open(nomeJson,"w",encoding="utf-8") as ficheiroJson:
        json.dump(colecao, ficheiroJson, indent=4, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    toJson("alunos.csv")
    toJson("alunos2.csv")
    toJson("alunos3.csv")
    toJson("alunos4.csv")
    toJson("alunos5.csv")