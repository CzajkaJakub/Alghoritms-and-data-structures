def hamiltonS(graph, ver, visited, vertices, first):
    global w
    tmp = visited[:]
    if ver not in visited:
        tmp.append(ver)
        if (len(tmp) == vertices) and (first in graph[tmp[-1]]):
            tmp.append(first)
            print(tmp)
            w = 1
        else:
            for j in graph[ver]:
                if j in graph.keys():
                    hamiltonS(graph, j, tmp, vertices, first)


def hamiltonN(adj, ver, visited, vertices, first):
    tmp = visited[:]
    if ver not in visited:
        tmp.append(ver)
        if (len(tmp) == vertices) and (adj[tmp[-1]][first] == 1):
            tmp.append(first)
            for i in range(vertices + 1):
                tmp[i] += 1
            print(tmp)
        else:
            for j in range(vertices):
                if adj[ver][j] == 1:
                    hamiltonN(adj, j, tmp, vertices, first)


def eulerS(edges, edges2):
    check = True
    for i in edges.keys():
        if not (i in edges.keys() and i in edges2.keys()) or len(edges[i]) != len(edges2[i]):
            print("There is no Eulerian circuit.")
            check = False
            break
    if check == True:
        output = eulerS1(edges, 1, [])
        output.reverse()
        print(output)


def eulerS1(edges, current, stack):
    for i in edges[current]:
        edges[current].remove(i)
        eulerS1(edges, i, stack)
    stack.append(current)
    return stack


def eulerN1(adj):
    check = True
    for i in adj:
        if sum(i) % 2 == 1:
            print("There is no Eulerian circuit.")
            check = False
            break
    if check == True:
        output = eulerN(adj, 1, [])
        output.reverse()
        print(output)


def eulerN(edges, current, stack):
    for i in range(len(edges)):
        if edges[i][current] == 1:
            edges[i][current] = 0
            edges[current][i] = 0
            eulerN(edges, i, stack)
    stack.append(current + 1)
    return stack
