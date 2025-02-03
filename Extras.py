#Trabajos extras
# 1. Desarrollar un programa que cuente cuántos elementos únicos hay en una lista y los imprima.

def contar_elementos_unicos(lista):
    elementos_unicos = set(lista)
    return len(elementos_unicos), elementos_unicos


lista = input("Ingrese una palabras o numeros separados por un espacio: ").split()

cantidad, unicos = contar_elementos_unicos(lista)

print(f"Cantidad de elementos únicos: {cantidad}")
print(f"Elementos únicos: {unicos}")

#2. Encontrar la cadena que no es un palindromo

def es_palindromo(cadena):
    return cadena == cadena[::-1]

def encontrar_no_palindromo(lista):
    for palabra in lista:
        if isinstance(palabra,str) and not es_palindromo(palabra): #la funcion instance evalua que el "objeto" que esta evaluado es el
            print(f"Cadena que no es palíndromo: {palabra}")        #tipo especificado (palabra,"cadena"). Esto se puede quitar pero funciona como fitro
            return
    print("Todos son palíndromos")


lista = input("Ingrese las palabras separadas por espacio y saldra la primera que no es palindromo: ").split()
encontrar_no_palindromo(lista)

#3. Buscar cadenas que no tengan vocales 

def no_tiene_vocales(cadena):
    # Definir las vocales
    vocales = 'aeiouAEIOU'
    
    # Verificar si la cadena contiene alguna vocal
    for char in cadena:
        if char in vocales:
            return False
    return True

def buscar_cadenas_sin_vocales(lista):
    # Filtrar las cadenas que no tienen vocales
    cadenas_sin_vocales = [elemento for elemento in lista if isinstance(elemento, str) and no_tiene_vocales(elemento)]
    
    if cadenas_sin_vocales:
        print("Cadenas sin vocales:", cadenas_sin_vocales)
    else:
        print("No hay cadenas sin vocales.")


lista = ["hmm", "bcd", "xyz", "hola", "cielo", "ritmo"]
buscar_cadenas_sin_vocales(lista)



