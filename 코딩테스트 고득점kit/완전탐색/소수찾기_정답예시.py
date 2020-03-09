# 코딩테스트 연습(코딩테스트 고득점 Kit) > 완전탐색 > 소수찾기
from itertools import permutations

def solution(s):
    answer = 0

    new_s = list(s)
    for i in range(2,len(s)+1):
        pm = list(permutations(s, i))
        for j in pm:
            if len(j) <= len(s):
                new_s.append(''.join(j))
    print(new_s)
    new_s = list(set(map(lambda x: int(x), new_s)))
    print(new_s)
    
    if new_s.count(1):
        new_s.remove(1)
    if new_s.count(0):
        new_s.remove(0)

    for x in new_s:
        i = 2
        while i*i <= x: 
            if x % i == 0:
                answer -= 1
                break
            i+=1
        answer += 1
    
    return answer

def main():
    res = solution("011")
    print("정답 : 2")
    print("결과 : " + str(res))
    # res = solution("17")
    # print("정답 : 3")
    # print("결과 : " + str(res))
    # res = solution("0001")
    # print("정답 : 0")
    # print("결과 : " + str(res))




if __name__ == "__main__":
    main()
    