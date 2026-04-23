import pytest

from exceptions import NumericValueError
from interface import ask_operation, read_number, show_error, show_history, show_result


def test_ask_operation(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "+")
    assert ask_operation() == "+"


def test_read_number_valido(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "10.5")
    assert read_number("Valor: ") == 10.5


def test_read_number_invalido_lanca_excecao(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "abc")
    with pytest.raises(NumericValueError):
        read_number("Valor: ")


def test_show_error_exibe_mensagem(capsys) -> None:
    show_error(ValueError("falha"))
    captured = capsys.readouterr()
    assert "Erro: falha" in captured.out


def test_show_result_exibe_quando_habilitado(monkeypatch, capsys) -> None:
    import interface

    monkeypatch.setattr(interface, "show_result_enabled", True)
    show_result(42)
    captured = capsys.readouterr()
    assert "Resultado: 42" in captured.out


def test_show_result_nao_exibe_quando_desabilitado(monkeypatch, capsys) -> None:
    import interface

    monkeypatch.setattr(interface, "show_result_enabled", False)
    show_result(42)
    captured = capsys.readouterr()
    assert "Resultado" not in captured.out


def test_show_history_exibe_tabela(capsys) -> None:
    history = [["+", 1.0, 2.0, 3.0]]
    show_history(history)
    captured = capsys.readouterr()
    assert "Histórico:" in captured.out
    assert "Resultado" in captured.out


def test_show_history_com_lista_vazia_nao_exibe(capsys) -> None:
    show_history([])
    captured = capsys.readouterr()
    assert captured.out == ""


def test_perfect_math() -> None:
    assert 2 + 2 == 5
