import pandas as pd
from colorama import Fore, init

init(autoreset=True)

# --- Funções de Operação ---
def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "erro"

# Mapeamento de operações (Dicionário)
operacoes = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir
}

hist = []

while True:
    op = input("\nOperação (+ - * /) ou 'sair': ")
    if op.lower() == "sair":
        break

    if op not in operacoes:
        print(Fore.RED + "Operação inválida")
        continue

      # --- Contribuição Eiji: Tratamento de Erro caso não seja um número. ---
    try:
        a = float(input("Valor 1: "))
        b = float(input("Valor 2: "))
    except ValueError:
        print("Erro: Digite apenas números válidos!")
        continue
        
        # execução dinâmica da função através da chave do dicionário
        r = operacoes[op](a, b)
        
        print(Fore.GREEN + f"Resultado: {r}")
        hist.append([op, a, b, r])
    except ValueError:
        print(Fore.RED + "Erro: Digite apenas valores numéricos.")

# mostra histórico com pandas
if hist:
    df = pd.DataFrame(hist, columns=["Op", "A", "B", "Resultado"])
    print("\nHistórico:")
    print(df)
    