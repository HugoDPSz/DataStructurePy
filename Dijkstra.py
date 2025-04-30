import heapq

def dijkstra(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return None, None  # Cidades não existem no grafo

    # Estruturas de dados
    distancias = {cidade: float('infinity') for cidade in grafo}  # Distâncias iniciais (infinito)
    distancias[origem] = 0  # Distância até a origem é 0
    fila_prioridade = [(0, origem)]  # Heap: (distância, cidade)
    caminho_anterior = {}  # Rastreia o caminho

    while fila_prioridade:
        dist_atual, cidade_atual = heapq.heappop(fila_prioridade)

        if cidade_atual == destino:  # Chegamos ao destino!
            # Reconstrói o caminho
            caminho = []
            while cidade_atual in caminho_anterior:
                caminho.insert(0, cidade_atual)
                cidade_atual = caminho_anterior[cidade_atual]
            caminho.insert(0, origem)
            return caminho, dist_atual

        if dist_atual > distancias[cidade_atual]:
            continue  # Já encontramos um caminho melhor

        for vizinho, peso in grafo[cidade_atual].items():
            distancia = dist_atual + peso
            if distancia < distancias[vizinho]:  # Encontramos um caminho melhor?
                distancias[vizinho] = distancia
                caminho_anterior[vizinho] = cidade_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return None, None  # Não há caminho

# Grafo com distâncias em km (exemplo)
grafo = {
    "A": {"B": 10, "C": 15},
    "B": {"A": 10, "D": 12, "E": 15},
    "C": {"A": 15, "F": 10},
    "D": {"B": 12},
    "E": {"B": 15, "F": 5, "G": 8},
    "F": {"C": 10, "E": 5, "H": 7},
    "G": {"E": 8, "I": 6},
    "H": {"F": 7, "J": 9},
    "I": {"G": 6, "K": 10},
    "J": {"H": 9, "L": 11},
    "K": {"I": 10, "M": 12},
    "L": {"J": 11, "N": 13},
    "M": {"K": 12},
    "N": {"L": 13}
}

# Testando
origem = "H"
destino = "N"
caminho, distancia_total = dijkstra(grafo, origem, destino)

if caminho:
    print(f"Caminho mais curto: {' → '.join(caminho)}")
    print(f"Distância total: {distancia_total} km")
else:
    print(f"Não há caminho entre {origem} e {destino}.")