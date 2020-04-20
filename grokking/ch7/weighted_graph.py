def find_shortest_path(distances, visited):
    shortest_distance = float('inf')
    nearest_city = None
    for to_city in distances:
        if distances[to_city] < shortest_distance and to_city not in visited:
            shortest_distance = distances[to_city]
            nearest_city = to_city
    return nearest_city


start = "Bozeman"
finish = "Seattle"

# map = {
#     'Bozeman':
#         {'Missoula': 202, 'Twin Falls': 356},
#     'Missoula':
#         {'Spokane': 198},
#     'Twin Falls':
#         {'Boise': 129},
#     'Boise':
#         {'Portland': 431, 'Yakima': 353},
#     'Spokane':
#         {'Yakima': 203, 'Seattle': 279},
#     'Portland':
#         {'Yakima': 185, 'Seattle': 174},
#     'Yakima':
#         {'Seattle': 142, 'Portland': 186},
#     'Seattle':
#         {'Squamish': 182},
#     'Squamish': {}
# }

# map = {
#     'Bozeman':
#         {'Missoula': 7, 'Twin Falls': 5},
#     'Missoula':
#         {'Boise': 1},
#     'Twin Falls':
#         {'Boise': 6},
#     'Boise':
#         {},
#
# }

map = {
    'Bozeman':
        {'Missoula': 1, 'Twin Falls': 5},
    'Missoula':
        {'Boise': 2},
    'Twin Falls':
        {'Boise': 1},
    'Boise':
        {'Portland': 4},
    'Portland':
        {'Seattle': 1},
    'Seattle':
        {}
}


distances = {finish: float('inf')}

for city in map[start].keys():
    distances[city] = map[start][city]

parents = {finish: None}
for edge in map[start]:
    parents[edge] = start

visited = []

next_city = find_shortest_path(distances, visited)

while next_city:
    distance = distances[next_city]
    for connection in map[next_city].keys():
        new_distance = distance + map[next_city][connection]
        if connection in distances:
            if distances[connection] > new_distance:
                distances[connection] = new_distance
                parents[connection] = next_city
        else:
            print('ping', next_city, connection, map[next_city][connection])
            distances[connection] = map[next_city][connection]
            parents[connection] = next_city

    visited.append(next_city)
    next_city = find_shortest_path(distances, visited)

print(distances)
print(parents)
