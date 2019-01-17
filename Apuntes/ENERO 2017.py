from typing import *

# EXAMEN ENERO 2017
# EJERCICIO 1 - VORACES (SIN COTAS)
# a)
def menor_numero_intervalos(puntos: List[float], a: float) -> int:
    vectorOrdenado = sorted(puntos) #De menor a mayor
    pivote = vectorOrdenado[0]
    limite = pivote + a
    numIntervalos = 0

    for elemAct in vectorOrdenado:
        if elemAct > limite:
            pivote = elemAct
            limite = pivote + a
            numIntervalos += 1

    return numIntervalos

# b) ???

# c) costes, en general será nLogN, ya que al ordenar ya es LogN, y al recorrer todos los elementos, pues es por N

# EJERCICIO 2 REDUCE Y VENCERAS
# SIN SEGUIR EL ESQUEMA
def solve(v: List[int], numero: int) -> int:
    pivote = 0
    izquierda = 0
    derecha = len(v) - 1
    apariciones = 0
    listaIzquierda = []
    listaDerecha = []

    while izquierda != derecha and v[pivote] != numero:
        pivote = (izquierda + derecha + 1) // 2
        if v[pivote] >= numero:
            derecha = pivote
        else:
            izquierda = pivote

    print(pivote)
    listaIzquierda = v[0: pivote]
    listaDerecha = v[pivote + 1: len(v)]

    indiceCorteIzquierdo = buscarNumero(listaIzquierda, numero - 1, numero)
    indiceCorteDerecho = buscarNumero(listaDerecha, numero + 1, numero) + pivote + 1
    apariciones = (indiceCorteDerecho - indiceCorteIzquierdo) - 1

    print(indiceCorteIzquierdo)
    print(indiceCorteDerecho)

    return apariciones

def buscarNumero(lista: List[int], numero: int, numeroOriginal: int) -> int:
    pivote = 0
    izquierda = 0
    derecha = len(lista) - 1

    while (derecha - izquierda) > 1:
        pivote = (izquierda + derecha + 1) // 2

        if lista[pivote] >= numero:
            derecha = pivote
        else:
            izquierda = pivote

    if lista[izquierda] != numeroOriginal:
        return izquierda
    else:
        return derecha

# EJERCICIO 3
# a) X = {(x_0, x_1...x_S-1) € (Y)}
# Y = {(y_0, y_1....y_N-1) € (0,1)^N | SUMATORIO 0<=i<n y_i*C_i = (SUMATORIO C_i/S)}

# b)
C = [1,2,3,4,5,6]
S = 2

class ParticionesConjuntoPS(PartialSolution):
    def __init__(self, sum: int, decisiones: List[int], indiceInicio: int):
        self.sumaDeseada = sum
        self.decisiones = decisiones
        self.indiceInicio = indiceInicio

    def is_solution(self) -> bool:
        suma = 0

        for i in range(len(self.decisiones)):
            suma += self.decisiones[i] * C[i]

        return suma == self.sumaDeseada


    def get_solution(self) -> solution:
        return self.decisiones


    def succesors(self) -> IEnumerable<PartialSolution>:
        for i in range(self.indiceInicio, len(C)):
            self.decisiones[i] = 1
            yield ParticionesConjuntoPS(self.sumaDeseada, self.decisiones, i+1)
            self.decisiones[i] = 0

# Recorremos los indices del conjunto C a partir del indice de inicio que recibe en el constructor
# generamos una nueva solucion parcial indicando que cogemos ese elemento del conjunto C
# y luego cuando hayamos procesado dicho estado, deshacemos el haber cogido dicho elemento.

# C) costes

# D)

def main():
    suma = #suma de los elementos de C / S

    initial_ps = ParticionesConjuntoPS(suma, [0]*len(C), 0)
    subconjuntos = []

    for subconjunto in BacktrackingSolver.solve(initial_ps):
        subconjuntos.append(subconjunto)

    if len(subconjuntos) == S:
        print(subconjuntos)
    else:
        print("No hay soluciones")

# EJERCICIO 5
# a) apartado 1
# X = {((t_0, p_0), (t_1, p_1)....(t_N-1, p_N-1)) € (N,N) | SUMATORIO 0<=1<N t_i+p_i <= M}

# a) apartado 2
# f(t_0, p_0), (t_1, p_1)...(t_i, p_i) = SUMATORIO 0<=i<N nota_estimada(i, t_i, p_i)

# b)
def C(i: int, m: int) -> Tuple[int, int, int, int]:
    if (i == 0 and m == 0):
        return (0, -1,-1, -1)
    elif (i==0 and m > 0) or (i > 0 and m <l(i)):
        return (float("inf"), -1, -1, -1)
    elif (i > 0 and m >= l(i)):
        clave = (i, m)

        if clave not in dic:
            tuplaMin = (float("inf"), -1, -1, -1)

            for j in range(1, min(abs(m/l(i)), s(i))):
                m1 = m - j * l(i)
                tuplaNueva = (C(i-1, m1) + j * p(i), i-1, m1, j)

                if tuplaNueva[0] < tuplaMin[0]:
                    tuplaMin = tuplaNueva

            dic[clave] = tuplaMin

        return dic[clave]
    else:
        return (floa(inf), -1, -1, -1)

