# 튜플
# 리스트와 비교가 중요
# 튜플 자료형 (순서, 중복, 수정X, 삭제X) # 불변

# 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))
# 원소가 하나일때는 끝이 콤마로 해야함 type((1)) => int형 나옴
print(type(a), type(b))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1]))

# 수정 X
# d[0] = 1500 오류가남

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산 : 튜플 원소 개수가 늘어나는 것은 허용
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
print('>>>>>')
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)
# 팩킹 : n개의 원소를 하나로 묶다
t = ('foo', 'bar', 'baz', ' qux')
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t
print(x1, x2, x3, x4)   # 묶여 있던 것을 각각 풀어서 변수에 할당
print(type(x1), type(x2), type(x3), type(x4))

# 팩킹 & 언팩킹
t2 = 1, 2, 3            # 팩킹
t3 = 4,                 # 팩킹
x1, x2, x3 = t2         # 언팩킹
x1, x5, x6 = 4, 5, 6    # 언팩킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x1, x5, x6)