#Desarrollar un programa que determine si una lista es palíndrome
#Una lista es palíndrome si el elemento en la posición i es el mismo de
#la posición n-1- i con n la longitud de la lista

def es_lista_palindroma(list):
    return list == list[::-1]  # Compara la lista con su versión invertida


lista = input("Ingresa los elementos de la lista separados por espacios: ").split()

# Verificar si la lista es palíndroma
if es_lista_palindroma(lista):
    print("La lista es palíndroma.")
else:
    print("La lista no es palíndroma.")