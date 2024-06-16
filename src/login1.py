import tkinter as tkk
win2=tkk.Tk()
win2.geometry("400x250")
uname = tkk.Label(text = "Username").place(x = 30,y = 50)
password = tkk.Label(text = "Password").place(x = 30, y = 90)
sbmitbtn = tkk.Button(text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 120)
e1 = tkk.Entry(width = 20).place(x = 100, y = 50)
e2 = tkk.Entry(width = 20, show='*').place(x = 100, y = 90)
win2.mainloop()
