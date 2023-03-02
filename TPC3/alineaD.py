import json
#PASTA|DATA|NOME|PAI|MAE|OBSERVACOES
def alinead(n):
    with open("processos.txt", "r") as f1:
        linhas = f1.readlines()
        l = []
        for i in range(0,n):
            linha = linhas[i]
            partes = linha.split('::')
            d = {
                'pasta': partes[0],
                'data': partes[1],
                'nome': partes[2],
                'pai': partes[3],
                'mae': partes[4],
                'observacoes': partes[5]
            }
            l.append(d)
        with open("alineaD.json", "w") as f2:
            json.dump(l,f2,indent=4)
                  
def main():
    alinead(20)

main()
