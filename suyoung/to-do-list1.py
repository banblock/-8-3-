from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
import os

# 읽기 함수
def r_todo():
    path = r"minipro\TDL.txt"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            con = file.read()
            ostring.set(con)

# 저장 함수
def a_todo():
    con = oentry.get()
    if con.strip() == "":
        return

    path = r"minipro\TDL.txt"
    with open(path, 'a', encoding='utf-8') as file:
        file.write(con + "\n")

    print(f"저장완료:{con}")
    oentry.set("")
    r_todo()

# 리셋 함수
def w_todo():
    path = r"minipro\TDL.txt"
    with open(path,'w',encoding='utf-8') as file:
        file.write("")
    print("리셋 완료")
    r_todo()

oroot = Tk()
oroot.geometry("500x450")
oroot.title("TO-DO-List")


oentry = StringVar()
ostring = StringVar()
 

ent = Entry(oroot, textvariable=oentry)
ent.pack()

obtn = Button(oroot, text="저장", command=a_todo)
obtn.pack()

obtn1 = Button(oroot, text="리셋", command=w_todo)
obtn1.pack()

olabel = Label(oroot, text="오늘의 할일")
olabel.pack()

olabel1 = Label(oroot, textvariable=ostring)
olabel1.pack()

r_todo()

oroot.mainloop()