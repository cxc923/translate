# -*- coding:utf-8 -*-
# Author : CXC
# Data : 2019/8/16 10:52

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import requests


def messages():
    content = text1.get(0.0, END)
    content = content.strip()
    if content == "":
        messagebox.showinfo('提示', '请输入需要翻译的内容！')
    else:
        data = {
            "i": content,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTIME",
            "typoResult": "false"

        }
        response = requests.post("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",
                                 data=data).json()
        # print(response)
        translate = response["translateResult"][0][0]["tgt"]  # 获取译文
        # 译文多行显示
        text2.insert(INSERT, translate)


def clean():
    """清空多行文本框以及弹出提示框"""
    content = text1.get(0.0, END)
    content = content.strip()
    if content == "":
        messagebox.showinfo('提示', '别点了，没有数据！！！')
    text2.delete(0.0, END)
    text1.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '每翻译一次请清空数据在进行翻译')
    window.quit()


if __name__ == '__main__':
    # 翻译工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("翻译软件v1.0")
    # 设置窗口大小
    window.geometry("800x600")
    # 禁止最大窗口
    window.resizable(0, 0)
    # 在界面上设定label1标签，（Label标签用于显示一个文本或图像）
    label1 = tk.Label(window, text="原文：", font="华文新魏 15", height=2)
    # 放置label标签
    label1.place(height=20, width=71, x=45, y=30)
    label2 = tk.Label(window, text="译文：", font="华文新魏 15", height=2)
    label2.place(height=21, width=82, x=460, y=30)
    # 接收翻译后的内容（设置Text标签，多行文本框，可用来收集或显示多行文本）
    text1 = tk.Text(window, width=32, font=('黑体', 12))
    text1.place(height=280, width=260, x=52, y=90)
    text2 = tk.Text(window, width=32, font=('黑体', 12))
    text2.place(height=280, width=260, x=476, y=90)
    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="开始翻译", command=messages, width=10, font="华文中宋 12")
    button1.place(height=41, width=152, x=52, y=420)
    button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    button2.place(height=42, width=147, x=590, y=420)
    button3 = tk.Button(window, text="清空数据", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=42, width=147, x=320, y=420)
    # 主窗口循环显示
    window.mainloop()
