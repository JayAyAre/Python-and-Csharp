"""
https://www.youtube.com/watch?v=5AnY8E8f_p4

Desarrolla un programa que solicite la longitud de una lista por teclado
Esta lista unicamente contendra numeros enteros

De acuerdo a la longitud. Se solicitara cada uno de los elementos
y se iran introduciendo uno a uno en la lista.

Finalmente, se imprimira la lista con todos los elementos, y a su vez
la suma de todos los elementos de la lista.

"""

print("".center(100, "="))
print("SUMAR VALORES DE UNA LISTA".center(100))
print("".center(100, "="), end="\n\n")

len_lista = int(input("Ingrese la longitud de la lista: "))
lista = []

for i in range(0, len_lista, 1):
    lista.append(int(input("Ingrese el numero de la posicion " + str(i) + ": ")))

suma = sum(lista)
print("La lista es: ", lista)
print("La suma de todos los elementos es: ", suma)

