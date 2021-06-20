def create_graph(vertices, graph, pre_graph):
    matrix = [[0 for _ in range(vertices + 3)] for _ in range(vertices)]
    for i in range(vertices+1):
        if i in graph.keys():
            matrix[i-1][vertices] = min(graph[i])

    for i in graph.keys():
        for j in graph[i]:
            matrix[i-1][j-1] = max(graph[i])


    for i in range(vertices+1):
        if i in pre_graph.keys():
            matrix[i-1][vertices+1] = min(pre_graph[i])

    for i in pre_graph.keys():
        for j in pre_graph[i]:
            matrix[i-1][j-1] = max(pre_graph[i])+vertices

    no_edge = {}
    for i in range(1, vertices+1):
        for j in range(1, vertices+1):
            if i in graph.keys():
                if j not in graph[i]:
                    if j in graph.keys():
                        if i not in graph[j]:
                            if i not in no_edge:
                                no_edge[i] = [j]
                            else:
                                temp = no_edge[i]
                                temp.append(j)
                                no_edge[i] = temp
                    else:
                        if i not in no_edge:
                            no_edge[i] = [j]
                        else:
                            temp = no_edge[i]
                            temp.append(j)
                            no_edge[i] = temp
            elif j in graph.keys():
                if i not in graph[j]:
                    if i not in no_edge:
                        no_edge[i] = [j]
                    else:
                        temp = no_edge[i]
                        temp.append(j)
                        no_edge[i] = temp
            else:
                if i not in no_edge:
                    no_edge[i] = [j]
                else:
                    temp = no_edge[i]
                    temp.append(j)
                    no_edge[i] = temp

    for i in range(vertices+1):
        if i in no_edge.keys():
            matrix[i-1][vertices+2] = min(no_edge[i])

    for i in no_edge.keys():
        for j in no_edge[i]:
            matrix[i-1][j-1] = max(no_edge[i]) * (-1)




    return matrix