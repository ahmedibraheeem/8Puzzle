\from tkinter import *

i = 0
file = open("link.txt", "r")
cont = file.read()
hamada = cont.split(',')


def gui_main():
    root = Tk()

    label_1 = Label(root, width=15, height=4, foreground="red", relief=SUNKEN).grid(row=0, column=0)
    label_2 = Label(root, width=15, height=4, foreground="green", relief=SUNKEN).grid(row=0, column=3)
    label_3 = Label(root, width=15, height=4, foreground="blue", relief=SUNKEN).grid(row=0, column=6)
    label_4 = Label(root, width=15, height=4, foreground="red", relief=SUNKEN).grid(row=3, column=0)
    label_5 = Label(root, width=15, height=4, foreground="green", relief=SUNKEN).grid(row=3, column=3)
    label_6 = Label(root, width=15, height=4, foreground="blue", relief=SUNKEN).grid(row=3, column=6)
    label_7 = Label(root, width=15, height=4, foreground="red", relief=SUNKEN).grid(row=6, column=0)
    label_8 = Label(root, width=15, height=4, foreground="green", relief=SUNKEN).grid(row=6, column=3)
    label_9 = Label(root, width=15, height=4, foreground="blue", relief=SUNKEN).grid(row=6, column=6)

    button = Button(root, text="Next state!", width=8, background="silver", relief=GROOVE).grid(row=9, column=0)
    button.bind("<Button-1>", click(label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9))
    quit_button = Button(root, text="Exit!", width=8, background="silver", relief=GROOVE).grid(row=9, column=6)
    quit_button.bind("<Button-1>", quit)

    root.mainloop()


def geti():
    return i


def seti(a):
    i = a


def click(label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9):
    a = geti()
    label_1.configure(text=hamada[(a + 0) % 9])
    label_2.configure(text=hamada[(a + 1) % 9])
    label_3.configure(text=hamada[(a + 2) % 9])
    label_4.configure(text=hamada[(a + 3) % 9])
    label_5.configure(text=hamada[(a + 4) % 9])
    label_6.configure(text=hamada[(a + 5) % 9])
    label_7.configure(text=hamada[(a + 6) % 9])
    label_8.configure(text=hamada[(a + 7) % 9])
    label_9.configure(text=hamada[(a + 8) % 9])
    a += 1
    seti(a)
