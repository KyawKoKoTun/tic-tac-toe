from tkinter import *
from tkinter import messagebox

class MyButton(Button):
    def __init__(self, root, func, i):
        super().__init__(root)
        self.configure(text= ' ', width=5, font=("ariel", 40, 'bold'), bg='#333333', fg='white',  command=lambda: func(i))
        self.no = i
        self.activated = i

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tic-Tac-Toe Player 1')
        self.root.wm_resizable(width=False, height=False)
        self.mode = True
        self.b1 = MyButton(self.root, self.mark, 0)
        self.b2 = MyButton(self.root, self.mark, 1)
        self.b3 = MyButton(self.root, self.mark, 2)
        self.b4 = MyButton(self.root, self.mark, 3)
        self.b5 = MyButton(self.root, self.mark, 4)
        self.b6 = MyButton(self.root, self.mark, 5)
        self.b7 = MyButton(self.root, self.mark, 6)
        self.b8 = MyButton(self.root, self.mark, 7)
        self.b9 = MyButton(self.root, self.mark, 8)
        self.grids = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        for grid in self.grids:
            grid.grid(row=int(self.grids.index(grid)/3), column=int(self.grids.index(grid)%3))

    def mark(self, index):
        if not (self.grids[index].activated=='o' or self.grids[index].activated=='x'):
            self.grids[index].configure(text= 'x' if self.mode else 'o')
            self.grids[index].activated = 'x' if self.mode else 'o'
            self.mode = not self.mode
            self.root.title('Tic-Tac-Toe Player 1') if self.mode else self.root.title('Tic-Tac-Toe Player 2')
            if (self.b1.activated == self.b2.activated and self.b2.activated == self.b3.activated
            ) or (self.b4.activated == self.b5.activated and self.b5.activated ==  self.b6.activated
            ) or (self.b7.activated == self.b8.activated and self.b8.activated  == self.b9.activated
            ) or (self.b1.activated == self.b4.activated and self.b4.activated  == self.b7.activated
            ) or (self.b2.activated == self.b5.activated and self.b5.activated  == self.b8.activated
            ) or (self.b3.activated == self.b6.activated and self.b6.activated  == self.b9.activated
            ) or (self.b1.activated == self.b5.activated and self.b5.activated  == self.b9.activated
            ) or (self.b3.activated == self.b5.activated and self.b5.activated  == self.b7.activated):
                if self.mode:
                    messagebox.showinfo(title='Tic-Tac-Toe', message='Player 2 win!')
                else:
                    messagebox.showinfo(title='Tic-Tac-Toe', message='Player 1 win!')
                self.restart()
            a = []
            for grid in self.grids:
                a.append(True) if grid.activated == 'o' or grid.activated == 'x' else a.append(False)
            if not (False in a):
                messagebox.showinfo(title='Tic-Tac-Toe', message='Draw!')
                self.restart()

    def restart(self):
        for grid in self.grids:
            grid.configure(text=' ')
            grid.activated = int(self.grids.index(grid))

App().root.mainloop()
