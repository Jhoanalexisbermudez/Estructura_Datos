def ordenar_por_insercion(lista):
    for indice in range(1, len(lista)):
        elemento_clave = lista[indice]
        posicion = indice - 1

        while posicion >= 0 and lista[posicion] > elemento_clave:
            lista[posicion + 1] = lista[posicion]
            posicion -= 1
        lista[posicion + 1] = elemento_clave

    return lista

numeros = [5, 1, 8, 9, 12]
resultado_ordenado = ordenar_por_insercion(numeros)
print("Lista ordenada: ", resultado_ordenado)