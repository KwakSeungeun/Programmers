# 코딩테스트 연습(코딩테스트 고득점 Kit) > 해시 > 베스트앨범

#  중복된 경우를 해결하지 못함

def solution(genres, plays):
    answer = []
    dic = dict()
    cnt = dict()
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += [i]
            cnt[genres[i]] += plays[i]
        else:
            dic[genres[i]] = [i]
            cnt[genres[i]] = plays[i]
    cnt = sorted(cnt.items(),reverse=True,  key = lambda item: item[1])
    for val in cnt:
        key = val[0]
        cur = dic[key]
        if len(cur) == 1:
            answer += cur
            continue
        cur = sorted(cur, key=lambda x: plays[x])
        end = []
        for i in range(2):
            end.append(cur.pop())
        print(end)
        if plays[end[0]] == plays[end[1]]:
            end.sort()
        answer.extend(end)
    return answer


# 숏코딩
def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

def main():
    res = solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500])
    print("정답 : [4, 1, 0, 3]")
    print("결과 : " + str(res))
    # res = solution(	["classic", "test", "classic", "test", "classic", "classic","pop"], [1000, 500, 1000, 2500, 500, 500,100])
    # print("정답 : [3, 1, 4, 5,6]")
    # print("결과 : " + str(res))


if __name__ == "__main__":
    main()
    