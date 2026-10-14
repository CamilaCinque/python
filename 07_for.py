
# avaliação de notas:

notas = [6.0, 7.0, 2.0, 10.0]

for nota in notas:

    if nota >= 6:
        print(nota, "aprovado!")

    else:
        print(nota, "reprovado!")

# somar valores do carrinho

valores_carrinho = [12.50, 30.00, 7.50]

# inicia com total = 0
total = 0   

# conforme for rodando, cada elemento da lista vai passar pela variável "valor"
for valor in valores_carrinho:  

    # aqui, a variável "total" passa a guardar e somar todas as informações de valor

    total += valor # total = total + valor

print(total)

# 1 - Maior temperatura (sem usar max)** - Com a lista `temperaturas = [22, 31, 27, 35, 19]`, use um `for` para descobrir a maior temperatura.

temperaturas = [22, 31, 27, 35, 19]

temperatura_inicial = 0

for temperatura in temperaturas:

    if temperatura_inicial < temperatura:
        temperatura_inicial = temperatura
        
print("a maior temperatura é:", temperatura_inicial)

# 2 - Palavras longas** - Com a lista `palavras = ["sol", "computador", "casa", "python", "janela"]`, conte quantas palavras têm mais de 5 letras (use `len`).

palavras = ["sol", "computador", "casa", "python", "janela"]

contador = 0

for palavra in palavras:

    print("total de caracteres: " + palavra + " - " + str(len(palavra)))

    if len(palavra) > 5:
        contador = contador + 1

print(contador)

#3 - Achar a Ana** - Com a lista `nomes = ["Ana", "Bruno", "Carla", "Ana"]`, use um `for` e um `if` para mostrar na tela o nome sempre que ele for igual a “Ana”.

nomes = ["Ana", "Bruno", "Carla", "Ana"]

for nome in nomes:

    if nome == "Ana":
        print(nome)

#4 - Achar o Pedro** - Com a lista `nomes = ["Lucas", "Pedro", "Julia", "Marcos"]`, use um `for` e um `if` para mostrar a mensagem `Achei o Pedro!` quando encontrar o nome “Pedro”.

nomes2 = ["Lucas", "Pedro", "Julia", "Marcos"]

for nome in nomes2:

    if nome == "Pedro":
        print("achei o pedro! 😁")

#5 - Contar Joãos** - Com a lista `nomes = ["João", "Maria", "João", "Paula"]`, use um `for`, um `if` e uma variável `contador` começando em 0 para contar quantas vezes “João” aparece e mostre o total no final.

nomes3 = ["João", "Maria", "João", "Paula"]

contador = 0

for nome in nomes3:
    
    if nome == "João":
        contador = contador + 1

print(contador)
