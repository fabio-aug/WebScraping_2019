import sys
from DiagnosticoRapido import doenca

if __name__ == '__main__':
    while True:
        doenca.Menu()
        opcao = int(input("Escolha Uma Opção: "))
        while opcao > 2 or opcao < 0:
            opcao = int(input("Escolha Uma Opção Novamente: "))
        #OPÇÕES DO MENU
        if (opcao == 1):
            doenca.amostrar_sintomas()
            escolha = int(input("\nQual o sintoma:"))
            doenca.busca_sintomas(escolha)
        elif (opcao == 2):
            doenca.mostrar_doenca()
        elif (opcao == 0):
            print("---Programa finalizado---")
            sys.exit()

        #Parado do programa
        resp = input('\nContinua Sistema: [S/N]').upper()
        if resp == 'N':
            print("\n---Programa finalizado---")
            break
