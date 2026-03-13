import tkinter as tk
from tkinter import messagebox


# ==============================
# Task Class
# ==============================
class Task:
    # 초기화
        # text : Task 저장값
        # done : Boolean 속성 현황값
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

    # 상태 반전
    def toggle(self):
        self.done = not self.done


# ==============================
# TodoList Class (데이터 관리)
# ==============================
class TodoList:
    # 초기화
    def __init__(self, filename="todo.txt"):
        self.tasks = []
        self.filename = filename
        self.load()
    
    # 할 일 추가
    def add_task(self, text):
        self.tasks.append(Task(text))

    # 할 일 삭제
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    # 내용 상태 변환
    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle()
    
    # 내용 저장
    # map 및 람다 사용
    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            # for task in self.tasks:
            #     f.write(f"{int(task.done)}|{task.text}\n")
            lines = map(lambda task: f"{int(task.done)}|{task.text}\n", self.tasks)
            f.writelines(lines)

    # 불러오기
    # 값을 불러오고 '|'을 기준으로 앞은 상태, 뒤는 내용으로 분리하여 저장.
    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    done, text = line.strip().split("|")
                    self.tasks.append(Task(text, bool(int(done))))
        except FileNotFoundError:
            pass


# ==============================
# Tkinter(GUI)
# ==============================
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo = TodoList()

        # 입력창 (Entry 사용)
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # 추가하는 버튼(할 일 목록에 추가)
        add_button = tk.Button(root, text="추가", command=self.add_task)
        add_button.pack()

        # 밑에 나오는 목록(리스트박스)
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)

        # 버튼 프레임
        frame = tk.Frame(root)
        frame.pack()

        # 완료에 대한 버튼
        complete_btn = tk.Button(frame, text="체크", command=self.complete_task)
        complete_btn.grid(row=0, column=0, padx=30)

        # 삭제에 대한 버튼
        delete_btn = tk.Button(frame, text="삭제", command=self.delete_task)
        delete_btn.grid(row=0, column=1, padx=30)

        # 매번 업데이트 진행
        self.update_listbox()

    # 상시 업데이트 진행
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # 리스트 박스 초기화

        for task in self.todo.tasks:    # Task 에 대해서 불러오는 구문
            status = "O" if task.done else " "
            self.listbox.insert(tk.END, f"[{status}] {task.text}")

    # 입력창의 텍스트를 가져오기
    def add_task(self):
        text = self.entry.get().strip()

        if not text:        # 공백 방지용
            messagebox.showwarning("경고", "내용을 입력하세요")
            return

        self.todo.add_task(text)    # Task 추가
        self.todo.save()            # 파일 저장

        self.entry.delete(0, tk.END)    # 입력창 초기화
        self.update_listbox()           # 업데이트

    # 내용 삭제 버튼
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]  # 선택 항목
            self.todo.delete_task(index)    # 삭제
            self.todo.save()                # 저장
            self.update_listbox()           # 업데이트
        except IndexError:
            messagebox.showwarning("경고", "삭제할 항목을 선택하세요")

    # 내용 완료 버튼
    def complete_task(self):
        try:
            index = self.listbox.curselection()[0] # 선택 항목
            self.todo.toggle_task(index)    # 완료(토글값 변경)
            self.todo.save()                # 저장
            self.update_listbox()           # 업데이트
        except IndexError:
            messagebox.showwarning("경고", "항목을 선택하세요")


# ==============================
# 실행
# ==============================
root = tk.Tk()
app = TodoApp(root)
root.mainloop()