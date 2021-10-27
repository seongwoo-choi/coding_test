def test(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        # coin 종류와 몇 개를 사용했는지
        details.append([coin, coin_num])
    return total_coin_count, details


coin_list = [1, 50, 100, 500]
value = 4720
print(test(value, coin_list))


# 무게 제한이 k 인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# 각 물건은 무게와 가치로 표현된다.
# 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있다.
def get_max_value(capacity, data_list):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()
    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            print(capacity)
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details


# 각 각 무게와 가치
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
print(get_max_value(30, data_list))


# 백준 11399
person = 5
person_list = [3, 1, 4, 3, 2]

def get_min_time(person, time_list):
    total_time = 0
    time_list = sorted(time_list)
    for index in range(person):
        for time in range(index+1):
            total_time += time_list[time]

    print(total_time)

get_min_time(person, person_list)
