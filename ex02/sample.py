import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(root,
                text="らべるを書いてみた件",
                font=("",20)
                )
label.pack()                    ##packは必須

entry = tk.Entry(root,width=30)   ##幅半角30文字
entry.insert(tk.END,"fugapiyo")    ##デフォルトで文字を入力 p.15
entry.pack()

##def button_click():
##   tkm.showwarning("警告","ボタン押したらあかん言うたやろ")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

button = tk.Button(root,text="押すな", command=button_click)
button.bind("<1>",button_click)
button.pack()

##tk.showerror("たいとる","めっせーじ")

root.mainloop()

