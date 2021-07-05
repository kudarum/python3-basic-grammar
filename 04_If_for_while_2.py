# for
# for in <collection>
#   <loop body>

for v1 in range(10):    # 0 ~ 9
    print('v1 is :', v1)

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)

for v3 in range(1, 11, 2):  # 1, 3, 5, 7, 9
    print('v3 is :', v3)

# 1 ~ 1000 까지의 합
sum1 = 0
for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum:', sum1)
print('1 ~ 1000 Sum:', sum(range(1, 1001)))
print(type(range(1, 11)))
print('1 ~1000 4의 배수의 합', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('name :', name)

# 예2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print('Current number :', n)

# 예3
word = "Beautiful"
for s in word:
    print('word :', s)

# 예4
my_info = dict(
    name='Lee',
    age=33,
    city='Seoul'
)

for k in my_info:
    print('Key :', k)
for k in my_info:
    print('Value :', my_info.get(k))

for v in my_info.values():
    print('Value :', v)

for v in my_info.items():
    print('Item :', v)

# 예5
name = 'FineAppLE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print('Found : 34!!')
        break
    else:
        print('Not Found :', num)


# continue
lt = ["1", 2, 5, True, 4.2, complex(4)]
for v in lt:
    if type(v) is bool:     # 자료형 대조시 is 사용
        continue
    print('current type :', type(v))
    print('multiply by 2', v * 3)

# for - else
# for 문의 모든 반복을 수행했을 떄 else 수행
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 23:
        print('Found : 23')
        break
else:
    print('Not Found : 23')

# 구구단 출력
for i in range(2,10):
    for j in range(1, 10):
        print(''+str(i)+' * '+ str(j)+' :', i*j)

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))  # 순서 X


