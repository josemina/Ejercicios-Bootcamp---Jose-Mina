from cmu_graphics import *
import math

## Trabajando con Ovalos
"""Óvalo(200, 200, 200, 150, relleno='oro')
Arco(200, 200, 200, 150, 120, 90, relleno='azulMarino')
"""

#45 Grados
Rótulo('ánguloDeBarrido = 45', 100, 110, tamaño=16)
Óvalo(100, 175, 190, 100, relleno='oro')
Arco(100, 175, 190, 100, 90, 45, relleno='azulMarino')

#90 Grados
Rótulo('ánguloDeBarrido = 90', 300, 110, tamaño=16)
Óvalo(300, 175, 190, 100, relleno='oro')
Arco(300, 175, 190, 100, 90, 90, relleno='azulMarino')

#135 Grados
Rótulo('ánguloDeBarrido = 135', 100, 260, tamaño=16)
Óvalo(100, 325, 190, 100, relleno='oro')
Arco(100, 325, 190, 100, 90, 135, relleno='azulMarino')

#180 Grados
Rótulo('ánguloDeBarrido = 180', 300, 260, tamaño=16)
Óvalo(300, 325, 190, 100, relleno='oro')
Arco(300, 325, 190, 100, 90, 180, relleno='azulMarino')


##Trabajando con Circulos
"""Círculo(200, 200, 125, relleno='oro')
Arco(200, 200, 250, 250, 0, 90, relleno='azulMarino')"""





cmu_graphics.run()