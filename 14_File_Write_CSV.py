# CSV 파일 읽기
# CSV : MEME - text/csv
import csv

# 예1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)    # header를 스킵한다.
    # 객체 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__

    for c in reader:
        # print(c)
        # print(type(c))
        # list to str
        print(' '.join(c))


# 예2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')   # delimiter 구분자 설정
    print(reader)


# 예3 : 딕셔너리를 가져오는 리더
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    for c in reader:
        for k,v in c.items():
            print(k, v)


# 예4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))
    for v in w:
        wt.writerow(v)

# 예5
with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    fields = ['One', 'Two', 'Three']

    # DicWriter
    wt = csv.DictWriter(f, fieldnames=fields)   # 필드 명으로 지정됨
    # Header Writer
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})
