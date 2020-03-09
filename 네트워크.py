# 코딩테스트 연습(코딩테스트 고득점 Kit) > 깊이/너비 우선탐색 (DFS/BFS) > 네트워크

from collections import deque

class node:
    def __init__(self,i, j, val):
        self.i = i
        self.j = j
        self.val = val

def solution(n, computers):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False] * n for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(i,n):
            if visited[i][j]: 
                continue
            visited[i][j] = True
            if computers[i][j]==1 :
                answer += 1
                q.append(node(i,j,computers[i][j]))
                while j < n-1:
                    j += 1
                    visited[i][j] = True
                    if computers[i][j] == 1:
                        print("그 라인에 연결된 노드 추가 : ("+str(i) + " , " +str(j)+") ")
                        visited[j][j] = True
                        q.append(node(i,j,computers[i][j]))
                        q.append(node(j,j,computers[j][j]))
                print("bfs돌기전 : ")
                print(len(q))
                print(visited)
                while q:
                    cur = q.pop()
                    for dir in range(4):
                        x = cur.i + dx[dir]
                        y = cur.j + dy[dir]
                        print("(x,y) = ( " + str(x) + " , " + str(y) + " ) ")
                        if x<0 or y < 0 or y >= n or x >= n or visited[x][y]:
                            continue
                        if visited[x][y] == False:
                            if computers[x][y] == 1: 
                                print("dfs나아감")
                                q.append(node(x,y,computers[x][y]))
                            visited[x][y] = True
    return answer

def main():
    # result = solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])
    # print("예상 : 3")
    # print(result)
    # result = solution(4, [[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
    # print("예상 : 2")
    # print(result)
    result = solution(	4, [[1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1]])
    print("예상 : 1")
    print(result)
    # result = solution(	3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    # print("예상 : 1")
    # print(result)


if __name__ == '__main__':
    main()