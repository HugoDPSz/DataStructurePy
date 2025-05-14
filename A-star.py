import heapq
import math

# Função para calcular a distância Euclidiana entre dois pontos (p1, p2)
def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def algoritmo_a_estrela(inicio, fim, pontos):
    # Inicializar estruturas
    aberto = []
    fechado = set()
    came_from = {}
    g = {}
    h = {}

    heapq.heappush(aberto, (0 + distancia(inicio, fim), 0, inicio))  # (f, g, ponto)
    g[inicio] = 0
    h[inicio] = distancia(inicio, fim)

    while aberto:
        # Pega o ponto com o menor valor de f = g + h
        _, custo_atual, atual = heapq.heappop(aberto)

        if atual == fim:
            caminho = []
            while atual in came_from:
                caminho.append(atual)
                atual = came_from[atual]
            caminho.append(inicio)
            caminho.reverse()

            distancia_percorrida = g[fim]
            
            distancia_reta = distancia(inicio, fim)
            
            return caminho, distancia_percorrida, distancia_reta

        fechado.add(atual)

        for vizinho in pontos[atual]:
            if vizinho in fechado:
                continue

            novo_g = custo_atual + distancia(atual, vizinho)

            if vizinho not in g or novo_g < g[vizinho]:
                g[vizinho] = novo_g
                f = novo_g + distancia(vizinho, fim)
                heapq.heappush(aberto, (f, novo_g, vizinho))
                came_from[vizinho] = atual

    return None, None, None  


pontos = {
    (0, 0): [(1, 0), (0, 1)], 
    (1, 0): [(2, 0), (0, 0)], 
    (0, 1): [(1, 1), (0, 0)],
    (1, 1): [(2, 1), (0, 1)], 
    (2, 0): [(2, 1), (1, 0)], 
    (2, 1): [(3, 1), (1, 1), (2, 0)],
    (3, 1): [(3, 0), (2, 1)],
    (3, 0): [(3, 1)],
    (3, 2): [(2, 2), (4, 2)],
    (2, 2): [(1, 2), (3, 2)],
    (1, 2): [(0, 2), (2, 2)],
    (0, 2): [(1, 2), (0, 3)],
    (0, 3): [(0, 2), (1, 3)],
    (1, 3): [(0, 3), (2, 3)],
    (2, 3): [(1, 3), (3, 3)],
    (3, 3): [(2, 3)]
}

inicio = (0, 0)
fim = (3, 1)

caminho, distancia_percorrida, distancia_reta = algoritmo_a_estrela(inicio, fim, pontos)

if caminho:
    print("Caminho percorrido:", caminho)
    print("Distância percorrida:", distancia_percorrida)
    print("Distância em linha reta:", distancia_reta)
else:
    print("Caminho não encontrado.")