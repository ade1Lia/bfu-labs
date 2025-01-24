//Найти в заданном графе количество и состав компонент связности с помощью поиска в ширину
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

const int INF = 1e9;

std::vector<int> bfs(const std::vector<std::vector<int>>& graph, int start) {
    unsigned long n = graph.size();
    std::vector<int> dist(n, INF);
    dist[start] = 0;
    std::queue<int> q;
    q.push(start);

    while (!q.empty()) {
        int vertex = q.front();
        q.pop();
        for (int neighbor = 0; neighbor < n; neighbor++) {
            if (graph[vertex][neighbor] == 1 && dist[neighbor] == INF) {
                dist[neighbor] = dist[vertex] + 1;
                q.push(neighbor);
            }
        }
    }

    return dist;
}

int main() {
    std::ifstream inputFile("graph.txt");
    std::ofstream outputFile("output.txt");

    int n;
    inputFile >> n;
    std::vector<std::vector<int>> graph(n, std::vector<int>(n));

    //считываем матрицу смежности из файла
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            inputFile >> graph[i][j];
        }
    }

    std::vector<int> visited(n, false); //массив векторов для отслеживания посещенных вершин
    int components = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            components++;
            std::vector<int> distances = bfs(graph, i);

            outputFile << "component " << components << ": ";

            for (int j = 0; j < n; j++) {
                if (distances[j] != INF) {
                    visited[j] = true;
                    outputFile << j << " ";
                }
            }
            outputFile << std::endl;
        }
    }
    outputFile << "Number of components: " << components << std::endl;

    inputFile.close();
    outputFile.close();

    return 0;
}