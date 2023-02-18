#Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória; (feito)
#Pense num modelo para guardar uma distribuição; (dicionarios)
#Crie uma função que calcula a distribuição da doença por sexo; (feito?)
#Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [30-34], [35-39], [40-44], ... (feito)
#Crie uma função que calcula a distribuição da doença por níveis de colesterol. Considere um nível igual a um intervalo de 10 unidades, comece no limite inferior e crie os níveis necessários até abranger o limite superior; (feito)
#Crie uma função que imprime na forma de uma tabela uma distribuição; (feito)
#Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas; (feito)
#Extra: explore o módulo matplotlib e crie gráficos para as suas distribuições

import csv
import matplotlib.pyplot as plt



def read_csv_file(filename):
    data = []
    with open(filename, 'r',encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
            #print(data)
    return data

#data = read_csv_file("myheart.csv")

#data é uma lista de dicionarios com entradas como a seguinte, representa todo o csv
# {'idade': '54', 'sexo': 'F', 'tensão': '120', 'colesterol': '273', 'batimento': '150', 'temDoença': '0'}

#agora, vou percorrer a lista de dicionarios adicionando info pertinente a outros dicionarios


#descobri depois que nao podia usar o modulo csv, então vou criar uma funcao que faça o mesmo que a read_csv_file

def CSVtoMap(filename):
    res=[]
    with open(filename, 'r', encoding="utf8") as csv_file:
        lines = csv_file.read().split('\n')
        keys = lines[0].split(',')
        for i in range(1, len(lines)):
            line = lines[i]
            if not line:
                continue
            values = line.split(',')
            dic = {}
            for j in range(0, len(keys)):
                dic[keys[j]] = values[j]
            res.append(dic)
    return res

data = CSVtoMap("myheart.csv")

def pessoas_por_genero(data):
    res = {
            'M': 0, #670
            'F': 0  #169
        }
    for entry in data:
        if entry['sexo'] == 'M': res['M']+=1
        elif entry['sexo'] == 'F': res['F']+=1
    return res

pessoasPorGenero = pessoas_por_genero(data)


def doentes_por_genero(data):
    res = {
            'M': 0, #428
            'F': 0  #40
        }
    for entry in data:
        if (entry['sexo'] == 'M') and (entry['temDoença'] == '1') : res['M']+=1
        elif (entry['sexo'] == 'F') and (entry['temDoença'] == '1') : res['F']+=1
    return res

doentesPorGenero = doentes_por_genero(data)

def probabilidade_doenca():
    res = {
            'M': 0, #0.6388059701492538 
            'F': 0  #0.23668639053254437
        }
    res['M'] = doentesPorGenero['M'] / pessoasPorGenero['M']
    res['F'] = doentesPorGenero['F'] / pessoasPorGenero['F']
    return res

probabilidadeDoenca = probabilidade_doenca()
#print(probabilidadeDoenca)

def faixasetarias(data):
    res = {
        '0-4': 0, #0
        '5-9': 0,  #0
        '10-14': 0, #0
        '15-19': 0, #0
        '20-24': 0, #0
        '25-29': 0, #4
        '30-34': 0, #17
        '35-39': 0, #53
        '40-44': 0, #88
        '45-49': 0, #107
        '50-54': 0, #168
        '55-59': 0, #172
        '60-64': 0, #135
        '65-69': 0, #65
        '70-74': 0, #23
        '75-79': 0, #7
        '80-84': 0, #0 
        '85-89': 0, #0
        '90-94': 0, #0
        '95-99': 0, #0
        '100-105': 0 #0
    }
    for entry in data:
        if (int(entry['idade']) >= 0) and (int(entry['idade']) <= 4):
            res['0-4'] += 1
        elif (int(entry['idade']) >= 5) and (int(entry['idade']) <= 9):
            res['5-9'] += 1
        elif (int(entry['idade']) >= 10) and (int(entry['idade']) <= 14):
            res['10-14'] += 1
        elif (int(entry['idade']) >= 15) and (int(entry['idade']) <= 19):
            res['15-19'] += 1
        elif (int(entry['idade']) >= 20) and (int(entry['idade']) <= 24):
            res['20-24'] += 1
        elif (int(entry['idade']) >= 25) and (int(entry['idade']) <= 29):
            res['25-29'] += 1
        elif (int(entry['idade']) >= 30) and (int(entry['idade']) <= 34):
            res['30-34'] += 1
        elif (int(entry['idade']) >= 35) and (int(entry['idade']) <= 39):
            res['35-39'] += 1
        elif (int(entry['idade']) >= 40) and (int(entry['idade']) <= 44):
            res['40-44'] += 1
        elif (int(entry['idade']) >= 44) and (int(entry['idade']) <= 49):
            res['45-49'] += 1
        elif (int(entry['idade']) >= 50) and (int(entry['idade']) <= 54):
            res['50-54'] += 1
        elif (int(entry['idade']) >= 55) and (int(entry['idade']) <= 59):
            res['55-59'] += 1
        elif (int(entry['idade']) >= 60) and (int(entry['idade']) <= 64):
            res['60-64'] += 1
        elif (int(entry['idade']) >= 65) and (int(entry['idade']) <= 69):
            res['65-69'] += 1
        elif (int(entry['idade']) >= 70) and (int(entry['idade']) <= 74):
            res['70-74'] += 1
        elif (int(entry['idade']) >= 75) and (int(entry['idade']) <= 79):
            res['75-79'] += 1
        elif (int(entry['idade']) >= 80) and (int(entry['idade']) <= 84):
            res['80-84'] += 1
        elif (int(entry['idade']) >= 85) and (int(entry['idade']) <= 89):
            res['85-89'] += 1
        elif (int(entry['idade']) >= 90) and (int(entry['idade']) <= 94):
            res['90-94'] += 1
        elif (int(entry['idade']) >= 95) and (int(entry['idade']) <= 99):
            res['95-99'] += 1
        elif (int(entry['idade']) >= 100) and (int(entry['idade']) <= 105):
            res['100-105'] += 1
    return res

faixasEtarias = faixasetarias(data)
#print(faixasetarias(data))

def doentesfaixasetarias(data):
    res = {
        '0-4': 0, #0
        '5-9': 0,  #0
        '10-14': 0, #0
        '15-19': 0, #0
        '20-24': 0, #0
        '25-29': 0, #0
        '30-34': 0, #6
        '35-39': 0, #19
        '40-44': 0, #27
        '45-49': 0, #51
        '50-54': 0, #83
        '55-59': 0, #114
        '60-64': 0, #101
        '65-69': 0, #45
        '70-74': 0, #17
        '75-79': 0, #5
        '80-84': 0, #0 
        '85-89': 0, #0
        '90-94': 0, #0
        '95-99': 0, #0
        '100-105': 0 #0
    }
    for entry in data:
        if (int(entry['idade']) >= 0) and (int(entry['idade']) <= 4) and (entry['temDoença'] == '1'):
            res['0-4'] += 1
        elif (int(entry['idade']) >= 5) and (int(entry['idade']) <= 9) and (entry['temDoença'] == '1'):
            res['5-9'] += 1
        elif (int(entry['idade']) >= 10) and (int(entry['idade']) <= 14) and (entry['temDoença'] == '1'):
            res['10-14'] += 1
        elif (int(entry['idade']) >= 15) and (int(entry['idade']) <= 19) and (entry['temDoença'] == '1'):
            res['15-19'] += 1
        elif (int(entry['idade']) >= 20) and (int(entry['idade']) <= 24) and (entry['temDoença'] == '1'):
            res['20-24'] += 1
        elif (int(entry['idade']) >= 25) and (int(entry['idade']) <= 29) and (entry['temDoença'] == '1'):
            res['25-29'] += 1
        elif (int(entry['idade']) >= 30) and (int(entry['idade']) <= 34) and (entry['temDoença'] == '1'):
            res['30-34'] += 1
        elif (int(entry['idade']) >= 35) and (int(entry['idade']) <= 39) and (entry['temDoença'] == '1'):
            res['35-39'] += 1
        elif (int(entry['idade']) >= 40) and (int(entry['idade']) <= 44) and (entry['temDoença'] == '1'):
            res['40-44'] += 1
        elif (int(entry['idade']) >= 44) and (int(entry['idade']) <= 49) and (entry['temDoença'] == '1'):
            res['45-49'] += 1
        elif (int(entry['idade']) >= 50) and (int(entry['idade']) <= 54) and (entry['temDoença'] == '1'):
            res['50-54'] += 1
        elif (int(entry['idade']) >= 55) and (int(entry['idade']) <= 59) and (entry['temDoença'] == '1'):
            res['55-59'] += 1
        elif (int(entry['idade']) >= 60) and (int(entry['idade']) <= 64) and (entry['temDoença'] == '1'):
            res['60-64'] += 1
        elif (int(entry['idade']) >= 65) and (int(entry['idade']) <= 69) and (entry['temDoença'] == '1'):
            res['65-69'] += 1
        elif (int(entry['idade']) >= 70) and (int(entry['idade']) <= 74) and (entry['temDoença'] == '1'):
            res['70-74'] += 1
        elif (int(entry['idade']) >= 75) and (int(entry['idade']) <= 79) and (entry['temDoença'] == '1'):
            res['75-79'] += 1
        elif (int(entry['idade']) >= 80) and (int(entry['idade']) <= 84) and (entry['temDoença'] == '1'):
            res['80-84'] += 1
        elif (int(entry['idade']) >= 85) and (int(entry['idade']) <= 89) and (entry['temDoença'] == '1'):
            res['85-89'] += 1
        elif (int(entry['idade']) >= 90) and (int(entry['idade']) <= 94) and (entry['temDoença'] == '1'):
            res['90-94'] += 1
        elif (int(entry['idade']) >= 95) and (int(entry['idade']) <= 99) and (entry['temDoença'] == '1'):
            res['95-99'] += 1
        elif (int(entry['idade']) >= 100) and (int(entry['idade']) <= 105) and (entry['temDoença'] == '1'):
            res['100-105'] += 1
    return res

doentesFaixasetarias = doentesfaixasetarias(data)
#print(doentesfaixasetarias(data))

def probabilidadesfaixasetarias(data):
    res = {
        '0-4': 0,
        '5-9': 0,
        '10-14': 0,
        '15-19': 0,
        '20-24': 0,
        '25-29': 0,
        '30-34': 0,
        '35-39': 0,
        '40-44': 0,
        '45-49': 0,
        '50-54': 0,
        '55-59': 0,
        '60-64': 0,
        '65-69': 0,
        '70-74': 0,
        '75-79': 0,
        '80-84': 0, 
        '85-89': 0,
        '90-94': 0,
        '95-99': 0,
        '100-105': 0
    }
    for fe in res:
        if faixasEtarias[fe] != 0:
            res[fe] = doentesFaixasetarias[fe]/faixasEtarias[fe]
    return res

probabilidadesFaixasetarias = probabilidadesfaixasetarias(data)
#print(probabilidadesfaixasetarias(data))

colestrois = []
for entry in data:
        colestrois.append(int(entry['colesterol']))
colestrois.sort()


def numscolestrol(data):
    res = {}
    size = 0
    min = 0
    maior = colestrois[colestrois.__len__()-1]
    aux = min
    intervalosde10 = range(min,maior,10)
    ninter = intervalosde10.__len__()
    topo = 0
    for i in intervalosde10:
        topo = i+10
        key = f"{i}-{topo}"
        res[key] = 0
    for c in colestrois:
        iter = 0
        while(iter < ninter):
            controlo = 0
            if c in range(topo-10,topo,1):
                res[f"{topo-10}-{topo}"]+=1
                controlo = 1
                break
            if c in range(aux,aux+10,1):
                if controlo == 0: res[f"{aux}-{aux+10}"]+=1
                break
            aux+=10
    return res

dicColestrol = numscolestrol(data)

def probabilidadedoencaColestrol():
    total = colestrois.__len__()
    res = {}
    for key in dicColestrol:
        res[key] = dicColestrol[key]/total
    return res

probabilidadeColestrois = probabilidadedoencaColestrol()

#print(probabilidadedoencaColestrol)

def mapatotabela(dicionario):
    print("{:<40} {:<40}".format('Chave','Valor'))
    for k in dicionario:
        print("{:<40} {:<40}".format(k,dicionario[k]))


def histograma(dicionario):
    plt.bar(dicionario.keys(), dicionario.values())
    plt.xticks(rotation=90)
    plt.ylabel('Frequencia')
    plt.title('Histograma')
    plt.show()


def regressar():
    print("Regressar?[S/N]")
    while(True):
        op2 = (input())
        if op2 == "S": menu()
        if op2 == "N": exit()

def graficamente():
    print("1-Grafico de doentes por sexo")
    print("2-Grafico de doentes por faixa etária")
    print("3-Gráfico de doentes por colestrol")
    op = int(input())
    if op == 1:
        histograma(doentesPorGenero)
    elif op == 2:
        histograma(doentesFaixasetarias)
    elif op == 3:
        histograma(dicColestrol)
    regressar()

def menu():
    print("Selecione uma opção: ")
    print("1-Ver total de cada sexo")
    print("2-Ver doentes por sexo")
    print("3-Ver incidência de doença por sexo")
    print("4-Numero de pessoas de cada faixa etária")
    print("5-Doentes de pessoas de cada faixa etária")
    print("6-Incidência de doença por faixa etária")
    print("7-Numero de pessoas por intervalo de colestrol")
    print("8-Incidência de doença por nivel colestrol")
    print("9-Visualizar gráficamente a informação")
    op = int(input())
    if op == 1:
        mapatotabela(pessoasPorGenero)
    elif op == 2:
        mapatotabela(doentesPorGenero)
    elif op == 3:
        mapatotabela(probabilidadeDoenca)
    elif op == 4:
        mapatotabela(faixasEtarias)
    elif op == 5:
        mapatotabela(doentesFaixasetarias)
    elif op == 6:
        mapatotabela(probabilidadesFaixasetarias)
    elif op == 7:
        mapatotabela(dicColestrol)
    elif op == 8:
        mapatotabela(probabilidadeColestrois)
    elif op == 9:
        graficamente()
    regressar()

menu()