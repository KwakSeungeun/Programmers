# 코딩테스트 연습(코딩테스트 고득점 Kit) > 깊이/너비 우선탐색 (DFS/BFS) > 여행경로
# !!! <중복>에 대한 언급이 없다면 같은 데이터가 존재한다는 가정을 해야함 !!!

from collections import deque
import copy

# inx=0 출발지
def findCity(startCity, tickets, path):
    res = []
    for ticket in tickets:
        if ticket[0] == startCity and path.count(ticket) < tickets.count(ticket):
            res.append(ticket)
    return res

def solution(tickets):
    answer = []
    reslist = []
    q = deque()

    # 초기 설정
    startTickets = findCity("ICN", tickets, [])
    for t in startTickets:
        q.append([t])

    while q:
        curPath = q.popleft()
        curTicket = curPath[len(curPath)-1]
        nextTickets = findCity(curTicket[1], tickets, curPath)
        if len(tickets) == len(curPath) and len(nextTickets) == 0 : 
            if len(reslist) != 0: #알파벳 순서 비교
                for i in range(len(tickets)):
                    print(reslist[i][1] > curPath[i][1])
                    if reslist[i][1] > curPath[i][1]:
                        reslist = copy.deepcopy(curPath)
                        break
                    elif reslist[i][1] < curPath[i][1]:
                        break
            else:
                print(reslist)
                reslist = copy.deepcopy(curPath)
        for next in nextTickets:
            temp = copy.deepcopy(curPath)
            temp.append(next)
            q.append(temp)

    answer.append("ICN")
    for val in reslist:
        answer.append(val[1])
    return answer


def main():
    res = solution([["ICN", "BOO"], ["ICN", "COO" ], ["COO", "DOO" ], ["DOO", "COO" ], ["BOO", "DOO" ],["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])
    print('정답 : 	["ICN","BOO","DOO","BOO","ICN","COO","DOO","COO","BOO"]')
    print("결과값 : " + str(res))

if __name__ == '__main__':
    main()