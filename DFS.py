graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # List for visited nodes.
    #Initialize a queue

def dfs(visited, graph, start, goal): #function for BFS
  visited.append(start)
  queue.append(start)
  

  

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
# Driver Code
start=input("Enter start state: ")
goal=input("Enter state to search: ")
print("Following is the Breadth-First Search")
bfs(visited, graph, start, goal)    # function calling