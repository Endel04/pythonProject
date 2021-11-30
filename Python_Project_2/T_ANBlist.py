from join_membership import join_membership
from write_Bulletin import write_Bulletin
from tkinter import *

class T_ANBlist:
    def __init__(self):
        self.T_ANB_list = []  # 게시물
        self.member_list = []  # 회원

    def join_membership(self):
        # message1 = input('회원가입을 하시겠습니까? (1 : yes, 1 이외의 숫자 : no) | ')
        #
        # if message1 == '1':

        id = input('\n사용하실 아이디를 입력해 주세요 : ')

        new_member = join_membership(id)
        new_member.start_membership()

        # 회원 리스트에 새로운 회원 추가하기
        self.member_list.append(new_member)
        return new_member

    def login(self):
        cnt = 0

        while True:
            print('----------------')
            id = input('아이디 : ')
            password = input('비밀번호 : ')
            print('----------------')

            if id == 'dbgkfka2737' and password == 'ho190304!':
                print('\n로그인 성공!')
                break
            else:
                cnt += 1
                print('\n로그인 {}회 실패'.format(cnt))

            if cnt >= 5:
                print('\n보안을 위해 로그인 시스템을 종료합니다!')
                break
            print()

    def set_bulletin(self):
        self.add_bulletin()

    def add_bulletin(self):
        # 새로 올릴 게시글 제목 입력
        topic = input('제목을 입력해 주세요 : ')

        # 게시글 추가
        new_bulletin = write_Bulletin(topic)
        new_bulletin.set_bullentin()

        # 게시글 리스트에 새로 올린 게시글 추가하기
        self.T_ANB_list.append(new_bulletin)

    def upload_bulletin(self):
        self.add_bulletin()

    def show_info(self):
        pass

    def show_bulletin(self):
        # 모든 게시글 보여주기
        for index, bulletin in enumerate(self.T_ANB_list):
            print(f'{index + 1}')
            print(bulletin)

    def search_bulletin(self):
        # 찾았던 게시글
        searched_bulletin = []

        # 글 제목 입력받기
        title = input('\n찾으시는 게시글의 제목을 입력하세요 : ')

        # 게시글의 제목이 검색한 제목과 같은지 확인
        for bulletin in self.T_ANB_list:
            if title == bulletin.name:  # 같으면 글 전체 보여주기
                searched_bulletin.append(bulletin)
                print(bulletin)

        if len(searched_bulletin) == 0:  # 검색한 제목이 없으면
            # 검색한 글의 제목이 없다고 표시하기
            print('\n검색한 게시글의 제목이 없습니다.')

    def init_bulletin(self):
        게시글1 = write_Bulletin('정나라 바보')  # title
        게시글1.image = 'image1.jpg'  # []
        게시글1.content = '정나라 ㄹㅇ 바보임 한 번 때려보고 싶음'  # ''

        self.T_ANB_list.append(게시글1)

        게시글2 = write_Bulletin('너네 하이큐 봣냐??')
        게시글2.image = ''
        게시글2.content = '와 진심 ㄹㅇ로 하이큐 꼭 보셈 개존잼임'

        self.T_ANB_list.append(게시글2)