import random

def selectedSort(data):
    for stand in range(len(data)-1):
        for index in range(stand+1, len(data)):
            if data[index] > data[stand]:
                data[stand], data[index] = data[index], data[stand]
    # data = data.reverse()
    return data

data = random.sample(range(100), 50)

print(selectedSort(data))