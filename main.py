import argparse
import subprocess
import sys

from utils.operacoes import Operacoes
from exceptions import OperationError, NumericValueError

def run_app() -> None:
    from interface import ask_operation, read_number, show_error, show_history, show_result

    hist = []

    while (op := ask_operation()).lower() != "sair":
        try:
            Operacoes.raise_if_operation_not_enabled(op)
            a = read_number("Valor 1: ")
            b = read_number("Valor 2: ")
            resultado = Operacoes.executar_operacao(op, a, b)
            show_result(resultado)
            hist.append([op, a, b, resultado])
        except (OperationError, NumericValueError) as e:
            show_error(e)
            continue

    show_history(hist)


def run_tests() -> int:
    return subprocess.call([sys.executable, "-m", "pytest", "tests", "-q"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculadora com histórico.")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Executa os testes automatizados da pasta tests.",
    )
    args = parser.parse_args()

    if args.test:
        return run_tests()

    run_app()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

    