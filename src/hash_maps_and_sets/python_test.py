map_to_graph = []
starting_cnt = 0
for i in range(9):
    map_to_graph.append([])
    sub_starting_cnt = starting_cnt
    for j in range(9):
        if j % 3 == 0:
            sub_starting_cnt += 1
        map_to_graph[i].append()

print(map_to_graph)
