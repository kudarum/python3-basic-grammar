# 리스트
# 리스트 자료형 (순서, 중복, 수정, 삭제)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('e - ', e[-1][1]) # e의 -1번 쨰는 List형이고 그 List의 1번쨰
print('e - ', list(e[-1][1]))   # 문자열이 한글자씩 분해되서 List가 된다

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])    # 0 부터 3까지 나와라
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print('>>>>>')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)
temp = c
print(temp, c)
print(id(temp) == id(c))
temp.pop(0) # temp, c에서 모두 삭제됨 (깊은복사, 얕은복사)
print(temp, c)

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']    # 1번쨰 값 위치에 a,b,c 각각 추가됨
print('c - ', c)
c[1:2] = [['a', 'b', 'c']]  # 1번째 값 위치에 ['a', 'b', 'c'] 리스트 변경됨
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)

del c[2]    # 삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10) # list 끝에 추가
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)  # 두번쨰 위치에 7을 추가할거야
print('a - ', a)
a.reverse()
print('a - ', a)
a.remove(10)    # 내가 제거할 값
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))   # a에 값 4가 몇개 있느냐? 내가 찾는 값이 이안에 몇개가 중복되어 있는지?

ex = [8, 9]
a.extend(ex)    # a를 연장한다
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문
while a:
    data = a.pop()
    print(data)