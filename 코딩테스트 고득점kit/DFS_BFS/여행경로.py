# 코딩테스트 연습(코딩테스트 고득점 Kit) > 깊이/너비 우선탐색 (DFS/BFS) > 여행경로

from collections import deque

# inx=0 출발지
def findCity(city, tickets,visited):
    des = "ZZZ"
    row = -1
    for (i,arr) in enumerate(tickets):
        if visited[i]:
            continue
        if arr[0] == city and arr[1] < des:
            des = arr[1]
            row = i
            continue
    return row

def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))]
    q = deque()
    startRow = findCity("ICN", tickets,visited)
    q.append(startRow)
    answer += ["ICN", tickets[startRow][1]]

    resLen = len(tickets) + 1
    print("결과 길이 : " + str(resLen))

    while q:
        curRow = q.pop()
        desCity = tickets[curRow][1]
        visited[curRow] = True
        
        res = findCity(desCity, tickets, visited)
        if visited[res] == False: # 경유 가능
            answer += [tickets[res][1]]
            visited[res] = True
            q.append(res)
            
    return answer


def main():
    res = solution([["ICN", "BOO"], ["ICN", "COO" ], ["COO", "DOO" ], ["DOO", "COO" ], ["BOO", "DOO" ],["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])
    print('정답 : 	[ICN-BOO-DOO-BOO-ICN-COO-DOO-COO-BOO]')
    print("결과값 : " + str(res))

if __name__ == '__main__':
    main()