def gcd(x, y):
    if y==0:
        return x
    return gcd(y, x%y)

def bfs(start, x_full, y_full, goal, queue, visited):
    queue.append(start)
    path = []
    while len(queue)!=0:
        state=queue.pop()
        visited.append(state)
        path.append(state)

        x, y = state
        if x==goal or y==goal:
            return path
        if state[0]<x_full and not ([x_full, state[1]] in visited):
            queue.append([x_full, state[1]])
        if state[1]<y_full and not ([state[0], y_full] in visited):
            queue.append([state[0], y_full])
        if state[0]>0 and not([0, state[1]] in visited):
            queue.append([0, state[1]])
        if state[1]>0 and not([state[0], 0] in visited):
            queue.append([state[0], 0])
        if (x+y>=x_full) and (y>0) and not([x_full, y-(x_full-x)] in visited):
            queue.append([x_full, y-(x_full-x)])
        if (x+y>=y_full) and (x>0) and not([x-(y_full-y), y_full] in visited):
            queue.append([x-(y_full-y), y_full])
        if (x+y>0) and (x+y<=x_full) and (y>=0) and not([x+y, 0] in visited):
            queue.append([x+y, 0])
        if (x+y>0) and (x+y<=y_full) and (x>=0) and not([0, x+y] in visited):
            queue.append(0, x+y)
    return "Not Found"

def water(x,y,goal):
    start=[0,0]
    if goal%gcd(x, y)==0:
        return bfs(start, x, y, goal, [], [])

print(water(2,3,1))