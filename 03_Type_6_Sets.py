# 집합

# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X, 수정O, 삭제O)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 4, 4, 4, 5, 6])  # 중복을 허용하지 않음
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
# {} : key: value 구조이면 dic // value만 있으면 set
e = {'foo', 'bar', 'bzz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))

# 합집합
print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))

# 차집합
print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인
# 교집합이 있으면 False / 없으면 True
print('s1 & s2', s1.isdisjoint(s2))

# 부분집합 확인
print('s1 & s2', s1.issubset(s2))
print('s1 & s2', s1.issuperset(s2)) # s1이 s2를 모두 포함할떄

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
s1.remove(4)
print('s1 - ', s1)
# 없는 원소 삭제시 KeyError 발생
s1.discard(3)
print('s1 - ', s1)

# remove 와 discard의 차이
# remove : 없는 원소 삭제시 KeyError 발생
# discard : 없는 원소 삭제해도 예외 발생 안함

# 전체삭제
s1.clear()
print('s1 - ', s1)