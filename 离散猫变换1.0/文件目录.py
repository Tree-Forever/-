import os

def showPicAndFold(dirs):
       loc=0
       fold=[]
       pic=[]
       for i in dirs:
              if os.path.isdir(i):
                     fold.append((i,''))
              elif os.path.splitext(i)[1]=='.png':
                     pic.append((os.path.splitext(i)[0],os.path.splitext(i)[1]))
       print('0\t..')
       for i in fold:
       	loc+=1
       	print('%d\t%s\tfolder'%(loc,i[0]))
       for i in pic:
       	loc+=1
       	print('%d\t%s\tpng'%(loc,i[0]))
       return fold+pic


print(os.name,'\n')
imgType_list = {'jpg','bmp','png','jpeg','rgb','tif'}
txt=os.getcwd()+'/1.txt'
while 1:
       path=os.getcwd()
       try:
              dirs = os.listdir('.') #file list
       except PermissionError:
              print('拒绝访问')
              
       print(path,'\n')

       viewfile=showPicAndFold(dirs)
       s=int(input())
       if s==0:
              os.chdir('..')
       elif 1<= s <=len(dirs):
              filename=path+'\\'+viewfile[s-1][0]+viewfile[s-1][1]
              if os.path.splitext(filename)[1]=='.png':
                     f=open(txt,'w')
                     pngname=filename
                     f.write(pngname)
                     f.close()
                     print('Select OK')
                     break
              else:
                     os.chdir(os.path.join('.',filename))

