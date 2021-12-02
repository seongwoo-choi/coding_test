# hash 함수를 이용해서 data 를 키로 변경
# 해시 함수로 입력 받은 키를 일관된 데이터로 변경
# 해시 테이블에 해시 함수를 통과한 해시 주소에 저장하고자 하는 value 를 저장한다.

hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Dave'))
print(hash_table)
