import tkinter as tk
def rgfrsb():
    winin=tk.Tk()
    winin.geometry('500x100')
    winin.title("Registration Form")

    ki=tk.Label(winin, text="Form Submitted Successfully.....")
def rgstfrm():
    win3=tk.Tk()
    win3.geometry('500x600')
    win3.title("Registration Form")
    
    hd=tk.Label(win3, text="Registration form",width=20,font=("bold", 20))
    hd.place(x=90, y=53)
    
    flnm= tk.Label(win3, text="FullName",width=20,font=("bold", 10)).place(x=63,y=130)
    e1=tk.Entry(win3,width=20).place(x=240,y=130)
    phnno= tk.Label(win3, text="Phone No.",width=20,font=("bold", 10)).place(x=66,y=180)
    e2=tk.Entry(win3,width=20).place(x=240,y=180)
    email= tk.Label(win3, text="E-Mail",width=20,font=("bold", 10)).place(x=56,y=230)
    e3=tk.Entry(win3,width=20).place(x=240,y=230)
    bankacc= tk.Label(win3, text='''Bank Account
(Optional)''',width=20,font=("bold", 10)).place(x=65,y=280)
    e4=tk.Entry(win3,width=20).place(x=240,y=280)                                                                                         
    gender= tk.Label(win3, text="Gender",width=20,font=("bold", 10)).place(x=58,y=332)
    rm=tk.Radiobutton(win3, text="Male",padx = 5, value=1).place(x=235,y=330)
    rf=tk.Radiobutton(win3, text="Female",padx = 20, value=2).place(x=290,y=330)
    aadharno= tk.Label(win3, text="Aadhar no.", width=20,font=("bold", 10)).place(x=68,y=380)
    e5=tk.Entry(win3,width=20).place(x=240,y=380)
    age = tk.Label(win3, text="Age:",width=20,font=("bold", 10)).place(x=55,y=420)
    e6=tk.Entry(win3,width=20).place(x=240,y=420)

    sub=tk.Button(win3, text='Submit',width=20,bg='brown',fg='white',command=rgfrsb).place(x=180,y=520)
    win3.mainloop()


rgstfrm()
