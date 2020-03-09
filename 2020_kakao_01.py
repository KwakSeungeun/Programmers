def calcLength(src, size):
    res = ""
    for i in range(0,len(src)):
        # cnt = 1
        cur = src[i:i+size]
        print(cur)
    
    return len(res)


def solution(s):
    min = len(s) # 압축이 아닌 상태 초기 값
    for size in range(1,len(s)):
        temp = calcLength(s, size)         
        if min > temp:
            min = temp
    return min


def main():
    solution("aabbaccc")


if __name__ == '__main__':
    main()