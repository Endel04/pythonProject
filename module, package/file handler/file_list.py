# 디렉토리의 현재 파일과 디렉토리 리스트 보여주기
import os

# data = os.listdir('c:\\')  # C:\
# data = os.listdir('..')  # 상위 디렉토리
data = os.listdir('.')  # 현재 디렉토리
data = os.listdir('my_directory')  # 하위 디렉토리


for d in data:
    print(d)
    print('is directory? : ' + str(os.path.isdir(d)))
    print('is file? : ' + str(os.path.isfile(d)))