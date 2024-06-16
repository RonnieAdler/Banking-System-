import tkinter as tk

import tkinter.font as font
def login():
    win2=tk.Toplevel(win)
    win2.geometry("400x250")

    uname = tk.Label(win2, text = "Username").place(x = 30,y = 50)
    password = tk.Label(win2, text = "Password").place(x = 30, y = 90)

    sbmitbtn = tk.Button(win2, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 120)

    e1 = tk.Entry(win2, width = 20).place(x = 100, y = 50)
    e2 = tk.Entry(win2, width = 20, show='*').place(x = 100, y = 90)


win=tk.Tk(className='myAccount')
win.geometry("500x550")

c=tk.Canvas( bg="white", height="1050", width="1000")

ft=font.Font(win,size=30, weight="bold", family="Consolas")
fto=font.Font(win,size=20, weight="bold", family="Fixedsys")

hlp=tk.Button(text="help")
b_ct= tk.Button(text="Sign up", pady=10, padx=50, relief="raised")
b_lg= tk.Button(text="Login",fg="blue", pady=10, padx=50, command=login)

hlp['font']=fto
b_ct['font']=ft
b_lg['font']=ft

b_ct.pack(side="top")
b_lg.pack(side="top")
hlp.pack(side="bottom")

c.pack()

win.mainloop()
