import random


def factorial(num):
    if num == 1:
        return num
    elif num > 1:
        return num * factorial(num - 1)
    else:
        return num


def factorial2(num):
    if num <= 1:
        return num


def multiple(num):
    sum = 1
    for i in range(1, num):
        sum *= i + 1
    print(sum)


def multiple2(num):
    if num <= 1:
        return num
    return num * multiple2(num - 1)


def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])


# 회문이 되기 위해서는 슬라이싱 하여 비교된 값들이 같아야 한다.
# 즉, [:-1], [1:] 의 값들이 서로 같을 경우 회문이 된다.
def palindrome(data):
    if len(data) <= 1:
        print(data)
        return
    data2 = "".join(list(reversed(data[1:])))
    if data[:-1] == data2:
        print("palindrome")
    else:
        print("no palindrome")


# 회문을 재귀함수로 표현
def palindrome2(data):
    # 재귀함수가 끝나게 하기 위한 조건
    if len(data) <= 1:
        print("palindrome")
        return
    elif data[0] == data[-1]:
        # 1번 인덱스와 -2번 인덱스 비교
        return palindrome2(data[1:-1])
    else:
        return False


data = 'level'
# palindrome(data)
palindrome2(data)
