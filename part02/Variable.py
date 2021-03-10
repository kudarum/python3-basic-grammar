# 변수

# 기본선언
n = 700

# 동시 선언
x = y = z = 700

# 재선언
n = "Change Value"

# Python 값 할당 방식
# Object Referecnes
# 1, 2 등의 숫자부터 시작해 모든 것이 객체이며 하나의 개체는 단 하나의 인스턴스로 존재한다(싱글톤).
# 예를들면 a = 2 라고 변수를 할당하면 2라는 값이 a가 가르키는 메모리 공간에 할당되는 것이 아니라
# 2라는 인스턴스의 주소 값을 a가 가르키고 있는 것
# (즉. 동일한 값은 주소가 동일하게 된다.)
# 정리하면 Python에서 모든 것은 객체이고 각 객체는 하나의 인스턴스를 갖는다.

# 예 1)
# n -> 777
n = 777
print(n,type(n))

# 예 2)
m = n # n을 m에 복사
# m -> 777 <- n
print(m, n)
print(type(m), type(n))

m = 400
print(m, n)

# id(identity) 확인 : 객체의 고유값 확인
# id 가 다름
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))

# id가 같음
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))

# 다양한 변수 선언 방법
# Camel Case : numberOfCollageGraduates -> Method 선언
# Pascal Case : NumberOfCollageGraduates -> Class 선언
# snake Case : number_of_collage_graduates -> python 변수 선언

# 예약어는 변수명으로 불가능
# for = 3
# as = 3
# class = 3