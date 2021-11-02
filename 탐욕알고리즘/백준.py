# 백준 5585
def solution5585(value, coin_list):
    coin_list = sorted(coin_list, reverse=True)
    total_num = 0
    for coin in coin_list:
        coin_num = value // coin
        total_num += coin_num
        value -= coin * coin_num
    return total_num


# value = 1000 - int(input())
# coin_list = [1, 10, 500, 100, 50, 5]
# print(solution5585(value, coin_list))


# 백준 11399
def solution11399(person, person_list):
    total_time = 0
    person_list = sorted(person_list)
    for loop in range(person):
        for index in range(loop + 1):
            total_time += person_list[index]
    return total_time


# person = int(input())
# person_list = list(map(int, input().split()))
# print(solution11399(person, person_list))

# 백준 1789
def solution1789(s):
    for n in range(s):
        a = n * (n + 1) / 2
        print(">>>>", n, a)
        if a <= s:
            pass
        elif a > s:
            return n - 1


s = int(input())
print(solution1789(s))
