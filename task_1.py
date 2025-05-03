import heapq

def find_shortest_paths(graph, start_node):
    num_nodes = len(graph)
    distance = [float('inf')] * num_nodes
    previous_node = [None] * num_nodes
    distance[start_node] = 0
    processing_queue = [(0, start_node)]

    while processing_queue:
        current_distance, current_node = heapq.heappop(processing_queue)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = distance[current_node] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous_node[neighbor] = current_node
                heapq.heappush(processing_queue, (new_distance, neighbor))

    return distance, previous_node
