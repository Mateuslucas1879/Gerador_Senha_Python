import random
import string


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]


simbolo = int(input("Digite o numero de simbolos que voce quer:"))
letra = int(input("Digite o numero de letras que voce quer:"))
numeros = int(input("Digite o numero de numeros que voce quer:"))


lista_senha =[]

for char in range(1,simbolo+ 1):
    lista_senha.append(random.choice(symbols))

for char in range(1,letra +1):
    lista_senha.append((random.choice(letters)))

for char in range(1,numeros + 1 ):
    lista_senha.append((random.choice(numbers)))

    random.shuffle(lista_senha)

senha = ""
for char in lista_senha:
    senha += char


print(f"SUA SENHA GERADA FOI: {senha}")





