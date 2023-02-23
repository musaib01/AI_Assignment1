graph = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Zerind": {"Oradea": 71, "Arad": 75},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 118, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Craiova": 146, "Pitesti": 97, "Sibiu": 80},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagarus": 99, "Rimnicu Vilcea": 80},
    "Fagarus": {"Sibiu": 99, "Bucharest": 211},
    "Bucharest": {"Pitesti": 97, "Urziceni": 85, "Giurgui": 90, "Fagarus": 211},
    "Giurgui": {"Bucharest": 90},
    "Urziceni": {"Hirsova": 98, "Bucharest": 85, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Vaslui": {"Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87},
    "Eforie": {"Hirsova": 86}
}

def BFS(source, goal):
    exploredCity = set()
    queue = [[source]]
    while queue:
        path = queue.pop(0)
        city = path[-1]
        if city == goal:
            return path
        if city not in exploredCity:
            exploredCity.add(city)
            for nextCity in graph[city]:
                new_path = list(path)
                new_path.append(nextCity)
                queue.append(new_path)
                
                
def DFS(source, goal):
    exploredCity = set()     
    stack = [(source, [source])] 
    while stack:
        (city, path) = stack.pop() 
        if city not in exploredCity:
            if city == goal:
                return path   
            exploredCity.add(city)
            for nextCity in graph[city]:
                stack.append((nextCity, path + [nextCity]))
    

source = "Arad"
goal = "Bucharest"

print("Depth First Search", DFS(source, goal))
print("Breadth First Search", BFS(source, goal))
