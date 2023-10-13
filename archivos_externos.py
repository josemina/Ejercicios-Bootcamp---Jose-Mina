#Abrir y/o crear archivos en modo escritura

"""archivo = open("archivo.txt", "w")"""

# Escribir en un archivo
"""frase = "Estupenda jornada de Bootcamp hoy se hacen proyectos\n"
archivo.write(frase)
texto = input("Ingrese su nombre")
archivo.write(texto)

#Cerrar un archivo
archivo.close()"""

#Leer un archivo completo
"""archivo = open("archivo.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)"""


#Leer linea a linea un archivo
"""archivo = open("archivo.txt", "r")
linea_texto = archivo.readlines()
archivo.close()
print(linea_texto)
print(linea_texto[1])"""


#Añadir una nueva linea con append
"""archivo = open("archivo.txt", "a")
archivo.write("\n Los proyectos de hoy seran de otro nivel")
archivo.write("\n Hoy se hacen muchos proyectos")
archivo.close()
"""
#Lectura posicionando el puntero
"""archivo = open("archivo.txt", "r")

archivo.seek(7)
print(archivo.read())"""
#archivo.seek(0)
#print(archivo.read())

#print(archivo.read(11))
#print


#Lectura y escritura 
"""archivo = open("archivo.txt", "r+")
archivo.write("Comienzo del texto")
print(archivo.readlines())"""


"""archivo = open("archivo.txt", "r+")
lista_texto = archivo.readlines()
lista_texto[1] = "Linea incluida desde afuera \n"
archivo.seek(0)
archivo.writelines(lista_texto)

archivo.close()"""