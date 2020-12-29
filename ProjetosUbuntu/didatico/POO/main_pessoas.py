from didático.POO.pessoafisica import pf

if __name__ == "__main__":
    name = str(input("Digite um nome:"))
    idade = int(input("Digite sua idade:"))
    cpf = int(input("Digite sua idade:"))
    cliente = pf( cpf,name, idade)
    print(f'O cliente {cliente.get_nome()} possui {cliente.get_idade()} anos e seu CPF é {cliente.get_cpf()}')