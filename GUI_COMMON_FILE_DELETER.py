def action():
    
    one=first.get()
    sec=second.get()
    try:
        s=os.listdir(one)
        t=os.listdir(sec)
        for i in s:
           if i in t:
              song=os.path.join(sec,i)
              os.remove(song)
        tkinter.messagebox.showinfo("Successfull","Common Files Deleted")      
              
    except:
        lable_one=ttk.Label(win,text="INVAILID PATH",font=('ariel',30)).grid(row=3,column=1)
        lable_one=ttk.Label(win,text="TRY AGAIN",font=('ariel',30)).grid(row=10,column=1)
import os,tkinter
from tkinter import ttk
import tkinter.messagebox
win=tkinter.Tk()
win.title("COMMON FILE DELETER")
first=tkinter.StringVar()
second=tkinter.StringVar()
lable_one=ttk.Label(win,text="<----COMMON FILE DELETER---->",font=('ariel',30)).grid(row=0,column=0)
lable_one=ttk.Label(win,text="ADRESS OF FIRST FOLDER---->",font=('ariel',20)).grid(row=4,column=0)
input_box_one=ttk.Entry(win,font=('ariel',20),textvariable=first,width=40).grid(row=4,column=1)
lable_one=ttk.Label(win,text="ADRESS OF SECOND FOLDER---->",font=('ariel',20)).grid(row=6,column=0)
lable_one=ttk.Label(win,text="(also from which you want to remove file)",font=('ariel',10)).grid(row=7,column=0)
input_box_two=ttk.Entry(win,font=('ariel',20),textvariable=second,width=40).grid(row=6,column=1)
style=ttk.Style()
style.configure("TButton",font=('verdana',20))
btn=ttk.Button(win,text="PROCEED FOR ACTION",command=action).grid(row=8,column=1)
win.mainloop()


