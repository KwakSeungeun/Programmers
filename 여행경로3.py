# 코딩테스트 연습(코딩테스트 고득점 Kit) > 깊이/너비 우선탐색 (DFS/BFS) > 여행경로

from collections import deque
import heapq

def solution(tickets):
    dic = {}
    for ticket in tickets:
        if ticket[0] in dic:
            heapq.heappush(dic[ticket[0]], ticket[1]) # Min Heap 사용해서 추가 시 알파벳 순으로 정렬
        else:
            dic[ticket[0]] = [ticket[1]]
    s = deque()
    s.append('ICN')
    path = []
    while s:
        cur = s[-1] # 끝에 값 가져옴 
        if cur not in dic or len(dic[cur])==0: # 다음 출발지가 없거나, 이미 다 사용한 경우
            path.append(s.pop())
        else:
            next = dic[cur][0]
            print(dic)
            del dic[cur][0]
            print(dic)
            print("--")
            s.append(next)       
    path.reverse() 
    return path


def main():
    # res = solution([["ICN", "BOO"], ["ICN", "COO" ], ["COO", "DOO" ], ["DOO", "COO" ], ["BOO", "DOO" ],["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]])
    # print('정답 : 	["ICN","BOO","DOO","BOO","ICN","COO","DOO","COO","BOO"]')
    # print("결과값 : " + str(res))
    # res = solution([["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"]])
    # print('정답 : 	["ICN", "JFK", "ICN", "JFK"]')
    # print("결과값 : " + str(res))
    res = solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]])
    print('정답 : 	[ICN -> COO -> ICN -> BOO -> DOO ]')
    print("결과값 : " + str(res))

if __name__ == '__main__':
    main()