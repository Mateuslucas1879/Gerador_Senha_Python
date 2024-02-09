import random
import string
import tkinter as tk
from tkinter import ttk

# Função para gerar a senha
def gerar_senha():
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    try:
        num_simbolos = int(entry_simbolos.get())
        num_letras = int(entry_letras.get())
        num_numeros = int(entry_numeros.get())
    except ValueError:
        num_simbolos = 0
        num_letras = 0
        num_numeros = 0

    lista_senha = []

    for _ in range(num_simbolos):
        lista_senha.append(random.choice(simbolos))

    for _ in range(num_letras):
        lista_senha.append(random.choice(letras))

    for _ in range(num_numeros):
        lista_senha.append(random.choice(numeros))

    random.shuffle(lista_senha)

    senha = ''.join(lista_senha)
    label_senha.config(text=f"SUA SENHA GERADA FOI: {senha}")

# Configuração da interface
root = tk.Tk()
root.title("Gerador de Senhas")

# Estilo
style = ttk.Style()
style.theme_use('clam')

# Define o esquema de cores
cor0 = "#444466"
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul
cor3 = "#f05a43"  # vermelha

# Define as cores dos widgets
root.configure(bg=cor0)
style.configure('TButton', foreground=cor1, background=cor2)
style.configure('TLabel', foreground=cor1, background=cor0)

# Frame para organização dos widgets
frame = ttk.Frame(root, padding="20")
frame.pack(padx=10, pady=10)

# Widgets
ttk.Label(frame, text="Número de símbolos:", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w")
entry_simbolos = ttk.Entry(frame)
entry_simbolos.grid(row=0, column=1)

ttk.Label(frame, text="Número de letras:", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w")
entry_letras = ttk.Entry(frame)
entry_letras.grid(row=1, column=1)

ttk.Label(frame, text="Número de números:", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w")
entry_numeros = ttk.Entry(frame)
entry_numeros.grid(row=2, column=1)

button_gerar = ttk.Button(frame, text="Gerar Senha", command=gerar_senha)
button_gerar.grid(row=3, columnspan=2, pady=10)

label_senha = ttk.Label(frame, text="", font=("Helvetica", 12), wraplength=300)
label_senha.grid(row=4, columnspan=2)

# Rodar a aplicação
root.mainloop()
