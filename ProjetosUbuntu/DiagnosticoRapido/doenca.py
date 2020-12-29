from DiagnosticoRapido import Pegar_doencas
import re
# PRINT DO MENU
def Menu():
    print(" --------< DIAGNOSTICO RÁPIDO >------- ")
    print("=-=" * 13)
    print("1.Busca Por Sintoma \n2.Ver Todas Doenças\n0.Exit/Quit")
    print("=-=" * 13)

# PRINT DOS DADOS NOS .TXT
def amostrar_doenca():
    n = 0
    print("---DOENÇAS NO SISTEMA---")
    for line in Pegar_doencas.dados_doenca:
        print(f'{n}. {line}')
        n += 1

def amostrar_sintomas():
    print("---SINTOMAS NO SISTEMA---")
    n = 0
    for line in list_sintoma_txt:
        print(f'{n}. {line}')
        n += 1
# BUSCADOR DE DOENÇAS
def busca_sintomas(i):
    todas_doencas = []
    todas_descricoes = []
    todos_sintomas = []
    print('--------------',list_sintoma_txt[i], '-----------------')
    for c in range(len(Pegar_doencas.dados_sintomas)):
        for v in  Pegar_doencas.dados_sintomas[c]:
            #if(list_sintoma_txt[i] in Pegar_doencas.dados_sintomas[c][v]):
            if re.search(list_sintoma_txt[i],v,re.IGNORECASE):
                todas_doencas.append(Pegar_doencas.dados_doenca[c])
                todas_descricoes.append(Pegar_doencas.dados_descricao[c])
                todos_sintomas.append(Pegar_doencas.dados_sintomas[c])
    print("---- DOENÇAS ENCONTRADAS ----")
    for i in range(len(todas_descricoes)):
        nome = todas_doencas[i]
        descricao = todas_descricoes[i]
        sintomas = todos_sintomas[i]
        print(f"Nome: {nome} \nDescrição: {descricao} \nSintomas: {sintomas}")
        print('=-'*20)


# MOSTRA TODAS DOENÇAS CADASTRADAS
def mostrar_doenca():
    amostrar_doenca()
    desc = int(input("\nInformação De Qual Doença Deseja? "))
    nome =  Pegar_doencas.dados_doenca[desc]
    descricao = Pegar_doencas.dados_descricao[desc]
    sintomas = Pegar_doencas.dados_sintomas[desc]
    print(f"Nome: {nome} \nDescrição: {descricao} \nSintomas: {sintomas}")

# Listar sintomas
list_sintoma_txt = list()
with open('sintoma.txt', "r") as sint:
    if sint.mode == 'r':
        conti = sint.read()
        cont = conti.splitlines()
        for content in cont:
            list_sintoma_txt.append(content)