 import numpy as np
from PIL import Image
import os

def marpow(A,n):
	a=A
	for i in range(n-1):
		a=np.dot(a,A)
	return a
	
def mod(a,b):
	c=a//b
	r=a-b*c
	return r
	
def times(n,A):
    num = A
    
    E=np.array([[1,0],[0,1]])
    count=1
    
    while 1:
        count+=1
        num=mod(np.dot(num,A),n)
        if (mod(num,n)==E ).all():
            return count

def do1(path,path1,A):
    img =Image.open(path)
    N=img.size[0]
    n=times(N,A)
    print(N)
    print(n)
    x = n//2-1
    load=img.load()
    
    imgnew = Image.new('RGB', [N,N])
    newload=imgnew.load()
    
    var=A
    for i in range(x-1):
        var=mod(np.dot(var,A) , N)
    for i in range(N):
        for j in range(N):
            loc=np.array([i,j])
            
            locnew=mod(np.dot(var,loc) , N)
            newi=int(locnew[0])
            newj=int(locnew[1])
                
            newload[newi,newj] = load[i,j]
    imgnew.save(savepath)
    
def do2(path,path1,A):
    img =Image.open(path)
    N=img.size[0]
    n=times(N,A)
    print(N)
    print(n)
    x = n - n//2+1
    load=img.load()
    
    imgnew = Image.new('RGB', [N,N])
    newload=imgnew.load()
    
    var=A
    for i in range(x-1):
        var=mod(np.dot(var,A) , N)
    for i in range(N):
        for j in range(N):
            loc=np.array([i,j])
            
            locnew=mod(np.dot(var,loc) , N)
            newi=int(locnew[0])
            newj=int(locnew[1])
                
            newload[newi,newj] = load[i,j]
    imgnew.save(savepath) 
    

txt=os.getcwd()+'/1.txt'
with open(txt,'r') as f:
	s=f.read()
path = s
savepath=r'C:\Users\月上庭\Desktop\1.png'
 
print('用处:加密或解密 1:1比例 图片.\n')
print('注意：请认真检查所选路径是否正确!!')
print('path:',path)
print('savepath:',savepath)

s=input('输入 0 或 1\n0：加密\n1：解密\n')
A=np.array([[2,1],[1,1]],dtype='int16')

if s=='0':
    do1(path,savepath,A)        
elif s=='1':
    do2(path,savepath,A)
        
print('操作完成')

