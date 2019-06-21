# code by mars NEU 
# Hangzhou
from PIL import ImageTK
from tkinter import *
import PIL
from PIL import Image 
imort tkinter as tk 
import os
import matplotlib.pyplot as plt 
import tkinter.messagebox
 
root_path = 'Z:/110110/code/need_pick_by_hand_list.txt'
 
img_list = []
for i in open(root_path,'r',encoding='UTF-8')
    img_list.append(i[:len(i)-1])
length = len(img_list)
str_v1 =StringVar
num=0
def last_image():
    global num,names,f_file_log
    f_file_log=open('Z:110110/code/log.txt','w')
    f_file_log.write(str(num))
    del names['path'+str(num)]
    del names['pilimage'+str(num)]
    del names['im_w'+str(num)]
    del names['im_h'+str(num)]
    del names['img'+str(num)]
    num = num -1
    if(num<0):
        tk.messagebox.showinfo(title='提示',message='已经到头了！')
    else:
        names['path'+str(num)] = img_list[num]
        names['pilimage'+str(num)] = Image.open(names['path'+str(num)])
        names['im_w'+str(num)] = names['pilimage'+str(num)].size[0]
        names['im_h'+str(num)] = names['pilimage'+str(num)].size[1]
        alpha = names['im_h'+str(num)]/names['im_w'+str(num)]
        names['pilimage'+str(num)] = names['pilimage'+str(num)].resize((int(120*alpha),120))
        names['img'+str(num)] = ImageTK.PhotoImage(names['pilimage'+str(num)])
        imLabel.configure(image=names['img'+str(num)])
        txLabel.configure(text='No: '+str(num))
        nm_en.delete(0,END)
        nm_en.insert(0,img_list[num].split('/')[-1])
        nm_en1.delete(0,END)
        nm_en1.insert(0,img_list[num].split('\\')[-1])
def next_image():
    global num,names,f_file_log
    f_file_log=open('Z:110110/code/log.txt','w')
    f_file_log.write(str(num))
    del names['path'+str(num)]
    del names['pilimage'+str(num)]
    del names['im_w'+str(num)]
    del names['im_h'+str(num)]
    del names['img'+str(num)]
    num = num +1
    if(num>length-1):
        tk.messagebox.showinfo(title='提示',message='已经没有了！')
    else:
        names['path'+str(num)] = img_list[num]
        names['pilimage'+str(num)] = Image.open(names['path'+str(num)])
        names['im_w'+str(num)] = names['pilimage'+str(num)].size[0]
        names['im_h'+str(num)] = names['pilimage'+str(num)].size[1]
        alpha = names['im_h'+str(num)]/names['im_w'+str(num)]
        names['pilimage'+str(num)] = names['pilimage'+str(num)].resize((int(120*alpha),120))
        names['img'+str(num)] = ImageTK.PhotoImage(names['pilimage'+str(num)])
        imLabel.configure(image=names['img'+str(num)])
        txLabel.configure(text='No: '+str(num))
        nm_en.delete(0,END)
        nm_en.insert(0,img_list[num].split('/')[-1])
        nm_en1.delete(0,END)
        nm_en1.insert(0,img_list[num].split('\\')[-1])
 
def pick_image00():
    global num,names,f_file_log,f_file00
    f_file_log=open('Z:110110/code/log.txt','w')
    f_file_log.write(str(num))
    f_file00.open('Z:110110/code/pick00.txt')
    f_file00.write(img_list[num])
    f_file00.write('\n')
    f_file00.close()
    del names['path'+str(num)]
    del names['pilimage'+str(num)]
    del names['im_w'+str(num)]
    del names['im_h'+str(num)]
    del names['img'+str(num)]
    num = num +1
    if(num>length-1):
        tk.messagebox.showinfo(title='提示',message='已经没有了！')
    else:
        names['path'+str(num)] = img_list[num]
        names['pilimage'+str(num)] = Image.open(names['path'+str(num)])
        names['im_w'+str(num)] = names['pilimage'+str(num)].size[0]
        names['im_h'+str(num)] = names['pilimage'+str(num)].size[1]
        alpha = names['im_h'+str(num)]/names['im_w'+str(num)]
        names['pilimage'+str(num)] = names['pilimage'+str(num)].resize((int(120*alpha),120))
        names['img'+str(num)] = ImageTK.PhotoImage(names['pilimage'+str(num)])
        imLabel.configure(image=names['img'+str(num)])
        txLabel.configure(text='No: '+str(num))
        nm_en.delete(0,END)
        nm_en.insert(0,img_list[num].split('/')[-1])
        nm_en1.delete(0,END)
        nm_en1.insert(0,img_list[num].split('\\')[-1])
 
