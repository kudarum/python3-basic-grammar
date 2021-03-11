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
## 2.3. Integer (정수) / Float (실수)
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

## 2.4. String (문자)
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
```python
print("I'm Boy")
print('I\'m Boy')
print('a\tb')
print('a\nb')
print('a\"\"b')
print('\000')
```
> `<출력결과>`</br>
> I'm Boy </br>
> I'm Boy </br>
> a	b </br>
> a </br>
> b </br>
> a""b </br>
> (공백)</br>

* Raw String : \ 신경 안씀
```python
# 기본 선언 : r를 앞에 추가한후 작성
raw_s = r'd:\python\test'
print(raw_s)
```
> `<출력결과>`</br>
> d:\python\test

* 멀티라인 입력 : 역슬러쉬(\\)를 이용해라
```python
multi_str = \
'''
문자열 
멀티라인 입력
테스트
'''
```
> `<출력결과>`</br>
> 문자열  </br>
> 멀티라인 입력 </br>
> 테스트 </br>

* 문자열 연산
```python
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
```
> `<출력결과>`</br>
> pythonpythonpythonpythonpythonpython</br>
> pythonpythonApple</br>
> True</br>
> False</br>
> True</br>
* 문자열 형변환
```python
# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
```
> `<출력결과>`</br>
> 66 <class 'str'></br>
> 10.1 <class 'str'></br>
> True <class 'str'></br>

* 문자열 함수 (upper, isalnum, startwith, count, endswith, isalpha...)
```python
str_o1 = "pythonpython"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

# 첫글자 대문자 변경
print("Capitalize: ", str_o1.capitalize())
# 끝 글자가 s로 끝나는가?
print("endswith : ", str_o2.endswith("s"))
# 문자열 변경
print("replace : ", str_o1.replace("thon","Good"))
# 정렬되서 리스트 형태로 반환
print("sorted : ", sorted(str_o1))
print("split : ", str_o4.split(" "))
```
> `<출력결과>`</br>
> Capitalize:  Pythonpython</br>
> endswith :  False</br>
> replace :  pyGoodpyGood</br>
> sorted :  ['h', 'h', 'n', 'n', 'o', 'o', 'p', 'p', 't', 't', 'y', 'y']</br>
> split :  ['Seoul', 'Deajeon', 'Busan', 'Jinju']</br>

* 반복(시퀀스)
```python
im_str = "Good Boy!"
print(dir(im_str)) # __iter__ 가 있으면 반복이 가능하다, 자르는 처리가 가능하다.
for i in im_str:
    print(i)
```
> `<출력결과>`</br>
> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']</br>
> G </br>
> o </br>
> o </br>
> d </br>
>
> B </br>
> o </br>
> y </br>
> ! </br>

* 슬라이싱
```python
str_s1 = "NicePython"
print(len(str_s1))
print(str_s1[0:3])  # 0 부터 3번 전까지 나옴 : 0,1,2
print(str_s1[5:11]) # Python
print(str_s1[5:])   # 5부터 끝까지 가져와 Python
print(str_s1[:len(str_s1)]) # str_s1[:11]
print(str_s1[1:9:2])# 1부터 8자리까지 2칸씩 건너띄어서 가져와라 1,3,5,7 번지 문자 반환
print(str_s1[-5:])  # 음수는 오른쪽 부터 자리수
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-3]) # 오른쪽 부터 3번지씩 건너띄어서 가져와라 0, -3, -6, -9
```
> `<출력결과>`</br> 
> 10</br>
> Nic</br>
> ython</br>
> ython</br>
> NicePython</br>
> ieyh</br>
> ython</br>
> icePyth</br>
> NcPto</br>
> nteN</br>

* 아스키 코드(또는 유니코드)
```python
a = 'z'
print(ord(a))   # 아스키 코드출력 z -> 122
print(chr(122)) # 아스키 코드를 문자로 변경 122 -> z
```

## 2.5 List
List 자료형의 특징 (순서, 중복, 수정, 삭제)
* 기본 선언
```python
a = []
b = list()
c = [70, 75, 80, 85]
# 서로 다른 자료형도 구성 가능
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]
```

