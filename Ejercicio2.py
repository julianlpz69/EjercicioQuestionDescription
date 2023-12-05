# - Ordenar la subsecuencia en orden creciente.
# - Determinar la suma de las diferencias de los elementos de la subsecuencia.
# - Devolver la longitud de la subsecuencia más larga en la que esta suma sea par.

# Podemos ver que la longitud máxima posible de una subsecuencia válida es 4.

# Descripción de la función
# Complete la función findLongestSubsequence en el editor de abajo.
# FindLongestSubsequence tiene los siguientes parámetros:
# Int arr[n]: una matriz de enteros
# Devuelve
# Int: la longitud de la subsecuencia más larga descrita

from os import system;
from itertools import combinations

def todas_las_parejas(n,arraInt):
    
    elementos = sorted(arraInt)
    if len(elementos) <=2:
        return [[list(elementos)]]
    else:
        result = []
        for i in range(1,n):
            
            for pareja in combinations(elementos, i+1):
                result.append(pareja)
                
                suma = 0
                cantidad = 0
                
                for i in range (1, len(pareja)):
                    print(pareja)
                    x = i- 1
                    suma += pareja[i] - pareja[(x)]
                
                
                if suma % 2 == 0:
                    
                    if len(pareja) > cantidad:
                        cantidad = len(pareja)
                        print(cantidad)
                        
                
                for resto in todas_las_parejas(n,set(elementos)-set(pareja)):
                    caso = [list(pareja)]
                    caso.extend(resto)
    return cantidad



resultado = todas_las_parejas(4,[1,3,5,7])
system("clear")   
print(f"\n\nla longitud de la subsecuencia más larga descrita es : {resultado}")



