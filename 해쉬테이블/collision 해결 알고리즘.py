# 1. Chaining 기법 (Open Hashing 기법)
# 충돌이 발생하면 링크드 리스트 자료 구조를 사용하여 링크드 리스트로 추가로 뒤에 연결시키는 방법
# 2. Linear Probing 기법 (Close Hashing 기법)
# 충돌이 발생하면 해당 hash address 의 다음 address 부터 맨 처음 나오는 빈공간에 저장하는 기법

# data 가 존재하지 않으면 배열은 0이 된다.
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

# Chaining 기법
def chaining_save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        # 해쉬 주소가 동일한 경우 => 충돌 발생
        for index in range(len(hash_table[hash_address])):
            # 같은 키 값이 들어오면 데이터를 덮어씌운다. => 키값은 hash(data) 로 인해 같은 키값이 들어왔다는 것은 같은 데이터가 들어왔다는 것이다.
            # 그래서 같은 데이터가 다른 값을 다시 저장할 수 있기 때문에 고려해줘야한다.
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                # 함수 종료
                return
        # key 값이 다른 경우 => 링크드 리스트 자료구조 형태로 값을 이어주면 된다.
        hash_table[hash_address].append([index_key, value])
    # 해시 테이블에 값이 존재하지 않을 경우 해당 해시 주소에 데이터를 저장한다.
    else:
        hash_table[hash_address] = [[index_key, value]]

def chaining_read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 0 이면 데이터가 없는 것
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0]:
                return hash_table[hash_address][index][1]
            return None
    else:
        return None


# Linear Probing 기법

def linear_save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 해시 테이블에 값이 존재할 경우
    if hash_table[hash_address] != 0:

        # 해시 테이블을 순회
        for index in range(hash_address, len(hash_table)):
            # 해시 테이블의 값이 0 일 경우 비어있기 때문에 그 공간에 값을 집어 넣는다.
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            # 입력받은 키값이 해시 테이블에 존재하는 슬롯의 키값과 같으면 밸류를 업데이트 해준다.
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def linear_read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 해시 테이블에 값이 존재할 경우
    if hash_table[hash_address] != 0:
        # 해시 테이블을 순회
        for index in range(hash_address, len(hash_table)):
            # 해시 테이블의 값이 0 일 경우 데이터가 존재하지 않음
            if hash_table[index] == 0:
                return None
            # 해시 테이블의 키값이 입력받은 키값과 같을 경우
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None