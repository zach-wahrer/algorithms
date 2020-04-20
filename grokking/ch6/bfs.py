from collections import deque


class Connections_Map:
    def __init__(self):
        self.locations = {}

    def add_location(self, location: str, connections: list):
        self.locations[location] = connections
        return self

    def add_multi_locations(self, places: dict):
        for place in places:
            self.add_location(place, places[place])
        return self

    def shortest_path(self, from_location, to_location):
        to_visit = deque()
        visited = {from_location}
        steps = 1

        to_visit += self.locations[from_location]

        while to_visit:
            visiting = to_visit.popleft()
            if type(visiting) == int:
                steps = visiting
                continue
            if visiting not in visited:
                if visiting == to_location:
                    return steps
                to_visit += [steps + 1] + self.locations[visiting]
                visited.add(visiting)

        return -1


places = {
    'Bozeman': ['Billings', 'Butte', 'Helena'],
    'Helena': ['Bozeman', 'Butte'],
    'Butte': ['Helena', 'Bozeman', 'Missoula'],
    'Billings': ['Bozeman'],
    'Missoula': ['Butte']
}


connections = Connections_Map().add_multi_locations(places)

print(connections.shortest_path("Butte", "Billings"))
