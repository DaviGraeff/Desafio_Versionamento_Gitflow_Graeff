import pytest

from exceptions import OperationError
from utils.operacoes import Operacoes


def test_somar() -> None:
    assert Operacoes(2, 3).somar() == 5


def test_subtrair() -> None:
    assert Operacoes(8, 3).subtrair() == 5


def test_multiplicar() -> None:
    assert Operacoes(4, 3).multiplicar() == 12


def test_dividir() -> None:
    assert Operacoes(10, 2).dividir() == 5


def test_dividir_por_zero_retorna_erro() -> None:
    assert Operacoes(10, 0).dividir() == "erro"


def test_raise_if_operation_not_enabled_deve_lancar() -> None:
    with pytest.raises(OperationError):
        Operacoes.raise_if_operation_not_enabled("%")


def test_executar_operacao_soma() -> None:
    assert Operacoes.executar_operacao("+", 1, 2) == 3


def test_executar_operacao_subtracao() -> None:
    assert Operacoes.executar_operacao("-", 5, 2) == 3


def test_executar_operacao_multiplicacao() -> None:
    assert Operacoes.executar_operacao("*", 3, 4) == 12


def test_executar_operacao_divisao() -> None:
    assert Operacoes.executar_operacao("/", 9, 3) == 3


def test_executar_operacao_nao_suportada_deve_lancar() -> None:
    with pytest.raises(OperationError):
        Operacoes.executar_operacao("x", 2, 2)
