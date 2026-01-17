#Sistemde de Login
#Autor: Matheus Henrique
#Data: 17/10/25

entrada = input("Você quer fazer login ou cadastro?")

if entrada == 'login':
    login = input("Digite seu nome de usuário:")
    senha = input("Digite sua senha:")
    print("Bem-vindo(a) ao Sistema!")
    
elif entrada == 'cadastro':
    cadastro = input("Digite um nome de usuário:")
    senha = input("Digite uma senha:")
    idade = int(input("Coloque sua idade:"))
    if idade >=18:
        print("Idade apropriada!")
        entrar = input("Quer entrar ou sair?")
        if entrar == 'entrar':
            print("Faça login!")
            e = input("Coloque seu nome de usuário:")
            s = input("Coloque sua senha:")
            senha_permitida = senha
            nome_permitido = cadastro
            if e == nome_permitido and s == senha_permitida:
                print("Você entrou, parabéns!")
            else:
                print("Ops, algo errado!")
    else:
        print("Você é de menor!")
else:

    print("Digite cadastro ou login.")
