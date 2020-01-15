from floyd_warshall.algo.Graph import Graph
from floyd_warshall.algo.Parser import Parser


def launch_floyd_warshall(csv):
    graph = Graph()
    try:
        Parser(csv, graph)
    except Exception as e:
        return e
    graph.initialize_tab()
    for l in graph.links:
        graph.add_link(l['src'], l['dst'], l['weight'])
    for k in range(graph.size):
        for i in range(graph.size):
            for j in range(graph.size):
                graph.tab[i][j] = min(
                    graph.tab[i][j], graph.tab[i][k] + graph.tab[k][j])
    return (graph.tab)
