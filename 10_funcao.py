
#1 - Boas-vindas** - Crie a função `boas_vindas(nome)` que mostra "Bem-vindo ao curso, NOME!" (trocando NOME pelo nome recebido). Chame a função para 3 nomes diferentes.

def boas_vindas(nome):
    return "Boas vindas ao curso, " + nome + "!"

print(boas_vindas("Camila"))
print(boas_vindas("Vânia"))
print(boas_vindas("Heloísa"))

#2 - Dobro** - Crie a função `dobro(numero)` que **retorna** o número multiplicado por 2. Teste com 4 e com 10.

def dobro(numero):
    return numero * 2

print(dobro(50))