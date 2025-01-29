#Desarrollar un programa que determine si en una lista se encuentra una cadena palîndrome
#Si la cadena existe debe imprimirla y si no existe debe imprimir "no existe"


def identificar_cad_palindrome(cad):
        return cad == cad[::-1]

def encontrar_pal_lis(lista):
    for palabra in lista:
        if identificar_cad_palindrome(palabra.lower()): #.lower es para ignorar si esta en mayusculas o minusculas
            return palabra
    return "no existe"

lista = input("Ingrese palabras separadas por un espacio o coma (,): ").split(" " or ",")

res = encontrar_pal_lis(lista)

if res != "no existe":
    print("Palindromo encontrado: ",res)
else:
    print(res)
     



