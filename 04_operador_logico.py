
#1 (and)** - Crie um programa de login. Peça usuário e senha. Se o usuário for "aluno" **e** a senha for "1234", mostre "Login realizado". Caso contrário, mostre "Usuário ou senha incorretos".

usuario = input("\ninforme o seu usuário: ")
senha = int(input("informe a senha: "))

if usuario == "aluno" and senha == 1234:
    print("\nlogin realizado com sucesso! 😉")

else:
    print("\nusuário ou senha incorretos. 🙁")

#2 (or)** - Peça ao usuário o dia da semana (ex.: sabado). Se for "sabado" **ou** "domingo", mostre "Fim de semana!". Caso contrário, mostre "Dia útil".

dia_semana = input("\ninforme o dia da semana: ")

if dia_semana == "sabado" or dia_semana == "domingo":
    print("\nhoje é fim de semana! 😁\n")

else:
    print("\nhoje é dia útil. 😉\n")

#3 (not)** - Crie a variável `bateria_carregada = False`. Se a bateria **não** estiver carregada, mostre "Conecte o carregador". Caso contrário, mostre "Bateria ok". Depois troque para `True` e veja a diferença.

bateria_carregada = False

if not bateria_carregada:
    print("conecte o carregador. 😉")

else:
    print("bateria ok! 😁")
