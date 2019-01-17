from typing import *

v = [1,1,2,2,3,4,4,5,5,6,6,7,7,8,8]

def busca_indice_solitario(v: List[int], i: int, j: int) -> int:
    if i > j:
        return -1
    if v[i] != v[i+1]:
        return i
    if v[j] != v[j-1]:
        return j
    else:
        return busca_indice_solitario(v, i+2, j-2)


print(busca_indice_solitario(v, 0, len(v)-1))
print(v[busca_indice_solitario(v, 0, len(v)-1)])