# 파이썬 예외처리 이해
# 예외 종류
# SysntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error')
# print('error'))
# if True

# NameError : 참조 없음
# a = 10
# b = 10
# print(c)

# ZeroDivisionError
# print(100/0)

# InxexError
# x = [50, 60, 70]
# print(x[3])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError
# dic = dict(
#     name='Lee'
#     , age=41
#     , city='Busan'
# )
# print(dic['ci'])
# print(dic.get("ci"))

# 예외가 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError : 자료구조 안에서 자료가 없을 때 발생
# x = [10, 50, 90]
# x.remove(50)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt')

# TypeError
# x = [1, 2]
# y = (1, 2)
# z = 'test'
# print(x + y)

# 예외처리
# try : 에러가 발생할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예1
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not Found it! - Occurred ValueError')
# else:
#     print('Ok! else.')
# finally:
#     print('Finally')


# 예2
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception:
#     print('Not Found it! - Occurred ValueError')
# else:
#     print('Ok! else.')
# finally:
#     print('Finally')

# 예3
# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e:
#     print(e)
#     print('Not Found it! - Occurred ValueError')
# else:
#     print('Ok! else.')
# finally:
#     print('Finally')


# 예4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! Pass!')
    else:
        raise ValueError
except ValueError:
    print('ValueError')