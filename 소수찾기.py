# 코딩테스트 연습(코딩테스트 고득점 Kit) > 완전탐색 > 소수찾기

def checkprime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def makenum(src):
    if len(src) == 1 :
        return src
    res = []
    cur = src[0]
    res.append(cur)
    back = makenum(src[1:])
    if len(back) == 1:
        res.append(back)
    for temp in back:
        res.append(cur + temp)
        res.append(temp + cur)
    return res
    

def solution(numbers):
    answer = 0
    # 조합 만들기 --> O(N^2)
    numlist = makenum(numbers)
    print(numlist)

    # 조합 list 소수 체크해서 count --> O(N^2)
    visited = [False for _ in range(10000000)]
    for num in numlist:
        if visited[int(num)]==False and checkprime(int(num)):
            visited[int(num)] = True
            answer += 1
    return answer

def main():
    res = solution("011")
    print("정답 : ")
    print("결과 : " + str(res))


if __name__ == "__main__":
    main()
    