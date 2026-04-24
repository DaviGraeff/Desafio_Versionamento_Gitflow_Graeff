import pandas as pd
from colorama import Fore, init

from config import show_result as show_result_enabled
from exceptions import NumericValueError

init(autoreset=True)


def ask_operation() -> str:
    return input("\nOperação (+ - * /) ou 'sair': ")


def read_number(prompt: str) -> float:
    try:
        return float(input(prompt))
    except ValueError as exc:
        raise NumericValueError("Digite apenas valores numéricos.") from exc


def show_error(error: Exception) -> None:
    print(Fore.RED + f"Erro: {error}")


def show_result(result) -> None:
    if show_result_enabled:
        print(Fore.GREEN + f"Resultado: {result}")


def show_history(history: list) -> None:
    if history:
        df = pd.DataFrame(history, columns=["Op", "A", "B", "Resultado"])
        print("\nHistórico:")
        print(df)
