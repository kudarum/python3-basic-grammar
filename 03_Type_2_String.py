# 문자형
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 타입
print(type(str1),type(str2),type(str3),type(str4))
# 길이
print(len(str1),len(str2),len(str3),len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드
\n : 개행
\t : 탭  
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""

# I'm Boy
print("I'm Boy")
print('I\'m Boy')
print('a\tb')
print('a\nb')
print('a\"\"b')
print('\000')

print()

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "What\'s on TV?"
print(escape_str2)

t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)

# Raw String 출력 : \ 신경안씀
raw_s = r'd:\python\test'
print(raw_s)

# 멀티라인 입력 : 역슬러쉬(\)를 사용해라
multi_str = \
'''
문자열 
멀티라인 입력
테스트
'''
print(multi_str)

# 문자열 연산
str_o1 = "pythonpython"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

# * : 늘어남
print(str_o1 * 3)
# + : 연결
print(str_o1 + str_o2)
# in : 찾기 (a in b b안에 a가 포함되어 있어요?)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startwith, count, endswith, isalpha...)
# 첫글자 대문자 변경
print("Capitalize: ", str_o1.capitalize())
# 끝 글자가 s로 끝나는가?
print("endswith : ", str_o2.endswith("s"))
# 문자열 변경
print("replace : ", str_o1.replace("thon","Good"))
# 정렬되서 리스트 형태로 반환
print("sorted : ", sorted(str_o1))
print("split : ", str_o4.split(" "))


# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__ 가 있으면 반복이 가능하다, 자르는 처리가 가능하다.
for i in im_str:
    print(i)

print()

# 슬라이싱
#         9876543210 (음수)
#         0123456789
str_s1 = "NicePython"
print(len(str_s1))
print(str_s1[0:3])  # 0 부터 3번 전까지 나옴 : 0,1,2
print(str_s1[5:11]) # Python
print(str_s1[5:])   # 5부터 끝까지 가져와 Python
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[1:9:2])    # 1부터 8자리까지 2칸씩 건너띄어서 가져와라 1,3,5,7 번지 문자 반환
print(str_s1[-5:])  # 음수는 오른쪽 부터 자리수
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-3]) # 오른쪽 부터 3번지씩 건너띄어서 가져와라 0, -3, -6, -9

print()

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a))   # 아스키 코드출력 z -> 122
print(chr(122)) # 아스키 코드를 문자로 변경 122 -> z

