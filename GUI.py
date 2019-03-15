from tkinter import *


def fillgrid():
    def check(grid):
        possible = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if grid[i][j] != '_':
                    possible[i][j] = []
                else:
                    for k in range(9):
                        if grid[i][k] != '_' and int(grid[i][k]) in possible[i][j]:
                            possible[i][j].remove(int(grid[i][k]))
                        if grid[k][j] != '_' and int(grid[k][j]) in possible[i][j]:
                            possible[i][j].remove(int(grid[k][j]))
                    for k in range(3):
                        for l in range(3):
                            if grid[i - (i % 3) + k][j - (j % 3) + l] != '_' and int(
                                    grid[i - (i % 3) + k][j - (j % 3) + l]) in possible[i][j]:
                                possible[i][j].remove(int(grid[i - (i % 3) + k][j - (j % 3) + l]))
        minlen = 9
        ind = []
        for i in range(9):
            for j in range(9):
                if 0 < len(possible[i][j]) < minlen:
                    minlen = len(possible[i][j])
                    ind = [i, j]
        grid[ind[0]][ind[1]] = possible[ind[0]][ind[1]][0]
        return grid

    grid = [[gr[i][j].get() for j in range(9)] for i in range(9)]
    while any('_' in grid[i] for i in range(9)):
        grid = check(grid)
    for i in range(9):
        for j in range(9):
            gr[i][j].configure(text=grid[i][j])


window = Tk()
window.title('Sudoku Solver')
positionRight = int(window.winfo_screenwidth()/2 - 400)
positionDown = int(window.winfo_screenheight()/2 - 400)
window.geometry("800x800+{}+{}".format(positionRight, positionDown))


title = Label(window, text='Input the grid:', font=('Arial', 30))
title.pack()
title.place(anchor='center', height=100, width=250, x=400, y=50)


subtitle = Label(window, text='Enter numbers and underscores ("_") for blanks', font=('Arial', 12))
subtitle.pack()
subtitle.place(anchor='center', height=50, width=350, x=400, y=100)


takein = Frame(window, height=400, width=400)
takein.pack()
takein.place(anchor='center', x=400, y=400)

gr = [[] for _ in range(9)]
for i in range(9):
    for j in range(9):
        gr[i].append(Entry(takein, width=3, font=("Arial", 30), justify="center"))
        gr[i][j].grid(column=i, row=j)


submit = Button(window, text='Submit Grid', font=('Arial Bold', 15), fg='green', command=fillgrid)
submit.pack()
submit.place(anchor='center', height=50, width=160, x=400, y=700)


window.mainloop()
