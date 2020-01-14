from floyd_warshall.algo.Graph import Graph
from floyd_warshall.algo.Parser import Parser


def launch_floyd_warshall(csv):
    try:
        data = Parser(csv)
    except Exception as e:
        return e
    graph = Graph(data.size)
    for l in data.links:
        graph.add_link(l['src'], l['dst'], l['weight'])
    for k in range(graph.size):
        for i in range(graph.size):
            for j in range(graph.size):
                graph.tab[i][j] = min(
                    graph.tab[i][j], graph.tab[i][k] + graph.tab[k][j])
    return (graph.tab)
