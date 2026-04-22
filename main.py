import pandas as pd
from colorama import Fore, init

init(autoreset=True)

# --- Funções de Operação ---
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "erro"

# histórico simples
hist = []

while True:
    op = input("\nOperação (+ - * /) ou 'sair': ")
    if op == "sair":
        break
    
    # --- Contribuição Eiji: Tratamento de Erro caso não seja um número. ---
    try:
        a = float(input("Valor 1: "))
        b = float(input("Valor 2: "))
    except ValueError:
        print("Erro: Digite apenas números válidos!")
        continue

    # operações
    if op == "+":
        r = somar(a, b)
    elif op == "-":
        r = subtrair(a, b)
    elif op == "*":
        r = multiplicar(a, b)
    elif op == "/":
        r = dividir(a, b)
    else:
        print(Fore.RED + "Operação inválida")
        continue

    print(Fore.GREEN + f"Resultado: {r}")

    # salva no histórico
    hist.append([op, a, b, r])

# mostra histórico com pandas
df = pd.DataFrame(hist, columns=["Op", "A", "B", "Resultado"])
print("\nHistórico:")
print(df)
