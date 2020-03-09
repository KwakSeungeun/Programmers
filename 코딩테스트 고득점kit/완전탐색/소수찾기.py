# 코딩테스트 연습(코딩테스트 고득점 Kit) > 완전탐색 > 소수찾기
# for 문에서 함수호출이 효율적이진 않음
from itertools import permutations

def solution(numbers):
    answer = 0
    numlist = list()
    for n in range(1, len(numbers)+1):
        temp = ["".join(i) for i in permutations(numbers,n)]
        numlist.extend(temp)
    numlist = list(set(map(lambda x: int(x), numlist)))
    print(numlist)
    
    for num in numlist:
        if num == 1 or num == 0:
            continue
        i = 2
        while i*i < num:
            if num%i == 0:
                answer -= 1
                break
            i += 1
        answer += 1
    return answer

def main():
    # res = solution("011")
    # print("정답 : 2")
    # print("결과 : " + str(res))
    res = solution("17")
    print("정답 : 3")
    print("결과 : " + str(res))
    # res = solution("0001")
    # print("정답 : 0")
    # print("결과 : " + str(res))




if __name__ == "__main__":
    main()
    