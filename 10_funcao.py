
# 1 - Boas-vindas** - Crie a função `boas_vindas(nome)` que mostra "Bem-vindo ao curso, NOME!" (trocando NOME pelo nome recebido). Chame a função para 3 nomes diferentes.

def boas_vindas(nome):
    return "Boas vindas ao curso, " + nome + "!"

print(boas_vindas(input("Informe o seu nome: ")))
print(boas_vindas("Camila"))
print(boas_vindas("Vânia"))
print(boas_vindas("Heloísa"))

#2 - Dobro** - Crie a função `dobro(numero)` que **retorna** o número multiplicado por 2. Teste com 4 e com 10.

def dobro(numero):
    return numero * 2

print(dobro(50))

##############################################################

def teste():
    return
print("teste")

teste

def mult04():

    numero01 = int(input("informe um número p multiplicar por 4: "))
    return print(numero01 * 4)

mult04()

def dividir (a, b):
    try:
        return a / b
    except:
        return "não foi possível realizar a divisão."

print(dividir(10, 0))

try:
    numero = int(input("informe um número: "))
    print(numero)
except:
    print("erro: informe um número!")