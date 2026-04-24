from utils.operacoes import Operacoes
from exceptions import OperationError, NumericValueError
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

    