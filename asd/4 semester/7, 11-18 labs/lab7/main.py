import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# чтение матрицы смежности из файла
with open('graph.txt', "r") as f:
    n = int(f.readline().strip())  # число вершин
    matrix = [[int(j) for j in f.readline().strip().split()] for i in range(n)]

# инициализация списка ребер дерева
edges = []
# инициализация списка посещенных вершин
visited = [0]
# инициализация списка доступных ребер
available_edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(i) if matrix[i][j] != 0 and 
                   (i in visited) != (j in visited)]

# проход по всем вершинам графа
for i in range(n-1):
    # поиск ребра с наименьшим весом среди доступных ребер
    e = min(available_edges, key=lambda x: x[2])
    # добавление ребра к дереву
    edges.append(e)
    # добавление новой вершины в список посещенных
    new_vertex = e[0] if e[1] in visited else e[1]
    visited.append(new_vertex)
    # обновление списка доступных ребер
    available_edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(i) if matrix[i][j] != 0 and 
                       ((i in visited) != (j in visited)) and ((i, j) not in edges) and ((j, i) not in edges)]

# вывод результирующего списка ребер
print("Минимальное остовное дерево состоит из следующих ребер:")
for e in edges:
    print("Ребро между вершинами {} и {}, вес ребра: {}".format(e[0], e[1], e[2]))
