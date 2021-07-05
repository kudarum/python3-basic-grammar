# while
# while <expr>:
#   <statement(s)>

# 예1
n = 5
while n > 0:
    n = n - 1
    print(n)

# 예2
a = ['foo', 'bar', 'baz']
while a:    # a 원소 수만큼 반복 X, a가 데이터가 있으니 True O
    print(a.pop())

# 예3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# 예4
# break, continue
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

# if 중첩
# 예5
i = 1
while 1 <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1

# while - else 구문
# 예6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

# 예7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')

# 예8
a = ['foo', 'bar', 'baz', 'qux']

while True:
    if not a:
        break
    print(a.pop())