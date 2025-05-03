import heapq

def dijkstra(G, s):
    n = len(G)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[s] = 0
    Q = [(0, s)]

    while Q:
        d, u = heapq.heappop(Q)
        
        if d > dist[u]:
            continue

        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(Q, (dist[v], v))

    return dist, prev
