from cmu_graphics import *
import math
"""contador = Rótulo(0, 200, 200, tamaño=100)

def enPaso():
    contador.valor += 1

def enTeclaPresionada(tecla):
    if tecla == "s":
        app.detener()"""


## Animaciones
"""estrella_uno = Estrella(100, 200, 100, 5, relleno='oro')
estrella_dos = Estrella(300, 200, 100, 5, relleno='oro')

def enPaso():
    estrella_uno.rotarÁngulo += 1
    estrella_dos.rotarÁngulo -= 1"""


## Pasos por segundo
"""estrella = Estrella(200, 200, 100, 5, relleno='oro')

def enPaso():
  estrella.rotarÁngulo += 1

def enTeclaPresionada(tecla):
    if (tecla == 'r'):
        app.pasosPorSegundo = 90
    elif (tecla == 'n'):
        app.pasosPorSegundo = 30
    elif (tecla == 'd'):
        app.pasosPorSegundo = 5"""


## Movimientos

#Recto e Inverso
"""c1 = Círculo(200, 200, 20, relleno='rojo')
c2 = Círculo(200, 100, 20, relleno='azulMarino')

def enPaso():
    c2.centroY += 5
    c1.centroY -= 5"""

#Usando dx
"""c1 = Círculo(50, 150, 20, relleno='azulMarino')
c1.dx = 5
c2 = Círculo(350, 250, 20, relleno='oro')
c2.dx = -5
def enPaso():
    c1.centroX += c1.dx
    c2.centroX += c2.dx"""

#Movimiento Acotado
"""
c = Círculo(200, 200, 20, relleno='azulMarino')
c.dy = 5

def enPaso():
    c.centroY += c.dy
    if (c.inferior > 400):
        c.inferior = 400"""

#Movimiento Diagonal
"""c1 = Círculo(50, 50, 20, relleno='azulMarino')
c1.dx = 10
c1.dy = 5

c2 = Círculo(350, 350, 20, relleno='oro')
c2.dx = -10
c2.dy = -5

def enPaso():
    c1.centroX += c1.dx
    c2.centroX += c2.dx
    c1.centroY += c1.dy
    c2.centroY += c2.dy"""

#Moviento Rebote

"""c = Círculo(200, 150, 20, relleno='azulMarino')
c.dx = 10
c.dy = 20
app.pasosPorSegundo = 120

def enPaso():
    c.centroY += c.dy
    if ((c.superior < 0) or (c.inferior > 400)):
        c.dy = -c.dy"""

"""c = Círculo(200, 150, 20, relleno='azulMarino')
c.dx = 35
c.dy = 20
app.pasosPorSegundo = 80

def enPaso():
    c.centroY += c.dy
    c.centroX += c.dx
    if ((c.superior < 0) or (c.inferior > 400)):
        c.dy = -c.dy
    if ((c.izquierda < 0) or (c.derecha > 400)):
        c.dx = -c.dx"""

#Movimiento Parabolico
"""app.pasosPorSegundo = 60

c = Círculo(0, 300, 20, relleno='azul')
c.dx = 10
c.dy = 20
def enPaso():
    c.centroX += c.dx
    if c.centroX < 200 :
        c.dy-=1
        c.centroY -= c.dy
    else:
        c.centroY += c.dy
        c.dy+=4"""




cmu_graphics.run()