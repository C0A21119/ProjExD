import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm #タイマー表示

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy,mx,my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1

    #上下左右で移動した場所に目隠しを入れる
    if key == "Up": canvas.create_image(cx,cy,image=kokaton10,tag="kokaton")
    if key == "Down": canvas.create_image(cx,cy,image=kokaton10,tag="kokaton")
    if key == "Left": canvas.create_image(cx,cy,image=kokaton10,tag="kokaton")
    if key == "Right": canvas.create_image(cx,cy,image=kokaton10,tag="kokaton")

    if maze_lst[mx][my] == 1: #移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    
    cx,cy = mx*100+50,my*100+50
    canvas.coords("kokaton",cx,cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    #print(maze_lst)
    mm.show_maze(canvas,maze_lst)

    kokaton = tk.PhotoImage(file="fig/8.png")
    kokaton10 = tk.PhotoImage(file="fig/10.png")
    mx,my = 1, 1
    cx,cy = mx*100+50,my*100+50
    canvas.create_image(cx,cy,image=kokaton,tag="kokaton")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()

def count_up():#タイマー表示
    global jid
    global tmr
    label["text"] = tmr
    tmr += 1 
    jid = root.after(1000, count_up)

def key_down(event):
    global jid
    if jid is not None:
        #カウントアップ中にキーが押されたら
        #カウントアップ中でないときは jid = None
        root.after_cancel(jid)
        jid = None
    else:
        jid = root.after(1000,count_up)
    #key = event.keysym    
    #tkm.showinfo("キー押下",f"{key}キーが押されました")

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text="-", font=("",80))
    label.pack()
    tmr = 0
    jid = None
    root.bind("<KeyPress>",key_down)

root.mainloop()
