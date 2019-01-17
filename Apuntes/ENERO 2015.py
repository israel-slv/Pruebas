from typing import *

# ENERO 2015
# EJERCICIO 1 - REDUCE Y VENCERAS
def busca_indice_solitario(v: list[int], i: int, j: int) -> int:
    if i > j:
        return -1
    if v[i] != v[i+1]:
        return i
    if v[j] != v[j-1]:
        return j
    else:
        return busca_indice_solitario(v, i+2, j-2)

# EJERCICIO 2 - BUSQUEDA RETROCEDO
# a)

class SumaDosEnterosPS(PartialSolutionWIthVisitedControl):
    def __init__(self, C: List[int], decisionesA: List[int], decisionesB: List[int], A: int, B:int):
        self.C = C
        self.decisionesA = decisionesA
        self.decisionesB = decisionesB
        self.A = A
        self.B = B

    def is_solution(self) -> bool:
        return sum(self.decisionesA) == self.A and sum(self.decisionesB) == self.B

    def get_solution(self) -> Solution:
        return (self.decisionesA, self.decisionesB)

    def successors(self) -> IEnumerable.....:
        for i in range(len(C)):
            aux = self.C[i]

            self.decisionesA.append(aux)
            del self.C[i]
            yield(SumaDosEnterosPS)
            self.decisionesA.pop()

            self.decisionesB.append(aux)
            yield (SumaDosEnterosPS)
            self.C.append(aux)
            self.decisionesB.pop()

    def state(self) -> state:
        return (sum(self.decisionesA), sum(self.decisionesB))

    #b)

#c)
def main():
    initial_ps = SumaDosEnterosPS(C, [], [], A, B)
    encontrado = False

    for solucion in bt(initial_ps):
        print(solucion)
        encontrado = True
        break

    if not encontrado:
        print("No se han encontrado soluciones.")

# EJERCICIO 4 - VORACES
def posicionGuardas(X: List[float], L: float, D: float) -> List[float]:
    cuadrosOrdenados = sorted(range(len(X)), key = lambda i: X[i+1]-X[i] if i != len(X)-1 else L-X[i])
    posicionesGuardas = []
    espacioDisponible = 2 * D

    for i in cuadrosOrdenados:
        siguienteCuadro = X[i+1]-X[i] if i != len(X)-1 else L-X[i]

        if espacioDisponible >= siguienteCuadro:
            espacioDisponible -= siguienteCuadro
            posicionesGuardas.append(siguienteCuadro/2)
        else:
            espacioDisponible = 2 * D - siguienteCuadro

    return posicionesGuardas