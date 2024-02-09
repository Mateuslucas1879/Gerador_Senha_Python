import random
import string
import tkinter as tk


# CORES
cor0 = "#444466"
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul
cor3 = "#f05a43"  # vermelha
# DEFINIR COR DE FUNDO
fundo = cor0
#FUNÇAO COM O SISTEMA PRINCIPAL
def gerar_senha():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç', '`', '/', '|',
               'ª', 'º', '¿', ]

    try:
        num_simbolos = int(entry_simbolos.get())
        num_letras = int(entry_letras.get())
        num_numeros = int(entry_numeros.get())
    except ValueError:
        # Se um dos campos de entrada estiver vazio, define o número correspondente como zero
        num_simbolos = 0
        num_letras = 0
        num_numeros = 0

    lista_senha = []

    for char in range(1,num_simbolos + 1):
        lista_senha.append(random.choice(symbols))

    for char in range(1,num_letras  + 1):
        lista_senha.append((random.choice(letters)))

    for char in range(1,  num_numeros  + 1):
        lista_senha.append((random.choice(numbers)))

    random.shuffle(lista_senha)

    senha = ''.join(lista_senha)
    label_senha.config(text=f"SUA SENHA GERADA FOI: {senha}")

# TELA PRINCIPAL CRIAÇÃO DA INTERFACE
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry('300x360')
root.configure(bg=fundo)

#SIMBOLOS
label_simbolos = tk.Label(root, text="Digite o número de símbolos que você quer:")
label_simbolos.pack()
entry_simbolos = tk.Entry(root)
entry_simbolos.pack()

# LETRAS
label_letras = tk.Label(root, text="Digite o número de letras que você quer:")
label_letras.pack()
entry_letras = tk.Entry(root)
entry_letras.pack()

# NUMEROS
label_numeros = tk.Label(root, text="Digite o número de números que você quer:")
label_numeros.pack()
entry_numeros = tk.Entry(root)
entry_numeros.pack()

# GERADOR
button_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
button_gerar.pack()

label_senha = tk.Label(root, text="")
label_senha.pack()

# RODAR PROJETO
root.mainloop()