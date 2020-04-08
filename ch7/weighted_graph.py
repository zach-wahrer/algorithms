def find_shortest_path(distances, visited):
    shortest_distance = float('inf')
    nearest_city = None
    for to_city in distances:
        if distances[to_city] < shortest_distance and to_city not in visited:
            shortest_distance = distances[to_city]
            nearest_city = to_city
    return nearest_city


# map = {
#     'Bozeman':
#         {'Missoula': 202, 'Twin Falls': 356},
#     'Missoula':
#         {'Twin Falls': 400, 'Spokane': 198},
#     'Twin Falls':
#         {'Boise': 129},
#     'Boise':
#         {'Spokane': 422, 'Portland': 431, 'Yakima': 353},
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

map = {
    'Bozeman':
        {'Missoula': 202, 'Twin Falls': 100},
    'Missoula':
        {'Boise': 5},
    'Twin Falls':
        {'Boise': 129},
    'Boise':
        {}
}

distances = {'Boise': float('inf')}
for city in map['Bozeman'].keys():
    distances[city] = map['Bozeman'][city]

# distances = {'Squamish': float('inf')}
# for city in map['Bozeman'].keys():
#     distances[city] = map['Bozeman'][city]

# parents = {'Squamish': None, 'Missoula': 'Bozeman', 'Twin Falls': 'Bozeman'}

parents = {'Boise': None, 'Missoula': 'Bozeman', 'Twin Falls': 'Bozeman'}

visited = []

next_city = find_shortest_path(distances, visited)

while next_city:
    print(next_city, distances)
    distance = distances[next_city]
    for connection in map[next_city].keys():
        new_distance = distance + map[next_city][connection]
        if distances[connection] > new_distance:
            distances[connection] = new_distance
            parents[connection] = connection
    visited.append(next_city)
    next_city = find_shortest_path(distances, visited)


print(distances)
print(distances['Boise'])
