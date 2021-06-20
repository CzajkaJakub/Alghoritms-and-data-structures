def read_file():
    try:
        file = open('readingData/test.txt', "r")
        vertex, edge = file.readline().split(" ")
        vertex = int(vertex)
        edge = int(edge)
        graph = {}
        pre_graph = {}
        for i in range(edge):
            verticle1, verticle2 = [int(i) for i in file.readline().split(" ")]
            if verticle1 not in graph:
                graph[verticle1] = [verticle2]
            else:
                temp = graph[verticle1]
                temp.append(verticle2)
                graph[verticle1] = temp

            if verticle2 not in pre_graph:
                pre_graph[verticle2] = [verticle1]
            else:
                temp = pre_graph[verticle2]
                temp.append(verticle1)
                pre_graph[verticle2] = temp

        return vertex, edge, graph, pre_graph


    except(ValueError):
        print("Błąd w pliku")
        return 0


def read_own():
    vertices = check_amount(input("Input the number of vertices:"))
    edges = check_amount(input("Input the number of edges:"))
    graph = {}
    pre_graph = {}
    for _ in range(edges):
        print("Input an edge")
        ver1, ver2 = check_edge(vertices)
        if ver1 not in graph:
            graph[ver1] = [ver2]
        else:
            temp = graph[ver1]
            temp.append(ver2)
            graph[ver1] = temp

        if ver2 not in pre_graph:
            pre_graph[ver2] = [ver1]
        else:
            temp = pre_graph[ver2]
            temp.append(ver1)
            pre_graph[ver2] = temp

    return vertices, edges, graph, pre_graph


def check_amount(amount):
    try:
        amount = int(amount)
        if amount > 0:
            return amount
        else:
            print("Wrong data entered, please try again:")
            return check_amount(input())
    except(ValueError):
        print("Wrong data entered, please try again:")
        return check_amount(input())


def check_edge(vertices):
    temp = input()
    if (len(temp.split(" ")) == 2):
        try:
            ver1, ver2 = [int(i) for i in temp.split(" ")]
            if ((ver1 > vertices) or (ver2 > vertices)):
                print(("Wrong data entered"))
                return check_edge(vertices)
            elif ((ver1 <= 0) or (ver1 <= 0)):
                print("Wrong data entered")
                return check_edge(vertices)
            else:
                return ver1, ver2

        except(ValueError):
            print("Wrong data entered, input again:")
            return check_edge(vertices)
    else:
        print("Wrong data entered, input again:")
        return check_edge(vertices)
