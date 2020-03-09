# 코딩테스트 연습(코딩테스트 고득점 Kit) > 스택/큐 > 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    curWeight = 0
    time = 0
    while len(truck_weights) > 0:
        time += 1
        n = len(truck_weights)-1
        while curWeight + truck_weights[n] <= weight:
            truck_weights.pop()
            n -= 1
    return answer

def main():
    res = solution(	2, 10, [7, 4, 5, 6] )
    print("정답 : 8")
    print("결과 : " + str(res))
    # res = solution(	100, 100, [10] )
    # print("정답 : 101")
    # print("결과 : " + str(res))
    # res = solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] )
    # print("정답 : 110")
    # print("결과 : " + str(res))


if __name__ == "__main__":
    main()
    