def main():
    camino = C(N, M)
    piezas = []
    coste = camino[0]

    while camino[1] != -1 and camino[2] != -1:
        piezas.append(camino[3])
        clave = (camino[1], camino[2])

        camino = dic[clave]

    piezas.reverse()

    print("Coste total: {0}, piezas: {1}".format(coste, piezas))


# JUNIO 2017

# EJERCICIO 1 - VORACES
# A)
def mejorArticulo(K: int, P: list[int], V: list[float]) -> list[int]:
    articulosOrdenados = sorted(range(len(V)), key = lambda i: -V[i]/P[i])
    listaAux = []
    pesoDisponible = K

    for i in articulosOrdenados:
        if P[i] <= pesoDisponible:
            listaAux.append(i)
            pesoDisponible -= P[i]

    return listaAux

# B: reordenar según el ratio de valor/peso, iterar sobre los elementos según los indices
# reordenados, y añadirlos al a lista auxiliar mientras quepan.


# EJERCICIO 2
# A) X = {(x_0, x_1...x_n-1) € [0, 1]^N | SUMATORIO 0<=i<n x_i*C_i = S}
# B)
class SubconjuntosStateSpace(PartialSolution):
    def __init__(self, C: list[int], S: int, decisiones: list[int]):
        self.C = C
        self.S = S
        self.decisiones = decisiones

    def is_solution(self)-> bool:
        suma = 0

        for i in range(len(self.decisiones)):
            suma += self.decisiones[i] * C[i]

        return suma == self.S

    def get_solution(self) -> Solution:
        return self.decisiones

    def successors(self) -> IEnumerable<PartialSolution>:
        n = len(C)
        decisionesTomadas = len(self.decisiones)

        if decisionesTomadas < n:
            for i in range(2):
                self.decisiones.append(i)
                yield SubconjuntosStateSpace(self.C, self.S, self.decisiones)
                self.decisiones.pop()
# C) el coste es O(2), o sea, costante porque siempre realizamos dos iteraciones
# D)

def main():

    initial_ps = SubconjuntosStateSpace(C, S, [])
    cont = 0

    for solucion in BacktrackingSolver.solve(initial_ps):
        cont +=1

    print(cont)

# EJERCICIO 4 - REDUCE Y VENCERAS
# NO SIGUE ESQUEMA ALGORITMICO - RECURSIVA
def potencia(a: int, n: int) -> int:
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        aAux = potencia(a * a, n // 2)

        if n % 2 == 1:
            aAux = aAux * a

        return aAux


# NO SIGUE ESQUEMA ALGORITMICO - ITERATIVA
def potencia1(a: int, n: int) -> int:
    resultado = 1
    base = a

    while n > 1:
        resultado = base * base

        if n % 2 == 1:
            resultado *= base

        n = n // 2
        base = base * base

    if n == 1:
        resultado *= a

    return resultado

class PotenciaClase(IDecreaseAndConquerProblem):
    def __init(self, a: int, n: int):
        self.a = a
        self.n = n

    def is_simple(self) -> bool:
        return self.n <= 1

    def trivial_solution(self) -> Solution:
        if self.n == 0:
            return 1
        if self.n == 1:
            return self.a

    def decrease(self) -> IDecreaseAndConquerProblem:
        return PotenciaClase(self.a*self.a, self.n//2)

    def process(self, s: solution) -> solution:
        if self.n % 2 == 1:
            return s * self.a
        else:
            return s

# EJERCICIO 5
# apartado a
X = {(x_0, x_1...x_n-1) € [R] | SUMATORIO 0<=i<N x_i <= Q}

# apartado b)
f((x_0, x_1...x_n-1)) = SUMATORIO 0<=i<n B(i, x_i)

# EJERCICIO 6
# Apartado A)
def L(q: int, n: int) -> Tuple(float, int, int, int):
    if q == 0 and n == 0:
        return (0, -1, -1, -1)
    elif q > 0 and n == 0:
        return (float("inf"), -1, -1, -1)
    else:
        clave = (q, n)

        if clave not in dic:
            dic[clave] = (float("inf"),-1,-1, -1)

            for i in range(0, min(m[n-1], abs(q/v[n-1]))):
                q2 = q-i*v[n-1]
                dic[clave] = min(dic[clave], (L(q2, n-1)+ i * w[n-1], q2, n-1, i))

        return dic[clave]

dic = {}

def main():
    camino = L(Q, len(v))
    desglose = []
    peso = camino[0]

    while camino[1] != -1 and camino[2] != -1:
        desglose.append(camino[3])
        clave = (camino[1], camino[2])
        camino = dic[clave]

    desglose.reverse()

    print(desglose)
    print(peso)