# 외장 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예1 : 설정값?
import sys
sys.argv.append('test')
print(sys.argv)

# 예2(강제 종료)
# sys.exit()
# print('test')

# 예3 파이썬 패키지 위치
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle

# 예4(쓰기)
f = open('test.obj','wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# 예5(읽기)
f = open('test.obj','rb')
data = pickle.load(f)
print(data)
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어있으면 삭제), rename

# 예6
import os
print(os.environ)
print(os.environ["JAVA_HOME"])

# 예7(현재 경로)
print(os.getcwd())

# time : 시간 관련 처리
import time

# 예8
print(time.time())

# 예9(형태 변환)
print(time.localtime(time.time()))

# 예10(간단 표현)
print(time.ctime())

# 예11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 예12(시간 간격 발생)
for i in range(5):
    print(i)
    # time.sleep(1)

print('Finish')

# random : 난수 리턴
import random

# 예13
print(random.random())  # 0 ~ 1 실수

# 예14
print(random.randint(1, 45))
print(random.randrange(1, 45))

# 예15(섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 예16(무작위 선택)
c = random.choice(d)
print(c)

# webbrowser : 본인 OS의 웹 프라우저 실행
import webbrowser
webbrowser.open('http://google.com')

