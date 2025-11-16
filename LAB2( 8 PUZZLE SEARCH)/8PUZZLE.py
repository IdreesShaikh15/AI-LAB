goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

def get_neighbors(s):
    x, y = find_zero(s)
    out = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            t = [r[:] for r in s]
            t[x][y], t[nx][ny] = t[nx][ny], t[x][y]
            out.append(t)
    return out

def dfs(s, visited):
    if s == goal:
        return [s]
    visited.add(str(s))
    for nxt in get_neighbors(s):
        if str(nxt) not in visited:
            p = dfs(nxt, visited)
            if p:
                return [s] + p
    return None

def dls(s, goal, depth, path, visited):
    if s == goal:
        return path
    if depth == 0:
        return None
    visited.add(str(s))
    for nxt in get_neighbors(s):
        if str(nxt) not in visited:
            res = dls(nxt, goal, depth-1, path+[nxt], visited)
            if res:
                return res
    return None

def ids(start, goal, limit=20):
    for d in range(limit+1):
        visited = set()
        r = dls(start, goal, d, [start], visited)
        if r:
            return r
    return None

if __name__ == "__main__":
    start = [[1,2,3],
             [8,6,4],
             [0,7,5]]

    print("DFS:")
    sol1 = dfs(start, set())
    if sol1:
        print("Moves:", len(sol1)-1)
        for st in sol1:
            for r in st:
                print(r)
            print("-"*40)
    else:
        print("No solution.")

    print("\nIDS:")
    sol2 = ids(start, goal, 20)
    if sol2:
        print("Moves:", len(sol2)-1)
        for st in sol2:
            for r in st:
                print(r)
            print("-"*40)
    else:
        print("No solution.")

 
