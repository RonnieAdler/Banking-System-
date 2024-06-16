import tkinter as tk
win2=tk.Tk()
win2.geometry("400x250")
uname = tk.Label(text = "Username").place(x = 30,y = 50)
password = tk.Label(text = "Password", show='x').place(x = 30, y = 90)
sbmitbtn = tk.Button(text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 120)
e1 = tk.Entry(width = 20).place(x = 100, y = 50)
e2 = tk.Entry(width = 20, show='x').place(x = 100, y = 90)
win2.mainloop()
