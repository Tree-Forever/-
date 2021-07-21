from tkinter import *  # 从tkinter库中导入所有函数
from 加密 import encryption
from 解密 import decrypt

window1=Tk()  # 创建一个窗口

window1.title('图片处理')  # 设置窗口标题

window1.geometry('500x500+100+100')  # 设置窗口大小x和左顶距离+
 

button1=Button(window1,text='加密',command=encryption)  # 设置按钮属性
button1.pack()  # 设置显示按钮

button2=Button(window1,text='解密',command=decrypt)  # 设置按钮属性
button2.pack()  # 设置显示按钮

window1.mainloop()  # 设置窗口循环显示
