import random

data = random.sample(range(100), 50)


def bubbleSort(data):
    for i in range(len(data) - 1):
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
    print(data)


def inserSort(data):
    for i in range(len(data) - 1):
        for index in range(i + 1, 0, -1):
            if data[index] < data[index - 1]:
                data[index], data[index - 1] = data[index - 1], data[index]
            else:
                break
    return data
