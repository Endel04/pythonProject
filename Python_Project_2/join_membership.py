import tkinter
from tkinter import *
from tkinter import messagebox

class join_membership:
    def __init__(self, title):
        self.root = Tk()
        self.root.T_ANB_title(title)
        self.root.geometry("800x500+250+50")
        self.root.resizable(False, False)

        self.nickname_label = Label(self.root, text="닉네임", width=50, height=4, font=("나눔바른고딕", 15))
        self.nickname_table = tkinter.Entry(self.root, width=20)
        self.id_label = Label(self.root, text="아이디", width=50, height=4, font=("나눔바른고딕", 15))
        self.id_table = tkinter.Entry(self.root, width=20)
        self.password_label = Label(self.root, text="비밀번호", width=50, height=4, font=("나눔바른고딕", 15))
        # self.password_table = tkinter.Entry(self.root, width=20)

        string = StringVar()
        self.combo = tkinter.Combobox(self.root, width=20, textvariable=string)
        self.combo['values'] = ('여자', '남자')
        self.combo.current(0)

        self.nickname_label.place(x=100, y=50)
        self.nickname_tabel.place(x=100, y=50)
        self.id_label.place(x=250, y=200)
        self.id_tabel.place(x=250, y=200)
        self.password_label.place(x=400, y=350)
        # self.password_tabel.place(x=100, y=50)

        self.root.mainloop()