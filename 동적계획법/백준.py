def solution11726(num):
    a = [0] * 1000
    a[1] = 1
    a[2] = 2
    if num <= 2:
        print("2 이상의 숫자만 입력해주세요")
        return
    else:
        for i in range(3, num + 1):
            a[i] = a[i - 2] + a[i - 1]
    print(a[i])


# number = int(input())
# solution11726(number)

def solution9095(num):
    a = [0 for i in range(num + 1)]
    a[1] = 1
    a[2] = 2
    a[3] = 4
    if num < 4 or num >= 11:
        print("4 이상 10 이하의 숫자를 입력해주세요")
        return
    else:
        for i in range(4, num + 1):
            a[i] = a[i - 3] + a[i - 2] + a[i - 1]
    return a[i]


# number = int(input())
# print(solution9095(number))

# 1. 입력값에 따른 빈 리스트 만들기
# 2. 초기값을 설정
# 3. 점화식 기반으로 계산값 적용하기
# 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
def solution9461(num):
    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1

    for n in range(1, 98):
        dp[n + 3] = dp[n] + dp[n + 1]
    return print(dp[num])

number = int(input())
solution9461(number)