def pick_image01():
    global num,names,f_file_log,f_file00
    f_file_log=open('Z:110110/code/log.txt','w')
    f_file_log.write(str(num))
    f_file00.open('Z:110110/code/pick01.txt')
    f_file00.write(img_list[num])
    f_file00.write('\n')
    f_file00.close()
    del names['path'+str(num)]
    del names['pilimage'+str(num)]
    del names['im_w'+str(num)]
    del names['im_h'+str(num)]
    del names['img'+str(num)]
    num = num +1
    if(num>length-1):
        tk.messagebox.showinfo(title='提示',message='已经没有了！')
    else:
        names['path'+str(num)] = img_list[num]
        names['pilimage'+str(num)] = Image.open(names['path'+str(num)])
        names['im_w'+str(num)] = names['pilimage'+str(num)].size[0]
        names['im_h'+str(num)] = names['pilimage'+str(num)].size[1]
        alpha = names['im_h'+str(num)]/names['im_w'+str(num)]
        names['pilimage'+str(num)] = names['pilimage'+str(num)].resize((int(120*alpha),120))
        names['img'+str(num)] = ImageTK.PhotoImage(names['pilimage'+str(num)])
        imLabel.configure(image=names['img'+str(num)])
        txLabel.configure(text='No: '+str(num))
        nm_en.delete(0,END)
        nm_en.insert(0,img_list[num].split('/')[-1])
        nm_en1.delete(0,END)
        nm_en1.insert(0,img_list[num].split('\\')[-1])
 
 
def pick_image02():
    global num,names,f_file_log,f_file00
    f_file_log=open('Z:110110/code/log.txt','w')
    f_file_log.write(str(num))
    f_file00.open('Z:110110/code/pick02.txt')
    f_file00.write(img_list[num])
    f_file00.write('\n')
    f_file00.close()
    del names['path'+str(num)]
    del names['pilimage'+str(num)]
    del names['im_w'+str(num)]
    del names['im_h'+str(num)]
    del names['img'+str(num)]
    num = num +1
    if(num>length-1):
        tk.messagebox.showinfo(title='提示',message='已经没有了！')
    else:
        names['path'+str(num)] = img_list[num]
        names['pilimage'+str(num)] = Image.open(names['path'+str(num)])
        names['im_w'+str(num)] = names['pilimage'+str(num)].size[0]
        names['im_h'+str(num)] = names['pilimage'+str(num)].size[1]
        alpha = names['im_h'+str(num)]/names['im_w'+str(num)]
        names['pilimage'+str(num)] = names['pilimage'+str(num)].resize((int(120*alpha),120))
        names['img'+str(num)] = ImageTK.PhotoImage(names['pilimage'+str(num)])
        imLabel.configure(image=names['img'+str(num)])
        txLabel.configure(text='No: '+str(num))
        nm_en.delete(0,END)
        nm_en.insert(0,img_list[num].split('/')[-1])
        nm_en1.delete(0,END)
        nm_en1.insert(0,img_list[num].split('\\')[-1])
 
def key(event):
    if(event.char=='6'):
        next_image()
    if(event.char=='2'):
        pick_image02()
    if(event.char=='4'):
        last_image()
 
names = locals()
root = tk.Tk()
root = title(FYJ)
root['background'] ='mintcream'
root.geometry(1800x1080)
root.resizable(width=False,height=False)
btn1 = tk.Button(root,text='Next Image',command=next_image)
btn1['background']='mintcream'
btn1.place(x=10,y=10,width=120,height=30)
 
btn2 = tk.Button(root,text='Class 1',command=pick_image00)
btn2['background']='mintcream'
btn2.place(x=10,y=180,width=120,height=30)
 
btn3 = tk.Button(root,text='Class 2',command=pick_image01)
btn3['background']='mintcream'
btn3.place(x=10,y=350,width=120,height=30)
 
btn4 = tk.Button(root,text='Class 3',command=pick_image02)
btn4['background']='mintcream'
btn4.place(x=10,y=520,width=120,height=30)
txLabel = tk.Label(root,text='No: '+str(num))
txLabel['background']='mintcream'
txLabel.place(x=10,y=570,width=120,height=30)
nm_en = Entry(root,textvariable=str_v1)
nm_en['background']='mintcream'
nm_en.insert(0,img_list[num])
nm_en.place(x=10,y=630,width=120,height=30)
 
nm_en1 = Entry(root,textvariable=str_v1)
nm_en1['background']='mintcream'
nm_en1.insert(0,img_list[num].split('\\')[-1])
nm_en1.place(x=10,y=730,width=120,height=30)
 
frame = tk.Frame(root,width=100,height=100,background='pink')
frame.bind('<Key>',key)
frame.place(x=10,y=800,width=120,height=30)
frame.focus_set()
 
txLabel1 = tk.Label(root,text='Total: '+str(length))
txLabel1['background']='mintcream'
txLabel1.place(x=10,y=600,width=120,height=30)
names['path'+str(num)] = img_list[num]
names['pilimage'+str(num)] = Image.open(names['path'+str(num)])
names['im_w'+str(num)] = names['pilimage'+str(num)].size[0]
names['im_h'+str(num)] = names['pilimage'+str(num)].size[1]
alpha = names['im_h'+str(num)]/names['im_w'+str(num)]
names['pilimage'+str(num)] = names['pilimage'+str(num)].resize((int(120*alpha),120))
names['img'+str(num)] = ImageTK.PhotoImage(names['pilimage'+str(num)])
imLabel=tk.Label(root,image=names['img'+str(num)],width = 800,height=350)
imLabel['background']='mintcream'
imLabel.pack()
root.mainloop()
