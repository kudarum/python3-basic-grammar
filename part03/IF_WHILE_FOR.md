# 3. IF, WHILE, FOR 문 (조건문과 반복문)
## 3.1 조건문 IF
### 3.1.1 IF 란
* if 란 조건문을 의미한다. if 조건문: 형태로 이루어져 있고 조건문의 True, False 여부에 따라 
다음 문장의 수행여부를 결정한다.

### 3.1.2 IF 기본 문법
```python
# 예1
if True:    # 조건문이 True이니 실행
    print('Good')
if False:   # 조건문이 False이니 실행 X
    print('Bad')

# 예2
if False:
    print('Bad')
else:   # 위 조건문이 False이니 else 수행
    print('Good')
```
> `<출력결과>`</br> 
> Good</br>
> Good</br>

### 3.1.3 연산자
#### 3.1.3.1 관계 연산자
* 관계연산자 : \>, \>=, <, <=, ==, != 
* 관계 연산자 예시
```python
x = 15
y = 10
# 양변이 같을 때 참
print(x == y)

# 양변이 다를떄 참
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)
```

> False</br> 
> True</br> 
> True</br> 
> True</br> 
> False</br> 
> False</br> 


* 빈 문자열의 조건문 판단
```python
# 빈문자열의 조건문 판단 기준
city = ""   # False로 인식
if city:
    print("You are in: ", city)
else:
    print("plz enter your city")    # 출력됨

city2 = "seoul"
if city2:   # True로 인식
    print("You are in: ", city2)    # 출력됨
else:
    print("plz enter your city")
```
> `<출력결과>`</br> 
> plz enter your city</br> 
> You are in:  seoul</br>
> 
#### 3.1.3.2 논리 연산자
* and : 두 조건이 모두 True일 경우 True
* or  : 두 조건 중 하나만 True여도 True
* not : 부정 !(True) => False, !(False) => True
```python
a = 75
b = 40
c = 10

print('and:', a > b and b > c)  # a > b > c, 두조건 모두 만족해야 참
print('or:', a > b or b > c)    # 두 조건중 하나라도 만족하면 참
print('not:', not a > b)
print('not:', not b > c)
print(not True)
print(not False)
```
> `<출력결과>`</br> 
> and: True</br> 
> or: True</br> 
> not: False</br> 
> not: False</br> 
> False</br> 
> True</br> 

#### 3.1.3.3 산술, 관계, 논리 연산자의 우선 순위!
* 우선순위 : 산설 > 관계 > 논리
```python
print('e1 :', 3+12 > 7+3)
print('e2 :', 5 + 1 * 3 > 7 + 3 * 20)
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10)
```
> `<출력결과>`</br> 
> e1 : True</br>
> e2 : False</br>
> e3 : True</br>
> e4 : False</br>

#### 3.1.3.4 Containment 연산자
* in, not in
* 사용법 : A in B (B에 A가 포함되어 있나요?) / A not in B (B에 A가 포함되지 않았나요?)
```python
a = [10, 20, 30, 40, 50]
w = {80, 80, 90, 100}
e = dict(
    name='Lee',
    city="Seoul",
    grade="A"
)
r = (10, 12, 14)

print(15 in a)
print(90 in w)
print(12 not in r)
print('name' in e)
print('Seoul' in e.values())
```
> `<출력결과>`</br>
> False</br>
> True</br>
> False</br>
> True</br>
> True</br>

#### 3.1.3.5 조건문 연습
* 다중 조건문
```python
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')
```
* 중첩조건문
```python
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')
```

## 3.2 반복문 FOR
### 3.2.1 FOR 란
* for 문은 리스트(list)와 같은 순서형(sequence) 자료를 이용해서 원하는 명령을 반복할 때 사용

### 3.2.2 FOR 기본 문법
* 기본형태</br> 
for in \<collection></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\<loop body>
```python
for v1 in range(5):    # 0 ~ 4
    print('v1 is :', v1)
```
> `<출력결과>`</br>
> v1 is : 0</br>
> v1 is : 1</br>
> v1 is : 2</br>
> v1 is : 3</br>
> v1 is : 4</br>

### 3.2.3 Iterables 자료형 반복
* 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
* iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

* List 를 사용한 반복문
```python
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('name :', name)
```
> `<출력결과>`</br>
> name : Kim</br>
> name : Park</br>
> name : Cho</br>
> name : Lee</br>
> name : Choi</br>
> name : Yoo</br>

