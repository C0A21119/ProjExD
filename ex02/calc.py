import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn =event.widget
    i =btn["text"]
    
    if i =="=":##イコールここで定義
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,i)
    if i == 'AC':##AC機能の追加
         entry.delete(0,tk.END)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right",width=10, font=("",40))
entry.grid(row=0,column=0, columnspan=3)


r,c = 1,0
for i in range(10):##数字の並びを逆に変更
    button = tk.Button(root,text=f"{i}",width=4,height=1,font=("",30))
    button.grid(row = r, column = c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 ==0:
        r+=1
        c =0


operators = ["+","=","*","/",".","AC","%","-"]##表示記号追加
for ope in operators:
    button = tk.Button(root,text=f"{ope}",width=4,height=1,font=("",30),fg='#ff0000')##演算記号を赤で表示'#ff0000で赤を示している
    button.grid(row = r, column = c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 ==0:
        r+=1
        c =0

root.mainloop()