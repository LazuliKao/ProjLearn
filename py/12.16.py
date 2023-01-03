# 任务：GUI实现成绩管理图像界面
# 主要功能：
# （1）支持添加信息、修改信息、删除信息的功能
# （2）修改账号和登录密码
# （3）支持查询学生信息
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.messagebox import *
import os


class DetailWindow(Toplevel):
    def __init__(self, action_flag: int, current_student: list, all_student_list: list):
        super().__init__()
        self.title("学生明细信息")
        self.geometry("600x500+600+150")
        self.resizable(0, 0)  # 不能改变大小

        # 定义全局变量
        self.flag = action_flag
        self.current_student_list = current_student
        self.all_student_list = all_student_list
        # 加载控件
        self.setup_UI()
        # 修改明细窗口标题
        self.load_windows_flag()

    def setup_UI(self):
        # 设置style
        self.Style01 = Style()
        self.Style01.configure("title.TLabel", font=(
            "华文黑体", 20, "bold"), foreground="navy")
        self.Style01.configure("detail.TLabel", font=(
            "华文黑体", 12, "bold"), foreground="navy")
        self.Style01.configure("TButton", font=(
            "华文黑体", 12, "bold"), foreground="navy")
        self.Style01.configure("TEntry", font=("华文黑体", 12, "bold"), width=10)
        self.Style01.configure("TRadiobutton", font=(
            "华文黑体", 12, "bold"), foreground="navy")

        # 添加一个title
        self.var_title = StringVar()
        self.Label_title = Label(self, text="==明细窗体==", style="title.TLabel")
        self.Label_title.place(x=360, y=20)

        # 加载一个pane
        self.Pane_detail = PanedWindow(self, width=590, height=380)
        self.Pane_detail.place(x=5, y=88)

        # 添加属性
        # 第一排：学号
        self.Label_sno = Label(
            self.Pane_detail, text="学号:", style="detail.TLabel")
        self.Label_sno.place(x=30, y=10)
        self.var_sno = StringVar()
        self.Entry_sno = Entry(self.Pane_detail, textvariable=self.var_sno, font=(
            "华文黑体", 15, "bold"), width=10)
        self.Entry_sno.place(x=80, y=8)
        # 姓名
        self.Label_name = Label(
            self.Pane_detail, text="姓名:", style="detail.TLabel")
        self.Label_name.place(x=220, y=10)
        self.var_name = StringVar()
        self.Entry_name = Entry(self.Pane_detail, textvariable=self.var_name, font=(
            "华文黑体", 15, "bold"), width=10)
        self.Entry_name.place(x=270, y=8)
        # 性别
        self.Label_gender = Label(
            self.Pane_detail, text="性别:", style="detail.TLabel").place(x=410, y=10)
        self.var_gender = IntVar()
        self.Radio_man = Radiobutton(
            self.Pane_detail, text="男", variable=self.var_gender, value=1)
        self.Radio_man.place(x=460, y=10)
        self.Radio_woman = Radiobutton(
            self.Pane_detail, text="女", variable=self.var_gender, value=2)
        self.Radio_woman.place(x=510, y=10)
        # 第二排：出生日期
        self.Label_age = Label(
            self.Pane_detail, text="出生日期:", style="detail.TLabel")
        self.Label_age.place(x=30, y=60)
        self.var_age = StringVar()
        self.Entry_age = Entry(self.Pane_detail, textvariable=self.var_age, font=(
            "华文黑体", 15, "bold"), width=10)
        self.Entry_age.place(x=110, y=58)
        # 身份证号码
        self.Label_id = Label(
            self.Pane_detail, text="身份证号码:", style="detail.TLabel")
        self.Label_id.place(x=250, y=60)
        self.var_id = StringVar()
        self.Entry_id = Entry(self.Pane_detail, textvariable=self.var_id, font=(
            "华文黑体", 15, "bold"), width=19)
        self.Entry_id.place(x=350, y=58)
        # 第三排：手机号码
        self.Label_mobile = Label(
            self.Pane_detail, text="手机号码:", style="detail.TLabel")
        self.Label_mobile.place(x=30, y=110)
        self.var_mobile = StringVar()
        self.Entry_mobile = Entry(self.Pane_detail, textvariable=self.var_mobile, font=(
            "华文黑体", 15, "bold"), width=12)
        self.Entry_mobile.place(x=110, y=108)
        # 邮箱地址
        self.Label_email = Label(
            self.Pane_detail, text="邮箱地址:", style="detail.TLabel")
        self.Label_email.place(x=270, y=110)
        self.var_email = StringVar()
        self.Entry_email = Entry(self.Pane_detail, textvariable=self.var_email, font=(
            "华文黑体", 15, "bold"), width=19)
        self.Entry_email.place(x=350, y=108)
        # 第四排：家庭住址
        self.Label_home = Label(
            self.Pane_detail, text="家庭住址:", style="detail.TLabel")
        self.Label_home.place(x=30, y=160)
        self.var_address = StringVar()
        self.Entry_home = Entry(self.Pane_detail, textvariable=self.var_address, font=(
            "华文黑体", 15, "bold"), width=43)
        self.Entry_home.place(x=110, y=158)
        # 第五排：入学时间
        self.Label_studyin = Label(
            self.Pane_detail, text="入学时间:", style="detail.TLabel")
        self.Label_studyin.place(x=30, y=210)
        self.var_studyin = StringVar()
        self.Entry_studyin = Entry(self.Pane_detail, textvariable=self.var_studyin, font=(
            "华文黑体", 15, "bold"), width=10)
        self.Entry_studyin.place(x=110, y=208)
        # 专业：
        self.Label_pro = Label(
            self.Pane_detail, text="专业:", style="detail.TLabel")
        self.Label_pro.place(x=250, y=210)
        self.var_pro = StringVar()
        self.Entry_pro = Entry(self.Pane_detail, textvariable=self.var_pro, font=(
            "华文黑体", 15, "bold"), width=24)
        self.Entry_pro.place(x=300, y=208)
        # 第六排：紧急联系人
        self.Label_emcon = Label(
            self.Pane_detail, text="紧急联系人:", style="detail.TLabel")
        self.Label_emcon.place(x=30, y=260)
        self.var_emcon = StringVar()
        self.Entry_emcon = Entry(self.Pane_detail, textvariable=self.var_emcon, font=(
            "华文黑体", 15, "bold"), width=8)
        self.Entry_emcon.place(x=130, y=258)
        # 紧急联系电话
        self.Label_emtel = Label(
            self.Pane_detail, text="紧急联系人电话:", style="detail.TLabel")
        self.Label_emtel.place(x=250, y=260)
        self.var_emtel = StringVar()
        self.Entry_emtel = Entry(self.Pane_detail, textvariable=self.var_emtel, font=(
            "华文黑体", 15, "bold"), width=16)
        self.Entry_emtel.place(x=380, y=258)
        # 放置两个按钮
        self.Button_save = Button(
            self, text="保存", style="TButton", command=self.commit)
        self.Button_save.place(x=300, y=472)
        self.Button_exit = Button(
            self, text="关闭", style="TButton", command=self.close_window)
        self.Button_exit.place(x=450, y=472)

    def load_windows_flag(self):
        if self.flag == 1:
            # 修改title
            self.Label_title.configure(text="==查看学生明细==")
            # 加载数据
            self.load_student_detail()
            # 控制控件的状态
            self.Button_save.place_forget()
            self.Entry_sno["state"] = DISABLED
            self.Entry_name["state"] = DISABLED
            self.Radio_man["state"] = DISABLED
            self.Radio_woman["state"] = DISABLED
            self.Entry_age["state"] = DISABLED
            self.Entry_id["state"] = DISABLED
            self.Entry_mobile["state"] = DISABLED
            self.Entry_email["state"] = DISABLED
            self.Entry_home["state"] = DISABLED
            self.Entry_studyin["state"] = DISABLED
            self.Entry_pro["state"] = DISABLED
            self.Entry_emcon["state"] = DISABLED
            self.Entry_emtel["state"] = DISABLED
        elif self.flag == 2:
            self.Label_title.configure(text="==添加学生明细==")
        elif self.flag == 3:
            self.Label_title.configure(text="==修改学生明细==")
            # 填充数据
            self.load_student_detail()
            # 学号不允许修改
            self.Entry_sno["state"] = DISABLED

    def load_student_detail(self):
        if len(self.current_student_list) == 0:
            showinfo("系统消息", "没有任何数据需要展示!")
        else:
            self.var_sno.set(self.current_student_list[0])  # 学号
            self.var_name.set(self.current_student_list[1])  # 姓名
            if "男" in self.current_student_list[2]:         # 性别
                self.var_gender.set(1)
            else:
                self.var_gender.set(2)
            self.var_age.set(self.current_student_list[3])  # 生日
            self.var_mobile.set(self.current_student_list[4])  # 电话号码
            self.var_email.set(self.current_student_list[5])  # 邮箱
            self.var_address.set(self.current_student_list[6])  # 地址
            self.var_id.set(self.current_student_list[7])  # 身份证号
            self.var_studyin.set(self.current_student_list[8])  # 入学时间
            self.var_pro.set(self.current_student_list[9])  # 专业
            self.var_emcon.set(self.current_student_list[10])  # 紧急联系人
            self.var_emtel.set(self.current_student_list[11])  # 紧急联系号码

    def close_window(self):
        """
        关闭当前窗  体
        :return:
        """
        self.userinfo = 0
        self.destroy()

    def commit(self):
        if self.flag == 1:  # 查看
            pass
        elif self.flag == 2:    # 添加
            # 准备数据
            temp_list = []
            if len(str(self.Entry_sno.get()).strip()) == 0:
                showinfo("系统消息", "学号不能为空！")
            else:
                temp_list.append(str(self.Entry_sno.get()).strip())
                temp_list.append(str(self.Entry_name.get()).strip())
                if self.var_gender.get() == 1:
                    temp_list.append("男")
                else:
                    temp_list.append("女")
                temp_list.append(str(self.Entry_age.get()).strip())
                temp_list.append(str(self.Entry_mobile.get()).strip())
                temp_list.append(str(self.Entry_email.get()).strip())
                temp_list.append(str(self.Entry_home.get()).strip())
                temp_list.append(str(self.Entry_id.get()).strip())
                temp_list.append(str(self.Entry_studyin.get()).strip())
                temp_list.append(str(self.Entry_pro.get()).strip())
                temp_list.append(str(self.Entry_emcon.get()).strip())
                temp_list.append(str(self.Entry_emtel.get()).strip())

                # 添加到all_student_list
                self.all_student_list.append(temp_list)
                # 提醒添加成功
                showinfo("系统消息", "学生信息添加成功")
                # 反馈信号给主窗体
                self.userinfo = 1
                # 关闭窗体
                self.destroy()
        elif self.flag == 3:    # 修改
            # 把当前界面中的数据存储在集合中
            temp_list = []
            if len(str(self.Entry_sno.get()).strip()) == 0:
                showinfo("系统消息", "学号不能为空！")
                return
            else:
                temp_list.append(str(self.Entry_sno.get()).strip())
                temp_list.append(str(self.Entry_name.get()).strip())
                if self.var_gender.get() == 1:
                    temp_list.append("男")
                else:
                    temp_list.append("女")
                temp_list.append(str(self.Entry_age.get()).strip())
                temp_list.append(str(self.Entry_mobile.get()).strip())
                temp_list.append(str(self.Entry_email.get()).strip())
                temp_list.append(str(self.Entry_home.get()).strip())
                temp_list.append(str(self.Entry_id.get()).strip())
                temp_list.append(str(self.Entry_studyin.get()).strip())
                temp_list.append(str(self.Entry_pro.get()).strip())
                temp_list.append(str(self.Entry_emcon.get()).strip())
                temp_list.append(str(self.Entry_emtel.get()).strip())
                # 遍历集合
                for index in range(len(self.all_student_list)):
                    if self.all_student_list[index][0] == self.current_student_list[0]:
                        self.all_student_list[index] = temp_list
                # 反馈信息
                # 提醒
                showinfo("系统消息", "学生信息修改成功！")
                # 反馈信号给主窗体
                self.userinfo = 1
                # 关闭窗体
                self.destroy()


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        # 定义起始参数:包括title，大小，背景颜色等等
        self.title('成绩管理系统')
        self.geometry('800x600')
        self.resizable(0, 0)
        self.config(bg='white')
        self.file_path = "A:\Documents\GitHub\ProjLearn\py\stu.txt"
        self.setup_UI()
        self.load_from_file()
        self.load_treeview(self.all_student_list)
        self.bind_event()

    def setup_UI(self):
        # 定义各种参数，包括按钮，模板，和容器
        # 创建两个Panedwindow容器，左边添加按钮，右边作为TreeView显示界面
        self.Pane_left = PanedWindow(
            width=200, height=540, style="left.TPanedwindow")
        self.Pane_left.place(x=4, y=80)
        self.Pane_right = PanedWindow(
            width=685, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=210, y=80)
        self.Pane_Top = PanedWindow(
            width=800, height=80, style="top.TPanedwindow")
        self.Pane_Top.place(x=0, y=0)
        # 添加Label
        # title.png
        self.titleImg = PhotoImage(file='title.png')
        self.titlelabel = Label(self.Pane_Top, image=self.titleImg)
        self.titlelabel.place(x=0, y=0)

        # self.Label_title = Label(self.Pane_Top, text='学生信息管理系统',
        #                          font=('黑体', 20))
        # self.Label_title.place(x=300, y=20)

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
        self.Button_query.place(x=430, y=20)
        self.Show_all = Button(self.Pane_right, text='显示全部')
        self.Show_all.place(x=520, y=20)
        # 添加Label
        self.Label_query = Label(self.Pane_right, text='学号/姓名/电话/身份证')
        self.Label_query.place(x=10, y=20)
        # 添加Entry
        self.Entry_query = Entry(self.Pane_right, width=40)
        self.Entry_query.place(x=150, y=20)
        # 添加TreeView
        self.Tree = Treeview(self.Pane_right, columns=(
            "sno", "names", "sex", "phone", "idcard", "zipcode", "address"), show="headings", height=20)
        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("names", width=100, anchor="center")
        self.Tree.column("sex", width=30, anchor="center")
        self.Tree.column("phone", width=100, anchor="center")
        self.Tree.column("idcard", width=100, anchor="center")
        self.Tree.column("zipcode", width=100, anchor="center")
        self.Tree.column("address", width=100, anchor="center")
        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("names", text="姓名")
        self.Tree.heading("sex", text="性别")
        self.Tree.heading("phone", text="电话")
        self.Tree.heading("idcard", text="身份证号")
        self.Tree.heading("zipcode", text="邮编")
        self.Tree.heading("address", text="地址")
        self.Tree.place(x=10, y=80)

    def load_from_file(self):
        self.all_student_list = []
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
            self.Tree.delete(*self.Tree.get_children())
            for index in range(len(current_list)):
                # 逐个录入加载出来的文件
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1],
                                                    current_list[index][2], current_list[index][3]))

    def bind_event(self):
        # 绑定事件
        self.Button_add.bind("<Button-1>", self.add_student)
        self.Button_update.bind("<Button-1>", self.update_student)
        self.Button_delete.bind("<Button-1>", self.delete_student)
        self.Button_query.bind("<Button-1>", self.query_student)
        self.Show_all.bind("<Button-1>", self.show_all_student)

    def add_student(self, e):
        # 添加Label
        detw = DetailWindow(
            current_student=None, all_student_list=self.all_student_list, action_flag=2)
        self.save_to_file()
        self.load_treeview(self.all_student_list)

    def update_student(self, e):
        # 获取当前选中的学生信息
        current_student = self.Tree.item(self.Tree.selection()[0], "values")
        # 弹出窗口
        detw = DetailWindow(
            current_student=current_student, all_student_list=self.all_student_list, action_flag=3)
        self.save_to_file()
        self.load_treeview(self.all_student_list)

    def delete_student(self, e):
        # 获取当前选中的学生信息
        current_student = self.Tree.item(self.Tree.selection()[0], "values")
        #删除current_student，通过学号查找
        for student in self.all_student_list:
            if student[0] == current_student[0]:
                self.all_student_list.remove(student)


        self.save_to_file()
        self.load_treeview(self.all_student_list)

    def query_student(self, e):
        # 获取当前输入的学生信息
        current_student = self.Entry_query.get()
        query_result = []
        for student in self.all_student_list:
            if current_student in student[0] or current_student in student[1] or current_student in student[2] or current_student in student[3]:
                query_result.append(student)
        self.load_treeview(query_result)

    def show_all_student(self, e):
        self.load_treeview(self.all_student_list)

    def save_to_file(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                for student in self.all_student_list:
                    f.write(",".join(student) + "\n")
        except:
            messagebox.showinfo("系统消息", "文件保存失败！")


if __name__ == '__main__':
    this_main = MainWindow()  # 调用窗口类
    this_main.mainloop()
