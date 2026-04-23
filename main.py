import pandas as pd
from colorama import Fore, init
from typing import Union

init(autoreset=True)

# --- Funções com Type Hints e Docstrings ---

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre dois números."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b

def dividir(a: float, b: float) -> Union[float, str]:
    """Retorna o quociente ou uma mensagem de erro em caso de divisão por zero."""
    return a / b if b != 0 else "erro"

# Mapeamento de operações
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

if hist:
    df = pd.DataFrame(hist, columns=["Op", "A", "B", "Resultado"])
    print("\nHistórico:")
    print(df)

    # comentário simulando um erro a ser corrigido no HOTFIX
    