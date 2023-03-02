import re


def alineaC():
    with open("processos.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        d = {}
        for linha in lines:
            if linha.strip():  # skip empty lines
                fields = linha.split('::')
                if len(fields) >= 6:
                    observacoes = fields[5]
                    regex = re.compile("\w*,([\w\s]*)\.[\s]*Proc\.[\d]*\.")
                    relacoes = regex.findall(observacoes)
                    if relacoes:
                        for relacao in relacoes:
                            if relacao in d:
                                d[relacao] += 1
                            else:
                                d[relacao] = 1
        return(d)
    
def sortD(dicionario):
    sorted_dict = dict(sorted(dicionario.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict

def main():
    d = alineaC()
    sortedD = sortD(d)
    print(sortedD)

main()