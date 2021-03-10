# Print 사용법

# 1. 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

# 2. Option

# 2.1. separator 옵션
# 연결을 어떻게 할 건지
print('P','y','t','h','o','n', sep='')
print('010', '1111', '2222', sep='-')
print('python','google.com', sep='@')

# 2.2. end 옵션
# 마지막 부분을 어떻게 처리할 건지
print('Welcome to', end='\n')
print('IT News', end=' ')
print('Web Site')

# 2.3. file 옵션
import sys
#print('Learn Python', file='test.txt')
print('Learn Python', file=sys.stdout)

# 3. format 옵션 (d, s, f)
# d : 정수 3
# s : 문자열 'python'
# f : 실수 3.14
print('%s %s' % ('one','two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))

# %s
# 10 : 10개의 자리수 (양수 : 왼쪽 공백, 음수 : 오른쪽 공백)
# 10개 자리수에 'nice'채우고 나머지는 왼쪽부터 공백 채운다
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) # 공백 대신 다른 글자 추가
print('{:^10}'.format('nice')) # 중앙정렬


print('%5s' % ('pythonstudy'))
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # 5글자 절삭
print('{:.5}'.format('pythonstudy')) # 5글자 절삭
print('{:10.5}'.format('pythonstudy')) # 10개의 공간이 있지만 5글자만 나오게 절삭하라

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%f' % (3.1415296535893))
print('{:f}'.format(3.1415296535893))
print('%1.5f' % (3.1415296535893)) # 정수부 1자리, 소수부 5자리까지

print('%06.2f' % (3.1415296535893)) # 총 6자리 중에 소수부 2자리
print('{:06.2f}'.format(3.1415296535893))