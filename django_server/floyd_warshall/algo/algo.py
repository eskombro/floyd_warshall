from Graph import Graph
from Parser import Parser


def launch_floyd_warshall(csv):
    try:
        data = Parser(csv)
    except Exception as e:
        return e
    graph = Graph(data.size)
    for l in data.links:
        graph.add_link(l['src'], l['dst'], l['weight'])
    return (graph.tab)


if __name__ == '__main__':
    csv = '''4
    7
    1,2,3
    2,3,2
    3,4,1
    3,1,5
    4,1,2
    2,1,8
    1,4,7
    '''
    print(launch_floyd_warshall(csv))
