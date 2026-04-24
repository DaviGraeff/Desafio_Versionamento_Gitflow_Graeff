from config import enabled_operations
from typing import Union
from exceptions import OperationError

class Operacoes:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def somar(self) -> float:
        """Retorna a soma de dois números."""
        return self.a + self.b

    def subtrair(self) -> float:
        """Retorna a diferença entre dois números."""
        return self.a - self.b

    def multiplicar(self) -> float:
        """Retorna o produto de dois números."""
        return self.a * self.b

    def dividir(self) -> Union[float, str]:
        """Retorna o quociente ou uma mensagem de erro em caso de divisão por zero."""
        return self.a / self.b if self.b != 0 else "erro"
    
    @staticmethod
    def raise_if_operation_not_enabled(op):
        if op not in enabled_operations:
            raise OperationError(f"Operação '{op}' não permitida.")
    
    @staticmethod
    def executar_operacao(op, a, b):
        operacao = Operacoes(a, b)

        de_para = {
            '+': operacao.somar,
            '-': operacao.subtrair,
            '*': operacao.multiplicar,
            '/': operacao.dividir
        }

        func = de_para.get(op)

        if not func:
            raise OperationError(f"Operação '{op}' não suportada.")
        
        return func()