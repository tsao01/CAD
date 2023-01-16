def task(csv_data):
    edges = [tuple(int(v) for v in edge.split(',') if v) for edge in csv_data.strip().rstrip().split('\n')]

    vertex_count = 0
    for v, u in edges:
        vertex_count = max(v, u, vertex_count)

    graph = {v: [] for v in range(1, vertex_count + 1)}
    for u, v in edges:
        graph[u].append(v)

    result = [set() for i in range(5)]

    for v, list_to in graph.items():
        if list_to:
            result[0].add(v)
        for to in list_to:
            result[1].add(to)
            if graph[to]:
                result[2].add(v)
            if len(graph[v]) > 1:
                result[4].add(to)
            result[3].update(graph[to])
            
    return [sorted(list(s)) for s in result]

def main():
    with open('data.csv') as file:
        csv_data = file.read()
        result = task(csv_data)
        print(result)

if __name__ == '__main__':
    main()