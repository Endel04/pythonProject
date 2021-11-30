class write_Bulletin:
    def __init__(self, title):
        # 글 제목
        self.title = title

        # 글 이미지
        self.image = []

        # 글 내용
        self.content = ''

    def set_title(self):
        title = input('제목을 입력해 주세요 : ')

        self.title = '제목을 입력해 주세요!' if title == '' else title

    def set_image(self):
        image = input('이미지를 삽입해 주세요 (없을 경우 X 입력) : ')

        self.image = '삽입된 이미지가 없습니다!' if image == '' else image

    def set_content(self):
        content = input('내용을 입력해 주세요 : ')

        self.content = '내용을 입력해 주세요!' if content == '' else content

    def set_bulletin(self):
        self.set_title()
        self.set_image()
        self.set_content()

    def __str__(self):
        return f'제목 | {self.title}\n이미지 | {self.image}\n내용 | {self.content}'