* 문자열 반복문
```python
word = "Beautiful"
for s in word:
    print('word :', s)
```
> `<출력결과>`</br>
> word : B</br>
> word : e</br>
> word : a</br>
> word : u</br>
> word : t</br>
> word : i</br>
> word : f</br>
> word : u</br>
> word : l</br>

* Dictionary를 사용한 반복문
```python
my_info = dict(
    name='Lee',
    age=33,
    city='Seoul'
)
# Key 반복
for k in my_info:
    print('Key :', k)
    
for k in my_info:
    print('Value :', my_info.get(k))

# Value 반복
for v in my_info.values():
    print('Value :', v)

# item 반복
for v in my_info.items():
    print('Item :', v)
```
> `<출력결과>`</br>
> <Key 반복></br>
> Key : name</br>
> Key : age</br>
> Key : city</br>
> 
> Value : Lee</br>
> Value : 33</br>
> Value : Seoul</br>
> 
> <Value 반복<>/br>
> Value : Lee</br>
> Value : 33</br>
> Value : Seoul</br>
> 
> <item 반복></br>
> Item : ('name', 'Lee')</br>
> Item : ('age', 33)</br>
> Item : ('city', 'Seoul')</br>

### 3.2.4 반복문 제어
* pass, break, countine 등을 사용하여 반복문의 흐름을 제어한다.
#### 3.2.4.1 pass
* 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행 (흐름에 영향이 전혀 없음)
#### 3.2.4.2 break
* 반복문을 멈추고 loop 밖으로 나가도록합니다.
```python
numbers = [14, 3, 15, 34, 36]
for num in numbers:
    if num == 34:
        print('Found : 34!!')
        break
    else:
        print('Not Found :', num)
```
> `<출력결과>`</br>
> Not Found : 14</br>
> Not Found : 3</br>
> Not Found : 15</br>
> Found : 34!!</br>
> Not Found : 36</br>

#### 3.2.4.3 continue
* 현재 순번을 종료하고 바로 다음 순번의 loop를 수행합니다.
```python
lt = ["1", 2, 5, True, 4.2, complex(4)]
for v in lt:
    if type(v) is bool:     # 자료형 대조시 is 사용
        continue            # bool 형일 경우 아래 프로세스 껀너뜀
    print('current type :', type(v))
    print('multiply by 2', v * 3)
```
> `<출력결과>`</br>
> current type : <class 'str'></br>
> multiply by 2 111</br>
> current type : <class 'int'></br>
> multiply by 2 6</br>
> current type : <class 'int'></br>
> multiply by 2 15</br>
> current type : <class 'float'></br>
> multiply by 2 12.600000000000001</br>
> current type : <class 'complex'></br>
> multiply by 2 (12+0j)</br>

### 3.2.5 FOR ~ ELSE 
* for문의 모든 반복문을 수행했을때 else 수행
```python
numbers = [14, 3, 4, 7, 10, 24]

for num in numbers:
    if num == 23:
        print('Found : 23')
        break
else:
    print('Not Found : 23')
```
> `<출력결과>`</br>
> Not Found : 23

## 3.3 반복문 WHILE
### 3.3.1 WHILE 란
* while문은 조건식 또는 조건식의 결과가 True인 경우 동작한다.

### 3.3.2 WHILE 기본 문법
* 기본형태</br> 
while \<expr>:</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\<statement(s)>
  
* 조건이 True일때 수행하고, False일때 종료함
```python
n = 5
while n > 0:
    n = n - 1
    print(n)
```
> `<출력결과>`</br>
> 4</br>
> 3</br>
> 2</br>
> 1</br>
> 0</br>

* 원소 수만큼 반복
```python
a = ['foo', 'bar', 'baz']
while a:    # a 원소 수만큼 반복 X, a가 데이터가 있으니 True O
    print(a.pop())
```
> `<출력결과>`</br>
> baz</br>
> bar</br>
> foo</br>

### 3.3.3 while ~ else
* while 문이 끝나면 else 구문 수행, 단! break를 만난경우 else 구문은 수행되지 않음
```python
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break   # break 만나서 빠져나오면 else 수행 X
else:
    print('else out.')
```
> `<출력결과>`</br>
> 9</br>
> 8</br>
> 7</br>
> 6</br>
> 5</br>
