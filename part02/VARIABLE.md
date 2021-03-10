# 1. Variable
## 1.1. Variable 란
객체를 가리키는 것!!
(객체 : Python에서 사용되는 모든 것)
## 1.2. 기본문법
```python
# 기본 선언
var = 1000
# 동시 선언
x = y = z = 1000
# 재 선언
x = 500
```
## 1.3. Python 값 할당 방식
* Call By Object Referecnes
    - 1, 2 등의 숫자부터 시작해 모든 것이 객체이며 하나의 개체는 단 하나의 인스턴스로 존재한다(싱글톤).
    - 예를들면 a = 2 라고 변수를 할당하면 2라는 값이 a가 가르키는 메모리 공간에 할당되는 것이 아니라 2라는 인스턴스의 주소 값을 a가 가르키고 있는 것
    - 정리하면 Python에서 모든 것은 객체이고 각 객체는 하나의 인스턴스를 갖는다.
    
* 예시
```python
# m 과 n은 서로 다른 객체(100, 1000)를 가리키고 있다
m = 100
n = 1000
print(id(m) == id(n)) # False
# m과 n은 서로 같은 객체를 가리키고 있다.
m = 100
n = 100
print(id(m) == id(n)) # True
```
## 1.4. 다양한 변수 선언 방법
* Camel Case : numberOfCollageGraduates -> Method 선언
* Pascal Case : NumberOfCollageGraduates -> Class 선언
* snake Case : number_of_collage_graduates -> python 변수 선언
* 주의 : 예약어는 변수명으로 사용 불가능
  - 예) for = 3, as = 3, class = 3
  
# 2. Type
## 2.1. 변수 타입 종류
* int : 정수
* float : 실수
* complex : 복소수
* bool : 불린
* str : 문자열(시퀀스)
* list : 리스트(시퀀스)
* tuple : 튜플(시퀀스)
* set : 집합
* dict : 사전
## 2.2. 변수 타입별 선언
### 2.2.1 기본 선언
```python
int_v = 7           # int
float_v = 10.0      # float
str1 = "Python"     # str type
str2 = "Anconda"    # str type
bool = False        # bool type
list = [str1, str2] # list
dict = {
    "name" : "Machine Learning"
    , "version" : 2.0
}                   # dict
tuple = (7, 8, 9)   # tuple = 7, 8, 9
set = {7, 8, 9}     # set
```
### 2.2.2 Integer (정수) / Float (실수)
* 선언
```python
# 정수 선언
i = 77
i2 = -14
# 큰 숫자도 가능함
big_int = 122123123019402971510984021984

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9
```
* 연산
```python
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
```
> `<출력결과>` </br>
> i1 + i2 :  978 </br>
> f1 + f2 :  5.173 </br>
> big_int1 + big_int2 :  901688100258629830 </br>
>  </br>
> i1 * i2 :  36621 </br>
> f1 * f2 :  4.860726 </br>
* 형변환
```python
a = 3.0
b = 6
c = 0.7
d = 12.7
print(type(a), type(b), type(c), type(d))

print(float(b))     # 정수 -> 실수 형변환
print(int(c))       # 실수 -> 정수 형변환
print(int(d))       # 실수 -> 정수 형변환
print(int(True))    # True : 1 // False : 0
print(float(False))
print(complex(3))   # 복소수 형변환
print(complex('3')) # 문자형 -> 순자형 형변환 후 수행됨
print(complex(False))
```
> `<출력결과>`</br>
> <class 'float'> <class 'int'> <class 'float'> <class 'float'></br> 
> 6.0 </br>
> 0 </br>
> 12 </br>
> 1 </br>
> 0.0 </br>
> (3+0j) </br>
> (3+0j) </br>
> 0j </br>

### 2.2.3. String (문자)
* 기본 선언
```python
# 기본 선언 형태
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''
# 빈 문자열
str1_t1 = ''
str2_t2 = str()
```
* Escape 문법
  - \n  : 개행
  - \t : 탭  
  - \\ : 문자
  - \' : 문자
  - \" : 문자
  - \000 : 널 문자
  
`backslash(\)`