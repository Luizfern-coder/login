

resposta = input('''[1] - Cadastrar novo usuário 
[2] - Fazer Login
''')
#armazenando os usuarios existentes
usuarios = ['carol', 'amanda', 'jeff']
senhas = ['12345', 'abcde', '123abdc']


if resposta == '1':
    #recebendo um usuario    
    usuario_digitado = input("Digite seu usuário: ")
 
    if usuario_digitado in usuarios:
        print("usuário existente")
    else:
    #recebendo uma senha 
     senha_digitada = input("Digite sua senha: ")
     usuarios.append(usuario_digitado)
     senhas.append(senha_digitada)
elif resposta == '2':
    usuario_digitado = input("Digite seu usuario: ")
    senha_digitada = input("Digite a senha:  ")
    encontrado = False
    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario and senha_digitada == senhas[indice]:
            print("Login Efetuado com Sucesso")
            encontrado = True
        elif encontrado == False:
            print('Usuario ou senha incorreto!')
else:
    print("Digitar apenas 1 ou 2")
