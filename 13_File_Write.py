# 파일 읽기 및 쓰기
# 읽기모드 : r, 쓰기모드 : w, 추가모드 : a, 텍스트모드 : t, 바이너리모드 : b
# 상대 경로('../', './'), 절대경로('/User/Dev/')

# 파일 읽기(Read)
# 예1
f = open('./resource/it_news.txt', 'r', encoding='UTF-8') # 텍스트는 기본 값이니 rt 랑 동일
# 속성확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
# 내용읽기
print(f.read())
# 반드시 close
f.close()

# 예2
# 자동으로 커넥션이 close 되기 때문에 f.close 생략 가능
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

# 예3
# read() : 전체 읽기, read(10) : 10Byte 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(10)
    print(c)
    c = f.read(10)
    print(c)
    c = f.read(20)
    print(c)    # 커서라는 것이 있어서 마지막 읽어온 내용 기억하고 있음
    f.seek(0, 0)    # 0, 0 다시 처음부터 읽겠다.
    c = f.read(10)
    print(c)

# 예4
# readline : 한 줄 씩 일기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

# 예5
# readliens : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end=' ')

# 파일 쓰기(write)
# 예1
with open('./resource/contents1.txt', 'w') as f: # 덮어쓰기?
    f.write('I love python!!\n')

# 예2
with open('./resource/contents1.txt', 'at') as f: # 내용추가
    f.write('I love python!!\n')

# 예3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f: # 내용추가
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예4
with open('./resource/contents3.txt', 'w') as f: # 내용추가
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)