* 인덱싱
```python
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('e - ', e[-1][1])         # e의 -1번 쨰는 List형이고 그 List의 1번쨰
print('e - ', list(e[-1][1]))   # 문자열이 한글자씩 분해되서 List가 된다
```
> `<출력결과>`</br> 
> d -  <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captine']</br> 
d -  10000</br> 
d -  21000</br> 
e -  Base</br> 
e -  ['B', 'a', 's', 'e']</br> 

* 슬라이싱
```python
print('d - ', d[0:3])    # 0 부터 3까지 나와라
print('d - ', d[2:])     # 2 부터 끝까지 나와라
print('e - ', e[-1][1:3])
```
> `<출력결과>`</br> 
> d -  [1000, 10000, 'Ace']</br> 
> d -  ['Ace', 'Base', 'Captine']</br> 
> e -  ['Base', 'Captine']</br> 

* 리스트 연산
```python
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))
```
> `<출력결과>`</br> 
> c + d [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captine']</br> 
> c * 3 [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]</br> 
> 'Test' + c[0] Test70</br> 

* 값 비교
```python
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
```
> `<출력결과>`</br> 
> True</br>
> [70, 75, 80, 85]</br>
> [70, 75, 80, 85]</br>

* Identity(id)
```python
temp = c
print(temp, c)
print(id(temp) == id(c))
temp.pop(0) # temp, c에서 모두 삭제됨 (깊은복사, 얕은복사)
print(temp, c)
```
> `<출력결과>`</br> 
> [70, 75, 80, 85] [70, 75, 80, 85]</br> 
> True</br> 
> [75, 80, 85] [75, 80, 85]</br>
 
* 리스트 수정, 삭제
```python
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
```
> `<출력결과>`</br> 
> c -  [4, 80, 85]</br> 
> c -  [4, 'a', 'b', 'c', 85]</br> 
> c -  [4, ['a', 'b', 'c'], 'b', 'c', 85]</br> 
> c -  [4, ['a', 'b', 'c'], 'b', 'c', 85]</br> 
> c -  [4, 'c', 85]</br> 
> c -  [4, 'c']</br> 

* 리스트 함수
> a = [5, 2, 3, 1, 4]

* append : list 끝 자리에 데이터 추가

```python
a.append(10) # list 끝에 추가
print('a - ', a)
```
> `<출력결과>`</br> 
> a -  [5, 2, 3, 1, 4]

* sort : list 데이터 정렬
```python
a.sort()
print('a - ', a)
```
> `<출력결과>`</br> 
> a -  [5, 2, 3, 1, 4, 10]

* reverse : list 데이터 역정렬
```python
a.reverse()
print('a - ', a)
```
> `<출력결과>`</br> 
> a -  [10, 5, 4, 3, 2, 1]

* insert : 원하는 위치에 데이터 추가
```python
a.insert(2, 7)  # 두번쨰 위치에 7을 추가할거야
print('a - ', a)
```
> `<출력결과>`</br> 
> a -  [10, 5, 7, 4, 3, 2, 1]

* remove : 원하는 데이터 제거
```python
a.remove(10)    # 내가 제거할 값
print('a - ', a)
```
> `<출력결과>`</br> 
> a -  [1, 2, 3, 4, 7, 5]
 
* pop : 끝에서 하나씩 제거하고, 제거할 대상인 데이터 리턴
```python
print('a - ', a.pop())
print('a - ', a)
```
> `<출력결과>`</br>
> a - 5
> a -  [1, 2, 3, 4, 7]

* count : 데이터가 몇개 있는가?
```python
# a에 값 4가 몇개 있느냐? 내가 찾는 값이 이안에 몇개가 중복되어 있는지?
print('a - ', a.count(4))   
```
> `<출력결과>`</br>
> a -  1

* extend : 리스트를 연장한다
```python
ex = [8, 9]
a.extend(ex)    # a를 연장한다
print('a - ', a)
```
> `<출력결과>`</br>
> a -  [1, 2, 3, 4, 8, 9]

* 삭제 기능은 remove, pop, del 이 있음

## 2.6. Tuple
리스트와 비교가 중요함<br/>
**수정이 불가능함 (단 원소 개수가 늘어나는 것은 허용됨)**<br/>
특징 : 순서 O, 중복 O, 수정 X, 삭제 X (불변!) <br/>

* 기본 선언
```python
a = ()
# 원소가 하나일때는 끝이 콤마로 해야함 type((1)) => int형 나옴
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))
```

* 인덱싱
```python
print('d - ', d[1])
print('d - ', d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1]))
```
> `<출력결과>`</br>
> d -  1000</br>
> d -  2000</br>
> d -  Captine</br>
> e -  ('Ace', 'Base', 'Captine')</br>
> e -  Base</br>
> e -  ['Ace', 'Base', 'Captine']</br>

* 슬라이싱
```python
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])
```
> `<출력결과>`</br>
> d -  (100, 1000, 'Ace')</br>
> d -  ('Ace', 'Base', 'Captine')</br>
> e -  ('Base', 'Captine')</br>

* 연산 : 수정은 불가능 하지만, 튜플 원소 개수가 늘어나는 것은 허용
```python
print('c + d', c + d)
print('c * 3', c * 3)
```
> `<출력결과>`</br>
> c + d (11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')</br>
> c * 3 (11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)</br>
 
* 함수
```python
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))
```
> `<출력결과>`</br>
> a -  (5, 2, 3, 1, 4)</br>
> a -  2</br>
> a -  1</br>

### (중요) 팩킹 & 언팩킹 (Packing, and Unpacking)
* 팩킹 : n개의 원소를 하나로 묶다.
```python
t = ('foo', 'bar', 'baz', ' qux')
print(t)
print(t[0])
print(t[-1])
```
> `<출력결과>`</br>
> ('foo', 'bar', 'baz', ' qux')</br>
> foo</br>
> qux</br>

* 언팩킹 : 묶여있는 것을 각각 푼다.
```python
(x1, x2, x3, x4) = t # 묶여 있던 것을 각각 풀어서 변수에 할당
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))
```
> `<출력결과>`</br>
> foo bar baz  qux</br>
> <class 'str'> <class 'str'> <class 'str'> <class 'str'></br> 

* 팩킹 & 언팩킹 구분
```python
# 팩킹 & 언팩킹
t2 = 1, 2, 3            # 팩킹 (튜플로 본다)
t3 = 4,                 # 팩킹 (튜플로 본다)
x1, x2, x3 = t2         # 언팩킹
x1, x5, x6 = 4, 5, 6    # 언팩킹
```

## 2.7. Dictionary
특징 : 순서 X, 키 중복 X, 수정 O, 삭제 O
* 선언
```python
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
)   # 이 방법이 가장 괜찮아 보임
```

* 출력
```python
print('a - ', a.get('name1'))   # None가 나옴 get을 훨씬 많이 사용함
print('b - ', b[0]) # 없을경우 오류남
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
```
> `<출력결과>`</br>
> a -  None</br>
> b -  Hello Python</br>
> b -  Hello Python</br>
> f -  Seoul</br>
> f -  33</br>

* 추가 
```python
a['address'] = 'Seoul'  # 추가
print('a - ', a)
a['name'] = 'Seoul' # 수정
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
```
> `<출력결과>`</br>
> a -  {'name': 'Kim', 'phone': '01033337777', 'birth': '890503', 'address': 'Seoul'}</br>
> a -  {'name': 'Seoul', 'phone': '01033337777', 'birth': '890503', 'address': 'Seoul'}</br>
> a -  {'name': 'Seoul', 'phone': '01033337777', 'birth': '890503', 'address': 'Seoul', 'rank': [1, 2, 3]}</br>

* Key 의 개수
```python
print('a - ', len(a))
```
> `<출력결과>`</br>
> a -  5

### # Dictionary Function

* keys : key 목록 조회
```python
# 키 목록 조회
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
print('a - ', a.keys())
# 키 목록 list로 형변환
print('a - ', list(a.keys()))
```
> `<출력결과>`</br>
> a -  dict_keys(['name', 'phone', 'birth'])</br>
> a -  ['name', 'phone', 'birth']</br>
* values : value 목록 조회
```python
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
# 값 목록 조회
print('a - ', a.values())
# 값 목록 list로 형변환
print('a - ', list(a.values()))
```
> `<출력결과>`</br>
> a -  dict_values(['Kim', '01033337777', '890503'])</br>
> a -  ['Kim', '01033337777', '890503']</br>

* items : key, value 조합 형태로 조회
```python
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
# dict item 형태 (key,value) 조합된 형태 목록으로 조회
print('a - ', a.items())
# dict item 형태 (key,value) 조합된 형태 목록 list로 형변환
print('a - ', list(a.items()))
```
> `<출력결과>`</br>
> a -  dict_items([('name', 'Kim'), ('phone', '01033337777'), ('birth', '890503')])</br>
> a -  [('name', 'Kim'), ('phone', '01033337777'), ('birth', '890503')]</br>

* pop : Dictionary에서 해당 key의 값 제거후 해당 key의 value 리턴
```python
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
# a에 name 리턴후 Dictionary에서 제거후 name의 value를 리턴
print('a - ', a.pop('name'))
print('a - ', a)
```
> `<출력결과>`</br>
> a -  890503
> a -  {'name': 'Kim', 'phone': '01033337777'}

* popitem : Dictionary에서 마지막 item 제거 후 해다 아이템 리턴(key, value 형태)
```python
f = dict(
    Name='Nice',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)
# f에서 마지막 아이템 리턴후 Dictionary에서 제거후 아이템 형태로 리턴
print('f - ', f.popitem())
print('f - ', f)
```
> `<출력결과>`</br>
> f -  ('Status', True)
> f -  {'Name': 'Nice', 'City': 'Seoul', 'Age': 33, 'Grade': 'A'}

* in : Dictionary에서 key 존재 여부 확인
```python
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
# birth라는 키가 a에 있나요? True, False
print('a - ', 'birth' in a)
```
> `<출력결과>`</br>
> a -  True

* update : Dictionary에서 key의 value를 수정
```python
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '890503', 'test': 'test'}
print("a - ", a)
a['test'] = 'test_dict'
print("a - ", a)
a.update(birth='910904')
print("a - ", a)
```
> `<출력결과>`</br>
> a -  {'name': 'Kim', 'phone': '01033337777', 'birth': '890503'}
> a -  {'name': 'Kim', 'phone': '01033337777', 'birth': '890503', 'test': 'test_dict'}
> a -  {'name': 'Kim', 'phone': '01033337777', 'birth': '910904', 'test': 'test_dict'}


## 2.8. Set
* 특징 : 순서 X, 중복 X, 수정 O, 삭제 O
* 기본 선언
```python
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 4, 4, 4, 5, 6])  # 중복을 허용하지 않음
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
# {} : key: value 구조이면 dic // value만 있으면 set
e = {'foo', 'bar', 'bzz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}
```

* 형변환
* 튜블 변환 (set -> tuple)
```python
a = set([1, 2, 3, 4])
b = tuple(a)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
```
> `<출력결과>`</br>
> t -  <class 'tuple'> (1, 2, 3, 4)
> t -  1 (2, 3)

* 리스트 형변환 (set -> list)
```python
c = set([1, 4, 4, 4, 4, 5, 6])  # 중복을 허용하지 않음
l = list(c)
print('l - ', l)
```
> `<출력결과>`</br>
> l -  [1, 4, 5, 6]

### Set Function
* len : 튜플의 길이 측정
```python
a = set([1, 2, 3, 4])
print(len(a))
```
> `<출력결과>`</br>
> 3

* add : Set에 데이터 추가
```python
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
```
> `<출력결과>`</br>
> s1 -  {1, 2, 3, 4, 5}

* remove : Set에서 해당 데이터 제거 (없는 원소 삭제시 KeyError 발생)
```python
s1 = set([1, 2, 3, 4])
s1.remove(4)
print('s1 - ', s1)
# 없는 원소 삭제시 KeyError 발생
s1.remove(5) # 오류 발생
```
> `<출력결과>`</br>
> s1 -  {1, 2, 3, 5}

* discard : Set에서 해당 데이터 제거 (없는 원소 삭제해도 오류 발생하지 않음)
```python
s1 = set([1, 2, 3, 4])
s1.discard(5)
print('s1 - ', s1)
s1.discard(4)
print('s1 - ', s1)
```
> `<출력결과>`</br>
> s1 -  {1, 2, 3, 4}
> s1 -  {1, 2, 3}

* clear : 전체 삭제
```python
s1 = set([1, 2, 3, 4])
s1.clear()
print('s1 - ', s1)
```
> `<출력결과>`</br>
> s1 -  set()