from errorHandling.errorHandling import *
from readingData.readData import *
from createGraph.createGraph import *
from actions.search import *


def main():
    print("Choose type of input 'F' if file or 'O' if own: ")
    input_type = check_type_of_input(input())
    vertices, edge, graph, pre_graph = graph_type(input_type)
    print("Write a number of program type:\n"
          "1. - Hamilton with directed graph\n"
          "2. - Hamilton with undirected graph\n"
          "3. - Euler with directed graph\n"
          "4. - Euler with undirected graph\n")
    task = task_type(input())
    action(vertices, edge, graph, task, pre_graph)
    return 0


def graph_type(type):
    if type == "O":
        return read_own()
    else:
        return read_file()


def action(vertices, edge, graph, task, pre_graph):
    if task == 1:
        for i in graph.keys():
            hamiltonS(graph, i, [], vertices, i)
        print("There is no a hamiltonian circuit")

    elif task == 2:
        matrix = create_adj(vertices, graph)
        for i in range(vertices):
            hamiltonN(matrix, i, [], vertices, i)
        print("There is no a hamiltonian circuit")
    elif task == 3:
        eulerS(graph, pre_graph)
    elif task == 4:
        matrix = create_adj(vertices, graph)
        eulerN1(matrix)


if __name__ == "__main__":
    main()
