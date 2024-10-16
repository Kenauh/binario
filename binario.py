def bus_bin(A, E, inicio=0):
        
    i = len(A) // 2  # Calcula el punto medio del arreglo
    
    if A[i] == E:  # Verifica si el elemento medio es el que buscamos
        return inicio + i  
    
    if A[i] < E:    # Si el elemento medio es menor que el elemento buscado, busca en la mitad derecha
        return bus_bin(A[i+1:], E, inicio + i + 1)
    else:
        return bus_bin(A[:i], E, inicio)   # Si el elemento medio es mayor que el elemento buscado, busca en la mitad izquierda
    
arreglo = [3, 7, 9, 14, 18, 21, 25]
E = 21

resultado = bus_bin(arreglo, E) # Realizar la búsqueda

if resultado != -1:
    print(f"El elemento {E} fue encontrado en el índice {resultado}.")
else:
    print(f"-1")