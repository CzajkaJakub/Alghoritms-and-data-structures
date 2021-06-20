def start(matrix):
    start = 0
    for i in range(len(matrix)):
        can = 1
        for j in range(len(matrix[i])):
            if matrix[j][i] == 1:
                can = 0
        if can == 1:
            start = i
    return start


def search_dfs(matrix, start, visited, stos):
    if start not in visited:
        visited.append(start)
        for i in range(len(matrix[start])):
            if matrix[start][i] == 1:
                visited, stos = search_dfs(matrix, i, visited, stos)
        stos.append(start + 1)
        return visited, stos
    else:
        return visited, stos


def dfs_ADJ(matrix):
    start_ver = start(matrix)
    vis, stos = search_dfs(matrix, start_ver, [], [])
    for i in range(len(stos)):
        print(stos[- i - 1], end=" ")


def start_v2(matrix, stack):
    for i in range(len(matrix)):
        x = matrix[i].count(1)
        y = matrix[i].count(-1)
        if ((x > 0) and y == 0):
            return i
    for i in range(1, len(matrix) + 1):
        if i + 1 not in stack:
            return i


def del_adj(matrix):
    stack = []
    for i in range(len(matrix[0])):
        start_ver = start_v2(matrix, stack)
        stack.append(start_ver + 1)
        for j in range(len(matrix[0])):
            if matrix[start_ver][j] == 1:
                matrix[start_ver][j] = 0
                matrix[j][start_ver] = 0

    for i in stack:
        print(i, end=" ")


def del_graph(matrix):
    st_in = []
    for i in range(len(matrix)):
        tmp = 0
        for j in range(len(matrix[i])):
            if len(matrix) < matrix[i][j] <= 2 * len(matrix):
                tmp += 1
        st_in.append(tmp)

    queue = []
    for i in range(len(matrix)):
        if st_in[i] == 0:
            queue.append(i)

    while queue:

        u = queue.pop(0)
        print(u + 1, end=" ")

        for i in range(len(matrix)):
            if 0 <= matrix[u][i] <= len(matrix):
                st_in[i] -= 1
                if st_in[i] == 0:
                    queue.append(i)

    return


def search_dfs_graph(matrix, start, visited, stos):
    if start not in visited:
        visited.append(start)
        for i in range(len(matrix)):
            if 0 < matrix[start][i] <= len(matrix):
                visited, stos = search_dfs_graph(matrix, i, visited, stos)
        stos.append(start + 1)
        return visited, stos
    else:
        return visited, stos


def dfs_graph(matrix):
    start_ver = 0
    for i in range(len(matrix)):
        if matrix[i][len(matrix) + 1] == 0:
            start_ver = i
            break
    vis, stos = search_dfs_graph(matrix, start_ver, [], [])
    for i in range(len(stos)):
        print(stos[-i - 1], end=" ")
    return 0
