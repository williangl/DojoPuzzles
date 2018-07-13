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

#amig1 = [1, 2]
#amig2 = [1, 2]
#amig3 = []


def amigos(amig1: list, amig2: list) -> str:
    """sdfdsfsdfd."""
    if amig1 == amig2:
        return 'Dois amigos não podem viver na mesma localização'
    
