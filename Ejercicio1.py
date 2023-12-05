# Reto 5: Descripción de la pregunta
# Sam y Kelly son compañeros de programación. Kelly se propone practicar más, ya que Sam es inicialmente un jefe.
# Cada uno resuelve un número de problemas al día. Halla el número mínimo de días para que Kelly haya resuelto más problemas que Sam. Si Kelly no puede superar retum -1.
# Ejemplo
# SamDiario = 3
# KellyDiario = 5
# Diferencia = 5
# Inicialmente, Sam ha resuelto más problemas de diferencias que Kelly. Cada día, resuelven problemas samDaily y kellyDaily cada uno.

# Día 1: samSolved = diferencia + samDaily = 5 + 3 = 8
# kellySolved = kellyDaily = 5
# Día 2: samSolved = 8 + 3 = 11
# kellySolved = 5 + 5 = 10
# Día 3: samSolved = 11 + 3 = 14
# kellySolved = 10 + 5 = 15
# Sam lleva 5 problemas de ventaja a Kelly y resuelven 3 y 5 problemas al día. Sam estará por delante por sólo
# 3 después del primer día, 1 después del segundo, y Kelly pasará a Sam el día 3.
# Descripción de la función
# Complete la función minNum en el editor de abajo.
# MinNum tiene los siguientes parámetros:
# SamDaily: Número de problemas que Sam resuelve en un día
# KellyDaily: Número de problemas que Kelly resuelve en un día
# Diferencia: Número de problemas que Sam isa cabeza para empezar
# Devuelve
# Int: el número mínimo de días que necesita Kelly para superar a Samm, o -1 si es imposible
# Restricciones
# - 1 ≤ samDaily, kellyDaily ≤ 100
# - 0 ≤ diferencia ≤ 100

from os import system;


def minNum(KellyDaily, SamDaily, diferencia  ):
    if SamDaily > KellyDaily or SamDaily == KellyDaily and diferencia > 0:
        return print("Imposible que kelly alcance a Sam -1")
    
    else:
        cerrar = 0
        dias = 0
        Sam = diferencia
        Kelly = 0
        while cerrar == 0:
            Sam += SamDaily
            Kelly += KellyDaily
            dias += 1
        
            if Kelly >= Sam:
                cerrar = 1
        
        return print(f"Kelly tardara almenos {dias} dias en alcanzar a Sam")
            
system("clear")    
minNum(5,3,5)