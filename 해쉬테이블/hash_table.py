# 0~9 데이터를 갖는 리스트를 만든다. => list comprehension
hash_table = list([i for i in range(10)])
print(hash_table)


# 해쉬 함수를 만드는 간단한 방식 => 나누기를 사용
# 어떤 키든 간에 5로 나눈 나머지를 가진다 => 고정된 길이로 값이 떨어진다.
def hash_func(key):
    return key % 5


# 파이썬의 딕셔너리와 유사한 형태가 된다.
def storage_data(data, value):
    # 키 생성
    key = ord(data[0])
    # 해쉬 함수에 키 값을 넣어 해쉬 주소 생성
    hash_address = hash_func(key)
    # 슬롯 생성, 슬롯에 value 값을 저장
    hash_table[hash_address] = value


def get_data(data):
    key = ord(data[0])
    # 입력받은 데이터의 해쉬 주소를 가져온다.
    hash_address = hash_func(key)
    return hash_table[hash_address]


# 각각에 데이터에 매칭되는 키값이 존재해야 한다.
# 키를 추출할 수 있는 별도의 함수가 존재할 수 있다.
data1 = 'Achoo'
data2 = 'Bad'
data3 = 'Concept'

# ord(): 문자의 아스키 코드를 리턴해주는 함수 => 영어나 특수문자만 코드화 가능
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))

# ord(data1[0]) 이 key 값이 된다.
# 추출된 키값을 hash_func(key) 에 넣으면 리턴된 값이 해쉬 주소가 된다.
print(hash_func(ord(data1[0])), hash_func(ord(data2[0])), hash_func(ord(data3[0])))

storage_data('Achoo', '01012341234')
storage_data('Bad', '01011111111')
storage_data('Concept', '01022222222')

print(get_data('Achoo'))
print(get_data('Bad'))
print(get_data('Concept'))
