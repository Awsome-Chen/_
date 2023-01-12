import tkinter as tk
import tkinter.font as tk_font

class Show():
    def __init__(self,info:str):
        win = tk.Tk()
        win.geometry("500x50+100+100")
        win.title("每日按时查询转专业信息")
        win.resizable(0,0)
        font_style = tk_font.Font(family="得意黑",size=28)
        tk.Label(win,text=info,font=font_style).pack()
        win.mainloop()
