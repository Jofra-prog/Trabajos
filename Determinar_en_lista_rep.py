#Desarrollar un programa que determine si en una lista no existen elementos repetidos

def lista_sin_rep(listaev):
    print(len(set(listaev)))
    return len(listaev) == len(set(listaev))  # Convierte la lista en una lista sin repetidos y compara longitudes



listaev = input("Ingresa los elementos de la lista separados por espacios o  por una coma (,): ").split("" or ",")

if lista_sin_rep(listaev):
    print("La lista no tiene elementos repetidos.")
else:
    print("La lista contiene elementos repetidos.")
