from write_Bulletin import write_Bullentin

class join_membership:
    def __init__(self, id, password):
        # 이름
        self.fullname = ''

        # 전화번호
        self.phone_number = ''

        # 생년월일
        self.birth = ''

        # 다니는 학교
        self.school = ''

        # 아이디
        self.id = id

        # 비밀번호
        self.password = password

    def set_fullname(self):
        fullname = input('이름을 입력해 주세요 : ')

        self.fullname = '이름을 입력해 주세요!' if fullname == '' else fullname

    def set_phone_number(self):
        phone_number = input('전화번호를 입력해 주세요')

        self.phone_number = '전화번호를 입력해 주세요!' if phone_number == '' else phone_number

    def set_birth(self):
        birth = input('생년월일을 입력해 주세요 (YYYY/MM/DD)')

        self.birth = '생년월일을 입력해 주세요!' if birth == '' else birth

    def set_school(self):
        school = input('재학 중인 학교의 이름을 입력해 주세요')

        self.school = '재학 중인 학교의 이름을 입력해 주세요!' if school == '' else school

    def set_id(self):
        id = input('아이디를 입력해 주세요')

        self.id = '아이디를 입력해 주세요!' if id == '' else id

    def set_password(self):
        password = input('비밀번호를 입력해 주세요')

        self.password = '비밀번호를 입력해 주세요!' if password == '' else password

    def start_membership(self):
        self.set_fullname()
        self.set_phone_number()
        self.set_birth()
        self.set_school()
        self.set_id()
        self.set_password()

    def __str__(self):
        return f'이름 : {self.fullname}\n전화번호 : {self.phone_number}\n생년월일 : {self.birth}\n학교 이름 : {self.school}\n아이디 : {self.id}\n비밀번호 : {self.password}'

class login:
    def __init__(self, id, password):
        # 아이디
        self.id = id

        # 비밀번호
        self.password = password

    def __str__(self):
        pass

class Bullentin_list:
    def __init__(self):
        self.T_ANB_list = []

    def join_membership(self):
        pass

    def login(self):
        pass

    def show_bullentin(self):
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

        if len(searched_bulletin) == 0:   # 검색한 제목이 없으면
            # 검색한 글의 제목이 없다고 표시하기
            print('\n검색한 게시글의 제목이 없습니다.\n')

    def __str__(self):
        pass