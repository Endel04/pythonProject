import tkinter
import tkinter.font
import tkinter.messagebox
from join_membership import join_membership
import sys
import os
import main

class GUI:
    def __init__(self):
        # 로그인, 회원가입 정보
        self.id = []
        self.password = []
        self.nickname = []

        # 시작 화면
        self.root = tkinter.Tk()
        self.root.title("T-ANB")
        self.root.geometry("800x500+250+50")
        self.root.resizable(False, False)

        # T-ANB 로고
        label = tkinter.Label(self.root, text="T-ANB")
        label.pack()

        # 회원가입 버튼
        self.join_membership_Button = tkinter.Button(self.root, text="회원가입", command=self.move_join_membership(), foreground="#9b95b7", width=10, repeatdelay=20, font=("나눔바른고딕", 15))
        self.join_membership_Button.place(x=250, y=350)

        # 로그인 버튼
        self.login_Button = tkinter.Button(self.root, text="로그인", command=self.move_login(), foreground="#9b95b7", width=10, repeatdelay=20, font=("나눔바른고딕", 15))
        self.login_Button.place(x=450, y=350)

        self.root.mainloop()

    def move_join_membership(self):
        self.root.destroy()

    def move_login(self):
        self.root.destroy()

if __name__ == '__main__':
    gui = GUI()