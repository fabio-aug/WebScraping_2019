import sys
def menuImprime():
    print("Login/Cadastro:")

def check_users(email):
    #coleta lista de usuarios 'list_users'
    list_users = set()
    f = open("logins.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        contents = contents.splitlines()
        for content in contents:
            list_users.add(content)
    f.close()
    #testa se um usuario existe
    email_check = email
    for i in list_users:
      email_user = i.split(',')[0]
      if(email_user == email_check):
          print("usuario existe, usar outro email")
          return True
    return False

def cadastrar():
    while True:
        email = input("E-mail: ")
        name = input("Nome:")
        password = input("Senha: ")
        if (check_users(email) == False):
            break      
    #adiciona user no arquivo de login
    f = open("logins.txt","r")
    content = f.readlines()
    content.append(email + ',' + name + ',' + password + '\n')
    f.close()
    f = open("logins.txt","w")
    f.writelines(content)
    f.close()
    return print("O usuário foi cadastrado no sistema com êxito!!")


def login():
    f = open("logins.text", "r")
    lista = f.readlines()
    while True:
        emailusu = input("Informe seu Email: ")
        senhausu = input("Informe sua Senha: ")
        emailverifica = lista.split(',')[0]
        senhaverifica = lista.split(',')[2]
        for i in lista:
            if (emailusu == emailverifica and senhausu == senhaverifica):
                print("Bem vindo, ", lista.split(',')[1])
                return True
        print("---USUÁRIO INVÁLIDO!!!---")
        resp = input('Continua no sistema Sistema: [S/N]').upper()
        if resp == 'N':
            print("---Programa finalizado---")
            sys.exit()
    f.close()

#(emailusu != emailverifica or senhausu != senhaverifica)
