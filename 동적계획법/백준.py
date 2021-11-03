def solution(num):
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


number = int(input())

solution(number)
