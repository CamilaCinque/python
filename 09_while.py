
# 1 - Soma até zero - Peça números ao usuário até ele digitar 0. No final, mostre a soma de todos.

soma = 0

numero = int(input("informe um número para somar (0 para parar): "))

while numero != 0:

    soma += numero
    numero = int(input("informe um número para somar (0 para parar): "))
   
print("a soma dos números informados é:", soma)

#1 - Escreva um programa que continue pedindo ao usuário para digitar a senha correta até que ele acerte. Quando a senha correta for inserida, o programa deve exibir uma mensagem de sucesso e encerrar.

senha_correta = "123"

senha_informada = input("informe a sua senha: ")

while senha_correta != senha_informada:
    senha_informada = input("informe a sua senha: ")

print("\nsenha correta! o login foi realizado com sucesso. 😉")

#2 - Peça ao usuário para adivinhar um número entre 1 e 20. O loop continuará até que o usuário acerte o número. Informe ao usuário se o palpite foi maior ou menor que o número correto.

# **Dica:** Defina um número secreto e compare os palpites do usuário com esse número.

numero_secreto = 17

numero_informado = 0 #int(input("\ninforme o seu palpite (somente números de 0 a 20): "))

while numero_secreto != numero_informado:

    numero_informado = int(input("informe o seu palpite (somente números de 0 a 20): "))

    print("você errou! tente novamente. 🫤\n")

    if numero_informado > numero_secreto:
        print("muito alto! tente um número menor.")

    else:
        print("muito baixo! tente um número maior.")

print("você acertou! 😁")

 

 

