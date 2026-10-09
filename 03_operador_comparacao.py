
#1 - Crie um programa que peça ao usuário para digitar a sua idade e a idade de um amigo. Verifique se as idades são iguais e, se forem, exiba a mensagem "Vocês têm a mesma idade".

print()

idade01 = int(input("informe a sua idade (somente números): "))
idade02 = int(input("informe a idade do seu amigo (somente números): "))

if (idade01 == idade02):

    print() 
    print("vocês têm a mesma idade! 😁")
    print()

else:

    print()
    print("vocês não têm a mesma idade! 🙁")
    print()

#2 - Crie um programa que peça ao usuário para digitar dois números. Verifique se os números são diferentes e, se forem, exiba a mensagem "Os números são diferentes".

numero01 = int(input("informe o primeiro número: "))
numero02 = int(input("informe o segundo número: "))

if (numero01 != numero02): 

    print()
    print("os números são diferentes! 🙁")
    print()

else:

    print()
    print("os números são iguais! 😁")
    print()

#3- Crie um programa que peça ao usuário para digitar a sua altura e a altura de um amigo (em centímetros). Verifique se a altura do usuário é maior que a do amigo e, se for, exiba a mensagem "Você é mais alto que seu amigo".

altura_user = int(input("informe a sua altura: "))
altura_amigo = int(input("informe a altura do seu amigo: "))

if (altura_user > altura_amigo):

    print()
    print("você é mais alto que seu amigo! 😁")
    print()

else:

    print()
    print("você é mais baixo que seu amigo! 🙁")
    print()

#4-  Crie um programa que peça ao usuário para digitar a sua nota em uma prova e a nota mínima necessária para passar. Verifique se a nota do usuário é menor que a nota mínima e, se for, exiba a mensagem "Você não passou na prova".

nota_user = float(input("informe a sua nota: "))
nota_minima = float(input("informe a nota mínima: "))

if (nota_user < nota_minima):

    print()
    print("você não passou na prova! 🙁")
    print()

else:

    print()
    print("você passou na prova! 😁")
    print()

#5 - Crie um programa que peça ao usuário para digitar a quantidade de horas que ele estudou em uma semana e a quantidade mínima de horas recomendadas. Verifique se o usuário estudou o suficiente e, se sim, exiba a mensagem "Você estudou o suficiente nesta semana".

horas_estudo = float(input("informe a quantidade de horas que você estudou nesta semana: "))
horas_minimas = float(input("informe a quantidade mínima de horas recomendadas: "))

if (horas_estudo < horas_minimas):

    print()
    print("você não estudou o suficiente nesta semana! 🙁")
    print()

else:

    print()
    print("você estudou o suficiente nesta semana! 😁")
    print()
    print("fim!!! 😉")
    print()