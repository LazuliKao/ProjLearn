# 任务：GUI实现成绩管理图像界面
# 主要功能：
# （1）支持添加信息、修改信息、删除信息的功能
# （2）修改账号和登录密码
# （3）支持查询学生信息
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import os


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        # 定义起始参数:包括title，大小，背景颜色等等
        self.title('成绩管理系统')
        self.geometry('800x600')
        self.resizable(0, 0)
        self.config(bg='white')
        self.setup_UI()
        self.loac_from_file()
        self.load_treeview(self.all_student_list)
        self.bind_event()

    def setup_UI(self):
        # 定义各种参数，包括按钮，模板，和容器
        # 创建两个Panedwindow容器，左边添加按钮，右边作为TreeView显示界面
        self.Pane_left = PanedWindow(
            width=200, height=540, style="left.TPanedwindow")
        self.Pane_left.place(x=4, y=94)
        self.Pane_right = PanedWindow(
            width=685, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=210, y=94)
        # 添加左边按钮
        self.Button_add = Button(self.Pane_left, text='添加信息')
        self.Button_add.place(x=40, y=20)
        self.Button_update = Button(self.Pane_left, text='修改信息')
        self.Button_update.place(x=40, y=45)
        self.Button_delete = Button(self.Pane_left, text='删除信息')
        self.Button_delete.place(x=40, y=70)
        # 定义各种参数，包括按钮，模板，和容器
        self.Pane_right = PanedWindow(width=725, height=540)
        self.Pane_right.place(x=170, y=94)
        # LabelFrame
        self.LabelFrame_query = LabelFrame(
            self.Pane_right, text="学生信息查询	", width=700, height=70)
        # 添加其余Button
        self.Button_query = Button(self.Pane_right, text='查询')
        self.Button_query.place(x=400, y=20)
        self.Show_all = Button(self.Pane_right, text='显示全部')
        self.Show_all.place(x=500, y=20)
        # 添加Label
        self.Label_query = Label(self.Pane_right, text='学号/姓名')
        self.Label_query.place(x=10, y=20)
        # 添加Entry
        self.Entry_query = Entry(self.Pane_right, width=20)
        self.Entry_query.place(x=80, y=20)
        # 添加TreeView
        self.Tree = Treeview(self.Pane_right, columns=(
            "sno", "names", "phone", "idcard"), show="headings", height=20)
        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("names", width=100, anchor="center")
        self.Tree.column("phone", width=100, anchor="center")
        self.Tree.column("idcard", width=100, anchor="center")
        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("names", text="姓名")
        self.Tree.heading("phone", text="电话")
        self.Tree.heading("idcard", text="身份证号")
        self.Tree.place(x=10, y=80)

    def loac_from_file(self):
        self.all_student_list = []
        self.file_path = "C:/Users/gaoxi/Desktop/stu.txt"
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    # 一次读一行，并分割数据
                    for line in f:
                        self.all_student_list.append(line.strip().split(","))
            except:
                messagebox.showinfo("系统消息", "文件读取失败！")
        else:
            messagebox.showinfo("系统消息", "提供的文件名不存在！")

    def load_treeview(self, current_list):
        # 判断是否有数据：
        if len(current_list) == 0:
            messagebox.showinfo("系统消息", "没有数据加载")
        else:
            for index in range(len(current_list)):
                # 逐个录入加载出来的文件
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1],
                                                    current_list[index][2], current_list[index][3]))

    def bind_event(self):
        pass


        # self.Button_add.bind("<Button-1>", self.add_student)
        # self.Button_update.bind("<Button-1>", self.update_student)
        # self.Button_delete.bind("<Button-1>", self.delete_student)
        # self.Button_query.bind("<Button-1>", self.query_student)
        # self.Show_all.bind("<Button-1>", self.show_all_student)
if __name__ == '__main__':
    this_main = MainWindow()  # 调用窗口类
    this_main.mainloop()
