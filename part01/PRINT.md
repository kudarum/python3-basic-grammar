##1. Print
***
###1.1. Print 란
***
Python으로 작업된 결과물을 화면에 출력하기 위해 사용
###1.2. 기본문법
***
* print("출력할 내용")
```python
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
```
* 출력결과
```text
Python Start!
Python Start!
Python Start!
Python Start!
```
### 1.3. Option 사용
***
#### 1) separator
* 문자열의 연결을 어떻게 할 것인가!
```python
print('P','y','t','h','o','n', sep=',')
```
* 출력결과
```text
P,y,t,h,o,n
```
#### 2) end
* 마지막 부분을 어떻게 처리할 것인가
```python
print('Welcome to', end='\n')
```
* 출력결과
```text
Welcome to
(공백)
```
#### 3) format
* d : 정수
* s : 문자열
* f : 실수
```python
print('%s %s' % ('one','two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))
```
* 출력결과
```text
one two
one two
two one
```
* %s
    - %10s : 10개 자리수 (양수 : 왼쪽공백, 음수 : 오른쪽공백)
    - {:>10} : 10개 자리수 (> : 왼쪽공백, : 오른쪽공백)
    ```python
    # 오른쪽 공백
    print('%10s' % ('nice'))
    print('{:>10}}'.format('nice'))
    # 왼쪽 공백
    print('%-10s' % ('nice'))
    print('{:10}}'.format('nice'))
    # 다른 문자 체우기
    print('{:_>10}}'.format('nice'))
    # 가운데 정렬
    print('{:^10}}'.format('nice'))
    # 절삭
    print('%.5s' % ('pythonstudy'))
    print('{:.5}'.format('pythonstudy'))
    print('{:10.5}'.format('pythonstudy')) # 10개의 공간에 5글자만 나오게 절삭
    ```
    - 출력결과
    ```text
        nice
        nice
    nice      
    nice      
    ______nice
       nice   
    pytho
    pytho
    pytho  (우측에 공백이 있음)
    ```
  
* %d
    - 사용법
    ```python
    print('%d %d' % (1,2))
    print('{} {}'.format(1,2))
    print('%4d' % (42))
    print('{:4d}'.format(42))
    ```
    - 출력결과
    ```text
    1 2
    1 2
    42
    42
    ```
* %f
    ```python
    print('%f' % (3.1415296535893))
    print('{:f}'.format(3.1415296535893))
    print('%1.5f' % (3.1415296535893)) # 정수부 1자리, 소수부 5자리까지
    
    print('%06.2f' % (3.1415296535893)) # 총 6자리 중에 소수부 2자리
    print('{:06.2f}'.format(3.1415296535893))
    ```
    - 출력결과
    ```text
    3.141530
    3.141530
    3.14153
    003.14
    003.14
    ```