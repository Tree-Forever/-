
'''
Python 使用离散猫变换对图片进行加密
创建者: 张树庭
'''

import win32ui
import win32api,win32con
import numpy as np
from PIL import Image
import sys

def encryption():
        
        def mod(a,b): #模运算
                c=a//b
                r=a-b*c
                return r
        
        def times(n,A): #计算需变换多少次能恢复原图
            num = A
            
            E=np.array([[1,0],[0,1]])
            count=1
            
            while 1:
                count+=1
                num=mod(np.dot(num,A),n)
                if (mod(num,n)==E ).all():
                    return count
               
        def do(path,A):#加密
            img =Image.open(path)
            N=img.size[0]#图片尺寸
            n = times(N,A)
            print('尺寸:',N)
            print('变换次数:',n)
            x = n//2-1
            load=img.load()
            
            imgnew = Image.new('RGB', [N,N])
            newload=imgnew.load()
            
            var=A
            for i in range(x-1):
                var=mod(np.dot(var,A) , N) # 找到加密变换矩阵
            for i in range(N):
                for j in range(N):
                    loc=np.array([i,j])
                    
                    locnew=mod(np.dot(var,loc) , N)
                    newi=int(locnew[0])
                    newj=int(locnew[1])
                        
                    newload[newi,newj] = load[i,j] #加密
            return imgnew



        def select_file():
                dlg= win32ui.CreateFileDialog(1)# 1表示打开文件对话框
                dlg.SetOFNInitialDir('C://')# 设置打开文件对话框中的初始显示目录
                num = dlg.DoModal()
                if num==2:
                        os._exit()

                return dlg.GetPathName()# 获取选择的文件名称

        def save_file():
                dlg= win32ui.CreateFileDialog(0)# 0表示打开另存为对话框
                dlg.SetOFNInitialDir('C://')# 设置另存为文件对话框中的初始显示目录
                num = dlg.DoModal()
                if num==2:
                        sys.exit(0)
               
                return dlg.GetPathName()# 获取选择的文件名称


        win32api.MessageBox(0, "加密 1:1 图片", "标题",0)
        A=np.array([[2,1],[1,1]],dtype='int16')
        while True:
              path = select_file()
              
              if path.endswith('.png') or path.endswith('.jpg'):
                        imgnew = do(path,A)
                        save_path = save_file()
                        imgnew.save(save_path)
                        win32api.MessageBox(0, "操作完成", "标题",win32con.MB_OK)
                        return 1
              else:
                        num = win32api.MessageBox(0, "非图片文件，是否重试", "Worng",win32con.MB_RETRYCANCEL)
                        if num==2:
                              sys.exit(0)


if __name__ == '__main__':
       encryption()
