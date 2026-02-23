import heapq

def astar(graph, heuristic, start, goal):

    open_set=[]
    heapq.heappush(open_set, (0 + heuristic.get(start,0), 0, start, [start]))
    closed = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g
        
        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in closed:
                new_g = g + cost
                new_f = new_g + heuristic.get(neighbor,0)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')