from tkinter import Tk, Frame, Listbox, Entry, Button, Checkbutton, Radiobutton, StringVar, Label, BooleanVar, messagebox
import file as fl
import re

class RootFrame():

    def __init__(self):
        self.oroot = Tk()
        self.oroot.geometry("300x300")
        
        self.s_importance = ['[High]', '[Mid]', '[Low]'] 
        
        self.uplist = []
        self.todolist = []
        self.setFrame()

    def setFrame(self):
        self.loadData()
        self.setTop()
        self.setMid()
        self.setBot()


    def setTop(self):
        self.top = Frame(self.oroot)
        self.top.pack()
        self.search_entry = Entry(self.top)
        self.search_btn = Button(self.top, command=self.searchTodo, text='search')
        self.search_entry.grid(row=0,column=1)
        self.search_btn.grid(row=0,column=2)
        self.check_val = {0:BooleanVar(), 1:BooleanVar(), 2:BooleanVar()}
        cbtn_high = Checkbutton(self.top, variable=self.check_val[0], text='[High]', command=self.resetMidFrame)
        cbtn_mid = Checkbutton(self.top, variable=self.check_val[1], text='[Mid]', command=self.resetMidFrame)
        cbtn_low = Checkbutton(self.top, variable=self.check_val[2], text='[Low]', command=self.resetMidFrame)
        cbtn_high.grid(row=1,column=1)
        cbtn_mid.grid(row=1,column=2)
        cbtn_low.grid(row=1,column=3)


    def setMid(self):
        self.mid = Frame(self.oroot)
        self.mid.pack()
        self.todo_listbox = Listbox(self.mid)
        self.todo_listbox.pack()
        self.resetMidFrame()

    def setBot(self):
        self.bot = Frame(self.oroot)
        self.bot.pack()
        self.todo_entry = Entry(self.bot)
        self.todo_entry.grid(row=0,column=1)
        self.add_btn = Button(self.bot, text='+', command=self.addTodo) 
        self.add_btn.grid(row=0,column=2)
        self.add_btn = Button(self.bot, text='-', command=self.removeTodo) 
        self.add_btn.grid(row=0,column=3)
        self.importance_label = Label
        self.radio_var = StringVar()
        self.radio_var.set('[Mid]')
        self.r_high_btn = Radiobutton(self.bot, text='High', variable=self.radio_var, value='[High]')
        self.r_mid_btn = Radiobutton(self.bot, text='Mid', variable=self.radio_var, value='[Mid]')
        self.r_low_btn = Radiobutton(self.bot, text='Low', variable=self.radio_var, value='[Low]')
        self.r_high_btn.grid(row=1,column=1)
        self.r_mid_btn.grid(row=1,column=2)
        self.r_low_btn.grid(row=1,column=3)



    def getRoot(self):
        return self.oroot


    def loadData(self):
        a = fl.load()
        self.todolist = a

    def saveData(self):
        print('call')
        fl.save(self.todolist)
        self.oroot.destroy()



    def addTodo(self):
        importance = self.radio_var.get()
        text = self.todo_entry.get() +' '+importance
        self.todolist.append(text)
        self.resetMidFrame()


    def removeTodo(self):
        index = self.todo_listbox.curselection()
        if not index:
            messagebox.showerror("오류", "삭제할 todo를 선택해야 합니다.")
        text = self.todo_listbox.get(index)
        self.uplist.remove(text)
        self.todolist.remove(text)
        self.resetMidFrame()


    def selectUplist(self):
        im_list = []
        for i in range(len(self.s_importance)):
            if self.check_val[i].get():
                im_list.append(self.s_importance[i])
        print(im_list)
        if im_list != [] :
            a = []
            p = "|".join(map(re.escape, im_list))
            for i in self.todolist:
                if re.search(p, i):
                    a.append(i)
                    print('incomming')
            
            self.uplist = a
            
        else:
            self.uplist = [x for x in self.todolist]


    def resetMidFrame(self):
        self.todo_listbox.delete(0, "end")
        self.selectUplist()
        for task in self.uplist:
            self.todo_listbox.insert("end", task)

    def searchTodo(self):
        pass


if __name__ == '__main__':
    ort = RootFrame()
    ort.getRoot().protocol("WM_DELETE_WINDOW", ort.saveData)
    ort.getRoot().mainloop()