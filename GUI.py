from tkinter import *


def fillgrid():
    grid = [[gr[i][j].get() for j in range(9)] for i in range(9)]


window = Tk()
window.title('Sudoku Solver')
positionRight = int(window.winfo_screenwidth()/2 - 400)
positionDown = int(window.winfo_screenheight()/2 - 400)
window.geometry("800x800+{}+{}".format(positionRight, positionDown))


title = Label(window, text='Input the grid:', font=('Arial', 30))
title.pack()
title.place(anchor='center', height=100, width=250, x=400, y=50)


subtitle = Label(window, text='Enter numbers and leave blanks blank', font=('Arial', 12))
subtitle.pack()
subtitle.place(anchor='center', height=50, width=350, x=400, y=100)


takein = Frame(window, height=400, width=400)
takein.pack()
takein.place(anchor='center', x=400, y=400)

gr = [[] for _ in range(9)]
for i in range(9):
    for j in range(9):
        gr[i].append(Entry(takein, width=3, font=("Arial", 30), justify="center"))
        gr[i][j].grid(column=j, row=i)


submit = Button(window, text='Submit Grid', font=('Arial Bold', 15), fg='green', command=fillgrid)
submit.pack()
submit.place(anchor='center', height=50, width=160, x=400, y=700)


window.mainloop()
