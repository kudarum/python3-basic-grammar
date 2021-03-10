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
### 1.4. 다양한 변수 선언 방법
* Camel Case : numberOfCollageGraduates -> Method 선언
* Pascal Case : NumberOfCollageGraduates -> Class 선언
* snake Case : number_of_collage_graduates -> python 변수 선언
* 주의 : 예약어는 변수명으로 사용 불가능
  - 예) for = 3, as = 3, class = 3
