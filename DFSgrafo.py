from collections import deque

def dfs_iterativo(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return None, None  # Cidades não existem

    pilha = [(origem, [origem])]  # (cidade_atual, caminho)
    visitados = set()

    while pilha:
        cidade_atual, caminho = pilha.pop()  # LIFO (último a entrar é o primeiro a sair)

        if cidade_atual == destino:
            distancia = len(caminho) - 1
            return caminho, distancia

        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            for vizinho in reversed(grafo[cidade_atual]):  # Empilha na ordem correta
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))

    return None, None  # Caminho não encontrado

# Grafo de exemplo (14 cidades)
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

# Testando
origem = "H"
destino = "N"
caminho, distancia = dfs_iterativo(grafo, origem, destino)

if caminho:
    print(f"Caminho DFS: {' → '.join(caminho)}")
    print(f"Distância: {distancia} saltos")
else:
    print(f"Não há caminho entre {origem} e {destino}.")