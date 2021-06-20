from errorsHandling.errorHandling import *
from readingData.readData import *
from makeGraphs.adjMatrix import *
from makeGraphs.graphMatrix import *
from actions.action import *


def main():
    print("Choose type of input 'F' if file or 'O' if own: ")
    input_type = check_type_of_input(input())
    vertices, edge, graph, pre_graph = graph_type(input_type)
    print("Write: 'Adj' if you would like to create an adjacency matrix or "
          "'Graph' if you would like to create a graph matrix")
    types = check_type(input())
    matrix = users_choice(vertices, graph, types, pre_graph)
    print("Your matrix:")
    matrix_p(matrix)
    if check_cyclic() == 1:
        print("Graph has no cycle")
        print("Write: 'DFS' if you would like to choose a Depth First Search algorithm or "
              "'DEL' if you want to choose a "
              "Kahn's algorithm")
        task = check_task(input())
        action(task, matrix, types)


def graph_type(typeI):
    if typeI == "O":
        return read_own()
    else:
        return read_file()


def users_choice(vertices, graph, types, pre_graph):
    if types == 'Adj':
        matrix = create_adj(vertices, graph)
    else:
        matrix = create_graph(vertices, graph, pre_graph)
    return matrix


def action(task, matrix, types):
    if task == "DEL":
        if types == "Graph":
            del_graph(matrix)
        else:
            del_adj(matrix)
    else:
        if types == "Adj":
            dfs_ADJ(matrix)
        else:
            dfs_graph(matrix)


def matrix_p(matrix):
    for row in matrix:
        x = 0
        for element in row:
            x += 1
            if x == len(row):
                print(element)
            else:
                print(element, end="\t")


if __name__ == "__main__":
    main()
