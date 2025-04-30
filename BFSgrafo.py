from collections import deque

def bfs_caminho_completo(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return None, None  # Retorna None se uma das cidades não existir

    fila = deque([(origem, [origem])])  # (cidade_atual, caminho_percorrido)
    visitados = set([origem])

    while fila:
        cidade_atual, caminho = fila.popleft()

        if cidade_atual == destino:
            distancia = len(caminho) - 1  # Distância = número de arestas
            return caminho, distancia

        for vizinho in grafo[cidade_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = caminho + [vizinho]
                fila.append((vizinho, novo_caminho))

    return None, None  # Se não houver caminho

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F", "G"],
    "F": ["C", "E", "H"],
    "G": ["E", "I"],
    "H": ["F", "J"],
    "I": ["G", "K"],
    "J": ["H", "L"],
    "K": ["I", "M"],
    "L": ["J", "N"],
    "M": ["K"],
    "N": ["L"]
}

# Entrada do usuário
origem = input("Digite a cidade de origem: ").strip().upper()
destino = input("Digite a cidade de destino: ").strip().upper()

caminho, distancia = bfs_caminho_completo(grafo, origem, destino)

if caminho:
    print(f"\nCaminho encontrado: {' → '.join(caminho)}")
    print(f"Distância (em número de cidades percorridas): {distancia}")
else:
    print(f"\nNão há caminho entre {origem} e {destino}.")