"""Mundo pequeno.

Como um programador muito popular, você conhece muitas pessoas em seu país.
Como você viaja muito, você decidiu que seria muito útil de ter um programa que
te dissesse quais de seus amigos estão mais próximos baseado em qual amigo você
está atualmente visitando.

Cada um de seus amigos vive em uma posição específica (latitude e longitude) -
para os propósitos deste problema o mundo é plano e a latitude e a longitude
são coordenadas cartesianas em um plano - e você consegue identificá-los de
alguma maneira. Também cada amigo mora em uma posição diferente
(dois amigos nunca estão na mesma latitude e longitude).

Escreva um programa que receba a localização de cada um dos seus amigo e,
para cada um deles, você indique quais são os outros três amigos mais
próximos a ele.
"""
from unittest import TestCase, main

import mundopequeno


class TesteMundo(TestCase):
    """Classe de teste mundo pequeno."""

    def testa_posicao_dos_amigos_sao_iguais(self):
        """Função para testar posição iguais."""
        amg1 = [1, 2]
        amg2 = [1, 2]
        esperado = 'Dois amigos não podem viver na mesma localização'
        self.assertEqual(mundopequeno.amigos(amg1, amg2), esperado)


main()
