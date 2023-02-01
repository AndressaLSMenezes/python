# operacoes_matematicas/multiplicacao.py
from .soma import somar


def multiplicar(a, b):
    acumulador = 0
    for i in range(b):
        acumulador = somar(acumulador, a)

    return acumulador