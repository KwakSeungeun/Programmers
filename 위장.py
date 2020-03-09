# 코딩테스트 연습(코딩테스트 고득점 Kit) > 해시 > 위장

from collections import deque

def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        key = cloth[1]
        if cloth[1] in dic: #1 : 의상 종류
            dic[key] += 1
        else:
            dic[key] = 1
    
    for val in dic.values():
        answer *= (val+1)
    
    return answer-1

def main():
    res = solution(		[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
    print("정답 : 3")
    print("결과 : " + str(res))


if __name__ == "__main__":
    main()
    