
# 1 - Crie uma lista com cinco itens que você compraria no supermercado. Em seguida, realize as seguintes operações:

# 1. Adicione dois novos itens ao final da lista.
# 2. Remova o primeiro item da lista.
# 3. Remova o último item da lista.
# 4. Adicione um novo item ao final da lista e remova o item "Café" da lista.

lista_mercado = ["leite", "ovos", "queijo", "café", "pão"]

print (lista_mercado)

lista_mercado.append("alface")
lista_mercado.append("tomate")

print (lista_mercado)

lista_mercado.pop(0)
lista_mercado.pop(-1)   # ou lista_mercado.pop()

print (lista_mercado)

lista_mercado.append("açúcar")

print (lista_mercado)

lista_mercado.remove("café")

print(lista_mercado)

# 2 - Crie uma lista com cinco nomes de pessoas. Em seguida, realize as seguintes operações:

# 1. Adicione dois novos nomes ao final da lista.
# 2. Substitua o segundo nome da lista por "Anônimo".
# 3. Remova o primeiro nome da lista.
# 4. Remova o último nome da lista.

pessoas = ["camila", "rafael", "heloísa", "vânia", "cida"]

print (pessoas)

pessoas.append("derick")
pessoas.append("gabriela")

print (pessoas) 

pessoas[1] = "anônimo"  # substitui o primeiro item da lista por "anônimo"

print (pessoas)

pessoas.pop(0)

print (pessoas)

pessoas.pop(-1)

print(pessoas)

#3  - Crie uma lista com cinco números inteiros. Em seguida, realize as seguintes operações:

# 1. Adicione um novo número ao final da lista.
# 2. Remova o menor número da lista.
# 3. Remova o último número da lista.
# 4. Adicione um novo número ao final da lista e remova o primeiro número da lista.

numeros_inteiros = [1, 2, 3, 4, 5]

print(numeros_inteiros)

numeros_inteiros.append(6)

print(numeros_inteiros)

# (min()) - retorna o menor valor | (max()) - retorna o maior valor

numeros_inteiros.remove(min(numeros_inteiros)) 

print(numeros_inteiros)

numeros_inteiros.pop(-1)

print(numeros_inteiros)

numeros_inteiros.append(50)

print(numeros_inteiros)

numeros_inteiros.pop(0)

print(numeros_inteiros)

#4 - Prever a saída (estilo Cisco) - Sem rodar, diga o que aparece na tela. Depois rode e confira.

a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(99)
print(a)
print(c)

#5  - Lista de convidados - Crie uma lista com 4 nomes. Peça um nome ao usuário. Se o nome estiver na lista (in), mostre "Pode entrar". Caso contrário, mostre "Você não está na lista".

lista_convidados = ["camila", "gabriela", "heloísa", "vânia"]

nome_informado = input("seu nome: ")

if nome_informado in lista_convidados:
    print("pode entrar!")

else:
    print("você não está na lista!")