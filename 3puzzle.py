import numpy as np

start_matrix = np.array([[1,2],[0,3]])
end_matrix =   np.array([[1,2],[3,0]])

visited = []
open = []
closed = []

closed.append(start_matrix)

def heuristic(matrix, end_matrix):
    res = matrix==end_matrix
    return 4 - np.count_nonzero(res)

def possibleChildren(matrix, e_matrix):
    visited.append(matrix)
    [i],[j] = np.where(matrix == 0)
    direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
    children = []
    for dir in direction:
      ni = i + dir[0]
      nj = j + dir[1]
      newMatrix = matrix.copy()
      if(ni>=0 and ni<=1 and nj>=0 and nj<=1):
          newMatrix[i,j], newMatrix[ni, nj] = matrix[ni,nj], matrix[i, j]
          if not(any(np.array_equal(newMatrix, i) for i in visited)):
              visited.append(newMatrix)
              newMatrix_heu = heuristic(newMatrix, end_matrix)
              children.append([newMatrix_heu, newMatrix])
    children = sorted(children, key = lambda x:x[0])
    for i in range(len(children)):
        children[i]=children[i][1]

    return children

def main(start_matrix, end_matrix):
    start_heuristic = heuristic(start_matrix, end_matrix)
    if start_heuristic==0:
        for node in closed:
            print(node)
        return True
    else:
        children = possibleChildren(start_matrix, end_matrix)
        if(len(children)>0):
            for i in range(len(children)):
                open.insert(i, children[i])

        if len(open)>0:
            newHeu = heuristic(open[0], end_matrix)
            newMatrix = open[0]
            closed.append(open[0])
            open.pop(0)

            if newHeu==0:
                for node in closed:
                    print(node)
                return True
            else:
                main(newMatrix, end_matrix)
        else:
            return False

main(start_matrix, end_matrix)