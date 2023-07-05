graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "E", "F"],
    "D": ["A", "F"],
    "E": ["B", "C", "H"],
    "F": ["D", "C", "G"],
    "G": ["H", "F", "K", "I"],
    "H": ["E", "G"],
    "I": ["J", "G"],
    "J": ["K", "I"],
    "K": ["G", "J"],
}

valueG = {
    "A": 50,
    "B": 31,
    "C": 29,
    "D": 38,
    "E": 22,
    "F": 21,
    "G": 0,
    "H": 10,
}

visited = set()
def findValue(elem):
    return valueG[elem]

def hillClimb(graph, visited, lst, start, end):
    lst.append(start)
    if start==end:
        print(lst)
        return True
    else:
        visited.add(start)
        node=''
        minH=100000
        for i in graph[start]:
            if i not in visited:
                if findValue(i)<minH:
                    minH = findValue(i)
                    node=i
        result=hillClimb(graph, visited, lst, node, end)
        if result:
            return True
    return False

hillClimb(graph, visited, [], 'A', 'G')