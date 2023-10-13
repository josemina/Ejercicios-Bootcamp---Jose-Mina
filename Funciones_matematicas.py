from cmu_graphics import *


# Calcular el valor absoluto de un número
"""numero = -78
valor_absoluto = abs(numero)
print(valor_absoluto)  # Salida: 78"""


# Calcular la potencia de un número
"""base = 20
exponente = 3
resultado = pow(base, exponente)
print(resultado)  # Salida: 8"""


# Redondear un número a un número específico de decimales
"""numero = 9999.99
redondeado = round(numero, 2)
print(redondeado)"""


# Encontrar el valor máximo y mínimo en una lista
"""
numeros = (5, 10, 2, 8)
maximo = max(numeros)
minimo = min(numeros)
print(maximo)  # Salida: 10
print(minimo)  # Salida: 2
"""
#Funciones de CMU

#distancia
"""c = Círculo(200, 140, 20, relleno='cian')
objetivo = Círculo(200, 200, 20, relleno='oro')

def enRatónMovido(x, y):
    c.centroX = x
    c.centroY = y
    distanciaAObjetivo = distancia(x, y, 200, 200)
    if (distanciaAObjetivo < 75):
        c.relleno = 'cian'
    else:
        c.relleno = 'rosado'"""
    

#angulo

"""flecha = Línea(200, 250, 200, 200, finalDeFlecha=Verdadero)
angulo = Rotulo(0, 0, 10)
def enRatónMovido(x, y):
    flecha.rotarÁngulo = ánguloA(flecha.centroX, flecha.centroY, x, y)

    angulo.valor = int(flecha.rotarÁngulo)
    angulo.centroX = x
    angulo.centroY = y - 10"""


#obtenerPuntoEnDir
"""flecha = Línea(200, 250, 200, 200, finalDeFlecha=Verdadero)
Círculo(flecha.centroX, flecha.centroY, 75, relleno=None, borde='grisClaro', anchuraDeBorde=1)

def enPaso():
     flecha.rotarÁngulo += 2

def enTeclaPresionada(tecla):
    x, y = obtenerPuntoEnDir(flecha.centroX, flecha.centroY, flecha.rotarÁngulo, 30)
    Rotulo("Punto X: ", x, y)
    Rotulo(int(x), x + 35, y)
    Rotulo("Punto Y: ", x, y+10)
    Rotulo(int(y), x +35, y+10)
    #Círculo(x, y, 3)
    print(f"El punto {flecha.centroX}, {flecha.centroY} con un angulo de {int(flecha.rotarÁngulo)}, a una distancia de 75 es: {int(x)}, {int(y)}")
"""
cmu_graphics.run()