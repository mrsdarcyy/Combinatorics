import collections

class Graph:
    def __init__(self, vertices:int) -> None:
        self.V = vertices
        self.graph = []

    def add_edge(self, u:int, v:int, w:int) -> None:
        self.graph.append([u, v, w])

def levit(gr, start: int = 0) -> None:
    m0 = []
    m1 = collections.deque()
    m2 = [x for x in range(gr.V)]
    
    m1.append(m2.pop(start))

    dist = [float('inf') for _ in range(gr.V)]
    dist[start] = 0

    pred = [-1 for _ in range(gr.V)]
    pred[start] = None


while m1:
    current = m1.popleft()
    for u, v, w in gr.graph:
        if u == current:
            # мы не находили путь к этой вершине раньше
            if v in m2:
                dist[v] = dist[u] + w
                m2.remove(v)
                m1.append(v)
                pred[v] = u
            
            # мы уже знаем какой-то путь к ней, но не от неё
            elif v in m1:
                # нашли более короткий путь
                if dist[v] >= dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
            
            # мы уже посчитали путь от вершины v к её соседям
            elif v in m0:
                # нашли более короткий путь до вершины v
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    # отправили вершину на перерасчёт всех путей к её соседям
                    m0.remove(v)
                    m1.appendleft(v)

    # расчёт путей до соседей окончен
    m0.append(current)


def levit(gr, start: int = 0) -> None:
    # вершины, расстояние до которых и сосдей которых посчитали
    m0 = []

    # вершины, расстояние до соседей которых надо рассчитать
    m1 = collections.deque()
    
    # вершины, до которых мы ещё не знаем, как добраться
    m2 = [x for x in range(gr.V)]
    m1.append(m2.pop(start))
    
    # массив расстояний до вершины
    dist = [float('inf') for _ in range(gr.V)]
    dist[start] = 0

    # родительские вершины
    pred = [-1 for _ in range(gr.V)]
    pred[start] = None

    while m1:
        current = m1.popleft()
        for u, v, w in gr.graph:
            if u == current:
                # мы не находили путь к этой вершине раньше
                if v in m2:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    m2.remove(v)
                    m1.append(v)
                    
                # мы уже знаем какой-то путь к ней, но не от неё
                elif v in m1:
                    # нашли более короткий путь
                    if dist[v] >= dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                
                # мы уже посчитали путь от вершины v к её соседям
                elif v in m0:
                    # нашли более короткий путь до вершины v
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        m0.remove(v)
                        # отправили вершину на перерасчёт всех путей к её соседям
                        m1.appendleft(v)

        # расчёт путей до соседей окончен
        m0.append(current)
        
