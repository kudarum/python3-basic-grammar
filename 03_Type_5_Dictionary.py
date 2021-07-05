# 딕셔너리
# 딕셔너리 자료형 (순서 X, 키 중복 X, 수정 O, 삭제 O)

# 선언
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33)
])

f = dict(
    Name='Nice',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
# print('a - ', a['name1'])       # 오류가 나옴
print('a - ', a.get('name1'))   # None가 나옴 get을 훨씬 많이 사용함
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 추가
a['address'] = 'Seoul'  # 추가
print('a - ', a)
a['name'] = 'Seoul' # 수정
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# key의 개수
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# 함수 (dict_keys, dict_values, dict_items : 주로 반복문에서 사용 가능)
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a) # birth라는 키가 a에 있나요? True, False
print('a - ', 'City' in a)

# 수정
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

temp = {'address':'Busan'}
a.update(temp)
print('a - ', a)

