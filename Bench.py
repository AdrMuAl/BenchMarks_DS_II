import time
import random
def contar_frecuencias(array): #O(n)
    frecuencias = {} 

    for numero in array:  
        if numero in frecuencias:  
            frecuencias[numero] += 1
        else:  
            frecuencias[numero] = 1

    return frecuencias


def busqueda_secuencial(arr, elemento): #O(n)
    for num in arr:
        if num == elemento:
            return True
    return False

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

def bubble_sort(arr): # O(n^2)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr): # O(n log n)
    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def generar_subconjuntos(conjunto):# O(2^n)
    n = len(conjunto)
    total_subconjuntos = 2 ** n
    for i in range(total_subconjuntos):
        subconjunto = []
        for j in range(n):
            if (i >> j) % 2 == 1:
                subconjunto.append(conjunto[j])


def medir_tiempo(arr, tipo):
    inicio = time.time()
    
    if tipo == "merge":
        merge_sort(arr.copy())
    elif tipo == "bubble":
        bubble_sort(arr.copy())
    elif tipo == "subc":
        generar_subconjuntos(arr.copy())
    elif tipo == "sec":
        busqueda_secuencial(arr.copy(),1000000000000)
    elif tipo == "bin":
        busqueda_binaria(arr.copy(), 1000000)
    elif tipo == "frec":
        contar_frecuencias(arr.copy())
        
    fin = time.time()
    tiempo = fin  - inicio 

    return tiempo



ArrayBubble = [10,100,1000,10000,12000]
tamaños_array = [10,100,1000,10000,50000,100000,500000,1000000,5000000,10000000,]
tamaños_arraySub = [5,10,15,20,25]

for tamano in tamaños_array:
    array = list(range(tamano))
    random.shuffle(array)


    tiempo_sec = medir_tiempo(array, "sec")
    tiempo_bin = medir_tiempo(array, "bin")
    tiempo_frec = medir_tiempo(array, "frec")

    print(f"Tamaño del array: {tamano}")

    print(f"Tiempo de Busqueda secuencial: {tiempo_sec} nanosegundos")
    print(f"Tiempo de Búsqueda Binaria: {tiempo_bin} nanosegundos")
    print(f"Tiempo de Contar Frecuencias: {tiempo_frec} nanosegundos")
    print("-" * 50)
    
for tamano in ArrayBubble:
    array = list(range(tamano))
    random.shuffle(array)

    tiempo_merge = medir_tiempo(array, "merge")
    tiempo_bubble = medir_tiempo(array, "bubble")
 

    print(f"Tamaño del array: {tamano}")
    print(f"Tiempo de Merge Sort: {tiempo_merge} nanosegundos")
    print(f"Tiempo de Bubble Sort: {tiempo_bubble} nanosegundos")

    print("-" * 50)
    
for tamano in tamaños_arraySub:
    array = list(range(tamano))
    random.shuffle(array)
    tiempo_subc = medir_tiempo(array, "subc")
    
    print(f"Tamaño del array: {tamano}")
    print(f"Tiempo de Generar Subconjuntos: {tiempo_subc} nanosegundos")


