import numpy as np
from PIL import Image

def mod(a,b): #模运算
	c=a//b
	r=a-b*c
	return r
	
def times(n): #计算需变换多少次能恢复原图
    A=np.array([[2,1],[1,1]],dtype='int16')
    num = A
    
    E=np.array([[1,0],[0,1]])
    count=1
    
    while 1:
        count+=1
        num=mod(np.dot(num,A),n)
        if (mod(num,n)==E ).all():
            return count

def do1(path,path1):#加密
    A=np.array([[2,1],[1,1]],dtype='int16')
    img =Image.open(path)
    N=img.size[0]#图片尺寸
    n = times(N)
    print('尺寸:',N)
    print('变换次数:',n)
    x = n//2
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
    imgnew.save(savepath) #保存文件
    
def do2(path,path1):#解密
    A=np.array([[1,-1],[-1,2]],dtype='int16')
    img =Image.open(path)
    N=img.size[0]#图片尺寸
    n = times(N)
    print('尺寸:',N)
    print('变换次数:',n)
    x = n//2
    load=img.load()
    
    imgnew = Image.new('RGB', [N,N])
    newload=imgnew.load()
    
    var=A
    for i in range(x-1):
        var=mod(np.dot(var,A) , N) # 找到解密变换矩阵
    for i in range(N):
        for j in range(N):
            loc=np.array([i,j])
            
            locnew=mod(np.dot(var,loc) , N)
            newi=int(locnew[0])
            newj=int(locnew[1])
                
            newload[newi,newj] = load[i,j] #解密
    imgnew.save(savepath) #保存文件
    
    
print('用处:加密或解密 1:1比例 图片.\n')

print('用法:为了操作方便,请把文件重命名为\'1.png\'后放入首页\n')

print('注意!!!\n本操过会在对\'1.png\'本身上修改，建议另保存副本\n')

s=input('输入 0 或 1\n0：加密\n1：解密\n')
A=np.array([[2,1],[1,1]],dtype='int16')
path    =r'C:\Users\月上庭\Desktop\1.png'
savepath=r'C:\Users\月上庭\Desktop\1.png'
if s=='0':
    do1(path,savepath)        
elif s=='1':
    do2(path,savepath)
        
print('操作完成')
input("请按回车退出")

