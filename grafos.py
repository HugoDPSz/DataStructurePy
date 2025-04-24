def inicializar_matriz(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return matriz

def inicializar_lista(n):
    lista = [[]for _ in range(n)]
    return lista

def adicionar_aresta_matriz(matriz, u, v):
    matriz[u][v] = 1
    matriz[v][u] = 1

def adicionar_aresta_lista(lista, u, v):
    lista[u].append(v)
    lista[v].append(u)

matriz = inicializar_matriz(5)
adicionar_aresta_matriz(matriz, 0, 4)
adicionar_aresta_matriz(matriz, 0, 3)
adicionar_aresta_matriz(matriz, 0, 2)
adicionar_aresta_matriz(matriz, 0, 1)
adicionar_aresta_matriz(matriz, 1, 2)
adicionar_aresta_matriz(matriz, 2, 3)
adicionar_aresta_matriz(matriz, 2, 4)

lista = inicializar_lista(5)
adicionar_aresta_lista(lista, 0, 4)
adicionar_aresta_lista(lista, 0, 3)
adicionar_aresta_lista(lista, 0, 2)
adicionar_aresta_lista(lista, 0, 1)
adicionar_aresta_lista(lista, 1, 2)
adicionar_aresta_lista(lista, 2, 3)
adicionar_aresta_lista(lista, 2, 4)