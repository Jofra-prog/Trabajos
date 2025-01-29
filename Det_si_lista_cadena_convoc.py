#Desarrollar un programa que determine si en una lista se encuentra
#una cadena de caracteres con dos ○ más vocales. Si la cadena existe
#debe imprimirla y si no existe debe imprimir "no existe"

def con_voc(cad):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cad if letra in vocales)  # Cuenta vocales en la cadena con la funcion sum

def encontrar_cadena_con_vocales(list):
    for palabra in list: 
        if con_voc(palabra) >= 2:  # Verifica si tiene 2 o más vocales
            return palabra
    return "No existe"


lista = input("Ingresa palabras separadas por espacios o coma (,): ").split(" " or ",")

# Verificar si hay una palabra con al menos 2 vocales

res = encontrar_cadena_con_vocales(lista)
if res != "no existe":
    print("Cadena encontrada: ",res)
else:
    print(res)
     

