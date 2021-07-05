# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"     # str type
bool = False        # bool type
str2 = "Anconda"    # str type
float_v = 10.0        # float
int_v = 7             # int
list = [str1, str2] # list
dict = {
    "name" : "Machine Learning"
    , "version" : 2.0
}
tuple = (7, 8, 9)   # tuple = 7, 8, 9
set = {7, 8, 9}


print(type(str1))
print(type(bool))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

print()

#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pwo(x,y) : x의 y제곱 (x ** y)
"""

# 정수 선언
i = 77
i2 = -14
big_int = 122123123019402971510984021984
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산
i1 = 39
i2 = 939
big_int1 = 777777817239182739
big_int2 = 123910283019447091
f1 = 1.234
f2 = 3.939

# +
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print()
# *
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print()

# 형 변환 실습
a = 3.0
b = 6
c = 0.7
d = 12.7
print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True))    # True : 1 // False : 0
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 -> 순자형 형변환 후 수행됨
print(complex(False))

# 수치연산
print(abs(-7))
# 목, 나머지
x, y = divmod(100,8)
print(x,y)
print(pow(5,3), 5 ** 3)


# 외부 모듈
import math
print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 수
print(math.pi)  # 원주율