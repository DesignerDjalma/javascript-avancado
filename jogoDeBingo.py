

from typing import List
import random
import math


def embaralha_lista(lista: List[int], num_items_a_retornar: int) -> List[int]:
    """Apartir de uma lista base, retorna uma lista aleatoria, 
    com comprimento fornecido pelo usuario"""
    niar = num_items_a_retornar
    copia_lista_numeros = lista[:]
    random.shuffle(copia_lista_numeros)
    num_items = math.ceil(len(copia_lista_numeros)*niar)
    return copia_lista_numeros[:num_items]


class Jogador:

    """Responsavel por criar o Jogador."""

    numeros = []

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def marca(self):
        ...

    def faltantes(self):
        ...

    def imprime(self):
        print(f"Nome do Jogador: {self.nome}")
        print(f"Números ainda não marcados: {0}")



class Bingo:

    """Responsavel por criar o jogo do Bingo."""

    numeros: List[int] = []
    jogadores: List[Jogador] = []
    vencedores: List[Jogador] = []

    def __init__(self, qtd_nums: int) -> None:
        self.numeros = list(range(1, qtd_nums))
        random.shuffle(self.numeros)

    def adiciona_jogador(self, jogador: Jogador) -> None:
        """Adiciona Jogadores ao Bingo."""
        jogador.numeros = embaralha_lista(self.numeros, 30/100)
        self.jogadores.append(jogador)

        


def main():
    p1 = Jogador("Djalma")
    b = Bingo(10)
    b.adiciona_jogador(p1)
    print(b)
    print(b.numeros)
    print(b.jogadores[0].numeros)


if __name__ == "__main__":
    main()