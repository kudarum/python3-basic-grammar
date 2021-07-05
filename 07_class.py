# 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 모든 클래스가 공유한다.
# 인스턴스 변수 : 객체마다 별도 존재

# 클래스 and 인스턴스 차이 이해

# 예1
class Dog(object):  # object 상속 받음
    # 클래스 속성 (변수)
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        super(Dog, self).__init__()
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)

# 인스턴스화 : self는 자동으로 들어감
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)

# 비교
print(a == b, id(a), id(b))
print(a == c, id(a), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예2
# self의 이해
class SelfTest:
    def func1():    # 클래스 메소드
        print('Func1 called')

    def func2(self):
        print(id(self)) # self와 아래 f의 id가 같다 즉. self == f 이다
        print('Func2 called')


f = SelfTest()

# print(dir(f))
print(id(f))

# f.func1() 예외 발생
SelfTest.func1()
# SelfTest.func2() 예외 발생
f.func2()


# 예3
# 클래스 변수, 인스턴스 변수
class Warehouse:

    # 클래스 변수 = 0
    stock_num = 0   # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

# 이 시점에 클래스 변수는 두번 호출되어서 2가 됨
print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)   # 클래스의 네임스페이스
print(user2.__dict__)
print('before', Warehouse.__dict__)
print(user1.stock_num)

del user1

print('after', Warehouse.__dict__)


# 예4
class Sms(object):  # object 상속 받음
    # 클래스 속성 (변수)
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        super(Sms, self).__init__()
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} syas {}!'.format(self.name, sound)


# 인스턴스 생성
c = Sms('july', 4)
d = Sms('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(c.speak('Mung Mung'))
