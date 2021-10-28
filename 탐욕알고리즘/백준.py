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
def get_min_time(person, person_list):
    total_time = 0
    person_list = sorted(person_list)
    for index in range(person):
        for time in range(index + 1):
            total_time += person_list[time]

    print(total_time)


person = int(input())
person_list = list(map(int, input().split()))
get_min_time(person, person_list)
