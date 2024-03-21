# Algoritmo de complejidad líneal

import random
import time

# Función para encontrar el máximo elemento en una lista
def encontrar_maximo(lista):
    maximo = lista[0]
    for elemento in lista[1:]:
        if elemento > maximo:
            maximo = elemento
    return maximo

# Solicita al usuario el tamaño del array
tamanio_array = int(input("Ingresa el tamaño del array: "))

# Generar una lista aleatoria de tamaño especificado por el usuario
lista = [random.randint(0, 100000) for _ in range(tamanio_array)]

# Medir el tiempo de ejecución en nanosegundos
inicio_ns = time.time_ns()
maximo = encontrar_maximo(lista)
fin_ns = time.time_ns()

# Calcular el tiempo de ejecución
tiempo_ejecucion_ns = fin_ns - inicio_ns

print(f"El máximo elemento en la lista es: {maximo}")
print(f"Tiempo de ejecución: {tiempo_ejecucion_ns} nanosegundos")

# Algoritmo de complejidad logarítmica
import random
import time

# Función de búsqueda binaria
def busqueda_binaria(lista, item):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        suposicion = lista[medio]
        if suposicion == item:
            return medio
        if suposicion > item:
            alto = medio - 1
        else:
            bajo = medio + 1
    return None

# Solicita al usuario el tamaño del array y el elemento a buscar
tamanio_array = int(input("Ingresa el tamaño del array: "))
elemento_a_buscar = int(input("Ingresa el elemento a buscar: "))

# Asegurar que el elemento a buscar no exceda el rango máximo
if elemento_a_buscar >= tamanio_array:
    print(f"El elemento a buscar debe ser menor que {tamanio_array}.")
else:
    # Generar una lista aleatoria dentro del rango [0, tamanio_array - 1] y la ordena
    lista = sorted([random.randint(0, tamanio_array - 1) for _ in range(tamanio_array)])

    # Medir el tiempo de ejecución en nanosegundos
    inicio_ns = time.time_ns()
    resultado = busqueda_binaria(lista, elemento_a_buscar)
    fin_ns = time.time_ns()

    # Calcular el tiempo de ejecución
    tiempo_ejecucion_ns = fin_ns - inicio_ns

    if resultado is not None:
        print(f"Elemento encontrado en el índice: {resultado}")
    else:
        print("Elemento no encontrado en la lista.")

    print(f"Tiempo de ejecución: {tiempo_ejecucion_ns} nanosegundos")
