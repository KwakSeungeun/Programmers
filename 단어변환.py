# 코딩테스트 연습(코딩테스트 고득점 Kit) > 깊이/너비 우선탐색 (DFS/BFS) > 단어변환
 

from collections import deque

# 단순하게 find함수를 쓰면 중복되는 단어들을 체크하지 못함 
def isConvertible(src,tar):
    cnt = 0
    for (i,s) in enumerate(src):
        if s == tar[i]:
            cnt +=1
    
    if cnt == len(src)-1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = -1
    try :
        inx = words.index(target)
    except ValueError:
        return 0      

    print("시작 : " + str(inx))
    q = deque()
    q.append([inx])

    while q:
        cur = q.pop()
        curInx = cur[len(cur)-1]

        # 정답이 나온 경우
        if isConvertible(words[curInx], begin) and (answer > len(cur) or answer == -1):
            answer = len(cur)

        
        for (i,val) in enumerate(words):
            print("i,val = " + str(i) + ","+val)
            print(isConvertible(words[curInx],val))
            if cur.count(i) > 0 : # 이미 방문
                print("skip!")
                continue
            if isConvertible(words[curInx],val):
                print(words[curInx] +" -> "+val)
                temp = cur + [i]
                q.append(temp)

    if answer == -1 :
        answer = 0
    return answer

def main():
    # print("결과값 : " + str(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])))
    # print("정답: 0")
    
    # res = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    # print("\n\n결과값 : " + str(res))
    # print("정답: 4")

    # print("결과값 : " + str(solution("hot", "lot", ["hot", "dot", "dog", "lot", "log"])))
    # print("정답: 1")

    print("결과값 : " + str(solution("hit", "hhh",["hhh","hht"])))
    print("정답: 2")
if __name__ == '__main__':
    main()