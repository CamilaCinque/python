
#1 - Frete por peso** - Peça o peso do pacote em kg. Até 1 kg o frete é R$ 10; até 5 kg é R$ 20; acima de 5 kg é R$ 35. Mostre o valor do frete.

peso_informado = float(input("\ninforme o peso do pacote (em kg): "))

if peso_informado <= 1:
    print("o frete é R$10!")

elif peso_informado <= 5: # ou: elif peso_informado > 1 and peso_informado <= 5:
    print("o frete é R$20!")

else:
    print("o frete é R$35!")

#2 - Menu do banco** - Mostre as opções 1 - Saldo, 2 - Extrato, 3 - Sair. Peça a opção e mostre a mensagem correspondente. Se digitar outra coisa, mostre "Opção inválida".

opcao_selecionada = int(input("selecione uma opção: \n\n1 - saldo\n2 - extrato\n3 - sair\n\n"))

# if opcao_selecionada != 1 and opcao_selecionada != 2 and opcao_selecionada != 3:
#     print("opção inválida!")
# else:
#     print("opção selecionada:", opcao_selecionada, "\n")

if opcao_selecionada == 1:
    print("opção selecionada: mostrar saldo")

elif opcao_selecionada == 2:
    print("opção selecionada: mostrar extrato")

elif opcao_selecionada == 3:
    print("opção selecionada: sair")

else:
    print("opção inválida!")