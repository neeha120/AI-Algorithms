import numpy as np
n = int(input("Enter the size of the matrix (nxn): "))
print("Enter the start matrix: ")
start_matrix = np.zeros((n,n))
for i in range(n):
    start_matrix[i] = list(map(int, input().split()))

print("Enter the end matrix: ")
end_matrix = np.zeros((n,n))
for i in range(n):
    end_matrix[i] = list(map(int, input().split()))

visited = []
open = []
closed = []

closed.append(start_matrix)
def heuristic(matrix, end_matrix):
    res = matrix==end_matrix
    print("Heuristic value:", n*n - np.count_nonzero(res))
    return n*n - np.count_nonzero(res)

def possibleChildren(matrix, e_matrix):
    visited.append(matrix)
    [i],[j] = np.where(matrix == 0)
    direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
    children = []
    for dir in direction:
        ni = i + dir[0]
        nj = j + dir[1]
        newMatrix = matrix.copy()
        if(ni>=0 and ni<n and nj>=0 and nj<n):
            newMatrix[i,j], newMatrix[ni, nj] = matrix[ni,nj], matrix[i, j]
            if not(any(np.array_equal(newMatrix, i) for i in visited)):
                print("Child matrix heuristic value:", newMatrix)
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
                print("New matrix heuristic value:", newHeu)
                main(newMatrix, end_matrix)
        else:
            return False

main(start_matrix, end_matrix)

print(len(visited))