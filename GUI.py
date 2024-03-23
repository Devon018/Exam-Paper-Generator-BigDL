import tkinter as tk
from tkinter import ttk
import os
import threading
import time
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import Data_collection
import changeToLatex
import ask_model

class ExamPaperGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.data = Data_collection.Data_collection()
        self.title("高中语文试卷生成器")
        self.geometry("800x300")
        self.path_ = None
        # 试卷生成路径
        self.path = tk.StringVar()
        self.path.set(os.path.abspath("."))

        # 输出文件格式
        self.file_format = tk.StringVar(self)
        self.file_format.set("选择格式...")

        # 试卷内容显示
        self.progress_info = tk.StringVar(self)

        # 动态更新文件格式下拉框的函数
        self.update_file_format()

        # 创建控件
        self.create_widgets()

    def create_widgets(self):

        # tk.Label(self, text="试卷生成路径：").grid(row=0, column=0, sticky="e")
        path_dropdown = ttk.OptionMenu(self, self.path, *os.listdir('.'))
        path_dropdown.grid(row=0, column=1, sticky="we")
        tk.Label(self, text="目标路径:").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.path, state="readonly").grid(row=0, column=1, ipadx=200)

        tk.Button(self, text="路径选择", command=self.selectPath).grid(row=0, column=2)
        tk.Button(self, text="生成试卷", command=self.generate_exam_paper).grid(row=2, column=0, columnspan=2, sticky="ew", pady=4)

        tk.Label(self, textvariable=self.progress_info).grid(row=3, column=0, columnspan=2, sticky="we")

    def selectPath(self):
        self.path_ = askdirectory()  # 使用askdirectory()方法返回文件夹的路径
        if self.path_ == "":
            self.path.set()
        else:
            self.path_ = self.path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
            self.path.set(self.path_)

    def update_file_format(self):
        # 根据路径动态更新格式下拉框
        self.file_format.set("选择格式...")
        format_dropdown = ttk.OptionMenu(self, self.file_format, *self.get_formats())
        format_dropdown.grid(row=1, column=1, sticky="we")

    def get_formats(self):
        # 示例：根据路径返回可用的文件格式
        return ['pdf']

    def generate_exam_paper(self):
        # 模拟试卷生成过程
        self.progress_info.set("正在生成试卷，请稍等...")
        self.update()  # 更新GUI
        threading.Thread(target=self.generate_thread).start()

    def generate_thread(self):

        # 模拟试卷生成操作，这个函数在后台线程中运行
        self.progress_info.set("正在收集现代文阅读I")
        self.data.collect(0,[])
        self.progress_info.set("正在收集现代文阅读II")
        self.data.collect(1,[])
        self.progress_info.set("正在收集文言文阅读")
        self.data.collect(2,[])
        self.progress_info.set("正在收集古诗文阅读")
        self.data.collect(3,[])
        # 调用模型生成题目
        ask_model.ask()

        # 将题目转换为PDF文档
        changeToLatex.template()
        changeToLatex.compile_tex_to_pdf(self.path_)

        # 生成完毕
        self.progress_info.set("试卷生成完毕！")
        self.after(100, self.generate_complete)  # 0.1秒后显示完成提示
        self.path = str(self.path).replace('\\','\\\\')
        self.generate_complete()
    def generate_complete(self):
        # 提示试卷生成完成
        messagebox.showinfo("完成", "试卷已经生成完毕！")

