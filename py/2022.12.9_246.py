import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lblTitile = tk.Label(self, text="个人信息调查")
        self.lblName = tk.Label(self, text="姓名")
        self.lblSex = tk.Label(self, text="性别")
        self.lblHobby = tk.Label(self, text="爱好")
        self.lblTitile.grid(row=0, column=0, columnspan=4)
        self.lblName.grid(row=1, column=0)
        self.lblSex.grid(row=2, column=0)
        self.lblHobby.grid(row=3, column=0)
        # 创建文本框
        self.entryName = tk.Entry(self)
        self.entryName.grid(row=1, column=1, columnspan=3)
        # 创建单选按钮
        self.vSex = tk.StringVar()
        self.vSex.set('M')
        self.rdoMale = tk.Radiobutton(
            self, text="男", variable=self.vSex, value='M')
        self.rdoFemale = tk.Radiobutton(
            self, text="女", variable=self.vSex, value='F')
        self.rdoMale.grid(row=2, column=1)
        self.rdoFemale.grid(row=2, column=2)
        # 创建复选按钮
        self.vHobbyMusic = tk.IntVar()
        self.vHobbySports = tk.IntVar()
        self.vHobbyTravel = tk.IntVar()
        self.vHobbyMovie = tk.IntVar()
        self.checkboxMusic = tk.Checkbutton(
            self, text="音乐", variable=self.vHobbyMusic)
        self.checkboxSports = tk.Checkbutton(
            self, text="体育", variable=self.vHobbySports)
        self.checkboxTravel = tk.Checkbutton(
            self, text="旅游", variable=self.vHobbyTravel)
        self.checkboxMovie = tk.Checkbutton(
            self, text="电影", variable=self.vHobbyMovie)
        self.checkboxMusic.grid(row=3, column=1)
        self.checkboxSports.grid(row=3, column=2)
        self.checkboxTravel.grid(row=3, column=3)
        self.checkboxMovie.grid(row=3, column=4)
        # 创建按钮
        self.btnSubmit = tk.Button(self, text="提交", command=self.submit)
        self.btnSubmit.grid(row=4, column=0, columnspan=2)
        self.btnCancel = tk.Button(self, text="取消", command=self.quit)
        self.btnCancel.grid(row=4, column=2, columnspan=2)

    def submit(self):
        strSex = "男" if self.vSex.get() == 'M' else "女"
        strMusic = self.checkboxMusic["text"] if self.vHobbyMusic.get(
        ) == 1 else ""
        strSports = self.checkboxSports["text"] if self.vHobbySports.get(
        ) == 1 else ""
        strTravel = self.checkboxTravel["text"] if self.vHobbyTravel.get(
        ) == 1 else ""
        strMovie = self.checkboxMovie["text"] if self.vHobbyMovie.get(
        ) == 1 else ""
        str1 = self.entryName.get() + '您好:\n'
        str1 += '您的性别是:' + strSex + '\n'
        str1 += '您的爱好是:' + strMusic + strSports + strTravel + strMovie
        messagebox.showinfo("个人信息", str1)

root=tk.Tk()
root.title("个人信息调查")
app=Application(master=root)
app.mainloop()
