f = open('text.txt', 'r', encoding='utf-8')

data = f.read()

f.close()

print(data)

print()

print('한 줄씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if line == '':  # 빈칸이면 끝내기
        break
    print(line.rstrip())  # line.replace('\n', '')

f.close()

print()

print('전체를 한 번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())