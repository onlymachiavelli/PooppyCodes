from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("XO by SpaceStudio")
index = ["B"]*9
pl = 0
lindex = len(index)
def ver():
    global  lindex
    global index
    if index[0]=="X" and index[1]=="X" and index[2] == "X" :
        button[0].configure(bg="#ff0000")
        button[1].configure(bg="#ff0000")
        button[2].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"]*9
        for i in range (lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[0]== "X" and index[3]== "X" and index[6] == "X":
        button[0].configure(bg="#ff0000")
        button[3].configure(bg="#ff0000")
        button[6].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[6]== "X" and index[7]== "X" and index[8] == "X":
        button[6].configure(bg="#ff0000")
        button[7].configure(bg="#ff0000")
        button[8].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[8]== "X" and index[5]== "X" and index[2] == "X":
        button[8].configure(bg="#ff0000")
        button[5].configure(bg="#ff0000")
        button[2].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[0]== "X" and index[4]== "X" and index[8] == "X":
        button[0].configure(bg="#ff0000")
        button[4].configure(bg="#ff0000")
        button[8].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[1]== "X" and index[4]== "X" and index[7] == "X":
        button[1].configure(bg="#ff0000")
        button[4].configure(bg="#ff0000")
        button[7].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[3]== "X" and index[4]== "X" and index[5] == "X":
        button[3].configure(bg="#ff0000")
        button[4].configure(bg="#ff0000")
        button[5].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[2]== "X" and index[4]== "X" and index[6] == "X":
        button[2].configure(bg="#ff0000")
        button[4].configure(bg="#ff0000")
        button[6].configure(bg="#ff0000")
        messagebox.showinfo("XO","Player X just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[0]== "O" and index[1]== "O" and index[2] == "O" :
        button[0].configure(bg="#00CCFF")
        button[1].configure(bg="#00CCFF")
        button[2].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[0]== "O" and index[3]== "O" and index[6] == "O":
        button[0].configure(bg="#00CCFF")
        button[3].configure(bg="#00CCFF")
        button[6].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[6]== "O" and index[7]== "O" and index[8] == "O":
        button[6].configure(bg="#00CCFF")
        button[7].configure(bg="#00CCFF")
        button[8].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[8]== "O" and index[5]== "O" and index[2] == "O":
        button[8].configure(bg="#00CCFF")
        button[5].configure(bg="#00CCFF")
        button[2].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[0]== "O" and index[4]== "O" and index[8] == "O":
        button[0].configure(bg="#00CCFF")
        button[4].configure(bg="#00CCFF")
        button[8].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[1]== "O" and index[4]== "O" and index[7] == "O":
        button[1].configure(bg="#00CCFF")
        button[4].configure(bg="#00CCFF")
        button[7].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[3]== "O" and index[4]== "O" and index[5] == "O":
        button[3].configure(bg="#00CCFF")
        button[4].configure(bg="#00CCFF")
        button[5].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
    elif index[2]== "O" and index[4]== "O" and index[6] == "O":
        button[2].configure(bg="#00CCFF")
        button[4].configure(bg="#00CCFF")
        button[6].configure(bg="#00CCFF")
        messagebox.showinfo("XO","Player O just WON!")
        index = ["B"] * 9
        for i in range(lindex):
            button[i].configure(text=index[i], bg="#339966")
def verplace(n):
    if index[n] !="B" :
        messagebox.showinfo("XO", "Sorry ! this index is already tooken ! try again")
        return False
    return True
def btn(n):
    global  pl
    if (pl == 0):
        if verplace(n):
            pl = 1
            index[n] = "X"
            button[n].configure(text=index[n])
            ver()
    else:
        if verplace(n):
            pl = 0
            index[n] = "O"

            button[n].configure(text=index[n])
            ver()
button = [None] * 9
button[0] = Button(root, text=index[0], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(0))
button[0].grid(row=0, column=0)
button[1] = Button(root, text=index[1], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(1))
button[1].grid(row=0, column=1)
button[2] = Button(root, text=index[2], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(2))
button[2].grid(row=0, column=2)
button[3] = Button(root, text=index[3], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(3))
button[3].grid(row=1, column=0)
button[4] = Button(root, text=index[4], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(4))
button[4].grid(row=1, column=1)
button[5] = Button(root, text=index[5], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(5))
button[5].grid(row=1, column=2)
button[6] = Button(root, text=index[6], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(6))
button[6].grid(row=2, column=0)
button[7] = Button(root, text=index[7], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(7))
button[7].grid(row=2, column=1)
button[8] = Button(root, text=index[8], padx=20,pady=16, fg="#fff", bg="#339966", command=lambda : btn(8))
button[8].grid(row=2, column=2)
root.mainloop()
