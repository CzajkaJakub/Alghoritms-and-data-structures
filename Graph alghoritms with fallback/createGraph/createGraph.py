def create_adj(vertices, graph):
    matrix = [[0 for _ in range(1, vertices + 1)] for _ in range(1, vertices + 1)]
    for e in graph.keys():
        link = graph[e]
        for i in link:
            matrix[e - 1][i - 1] = 1
            matrix[i - 1][e - 1] = 1
    return matrix