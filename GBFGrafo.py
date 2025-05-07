import heapq

# Função que implementa a busca gulosa
def busca_gulosa(grafo, heuristicas, cidade_inicial, cidade_objetivo):
    # Fila de prioridade para explorar as cidades
    fila_prioridade = []
    # Coloca a cidade inicial na fila de prioridade (com a heurística como chave)
    heapq.heappush(fila_prioridade, (heuristicas[cidade_inicial], cidade_inicial))
    
    # Dicionário para armazenar o predecessor de cada cidade (para reconstruir o caminho)
    predecessores = {cidade_inicial: None}
    
    # Dicionário para armazenar o custo total de chegar em cada cidade
    custos = {cidade_inicial: 0}
    
    # Conjunto para verificar se uma cidade já foi visitada
    visitadas = set()

    while fila_prioridade:
        # Obtém a cidade com a menor heurística
        _, cidade_atual = heapq.heappop(fila_prioridade)

        # Se encontramos a cidade objetivo, reconstruímos o caminho
        if cidade_atual == cidade_objetivo:
            print(f"Objetivo encontrado: {cidade_atual}")
            
            # Reconstruir o caminho percorrido
            caminho = []
            cidade_atual_aux = cidade_objetivo
            while cidade_atual_aux is not None:
                caminho.append(cidade_atual_aux)
                cidade_atual_aux = predecessores[cidade_atual_aux]
            caminho.reverse()
            
            print("Caminho percorrido:", caminho)
            print("Distância total:", custos[cidade_objetivo])
            return True
        
        if cidade_atual in visitadas:
            continue

        # Marca a cidade como visitada
        visitadas.add(cidade_atual)

        # Explora os vizinhos da cidade atual
        for vizinho, distancia in grafo[cidade_atual].items():
            if vizinho not in visitadas:
                custo_total = custos[cidade_atual] + distancia
                # Se o vizinho não foi visitado ou encontrou um caminho mais barato
                if vizinho not in custos or custo_total < custos[vizinho]:
                    custos[vizinho] = custo_total
                    predecessores[vizinho] = cidade_atual
                    # Coloca os vizinhos na fila de prioridade
                    heapq.heappush(fila_prioridade, (heuristicas[vizinho], vizinho))
    
    print("Objetivo não encontrado")
    return False

# Grafo: cidades e distâncias entre vizinhas (distância entre nós)
grafo = {
    'A': {'B': 2, 'C': 4, 'D': 6, 'E': 10},
    'B': {'A': 2, 'C': 1, 'F': 3},
    'C': {'A': 4, 'B': 1, 'D': 2, 'G': 8},
    'D': {'A': 6, 'C': 2, 'H': 5},
    'E': {'A': 10, 'F': 7},
    'F': {'B': 3, 'E': 7, 'I': 4},
    'G': {'C': 8, 'H': 2},
    'H': {'D': 5, 'G': 2, 'J': 6},
    'I': {'F': 4, 'K': 2},
    'J': {'H': 6, 'K': 3, 'L': 1},
    'K': {'I': 2, 'J': 3, 'L': 4},
    'L': {'J': 1, 'K': 4, 'M': 2},
    'M': {'L': 2, 'N': 3},
    'N': {'M': 3}
}

# Heurísticas: distância em linha reta da cidade até a cidade objetivo 'N'
heuristicas = {
    'A': 12,
    'B': 10,
    'C': 8,
    'D': 6,
    'E': 14,
    'F': 8,
    'G': 5,
    'H': 4,
    'I': 7,
    'J': 3,
    'K': 2,
    'L': 1,
    'M': 1,
    'N': 0  # Cidade objetivo
}

busca_gulosa(grafo, heuristicas, 'A', 'N')