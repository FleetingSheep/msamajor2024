import tkinter as tk
import turtle as trtl
import numpy as np
board = None
def highlight(x, y):
    global board
    print(f"X: {x}")
    print(f"Y: {y}")
    x += 400
    y -= 400
    y *= -1
    print(f"Coordinate X: {int(x / 100)}")
    print(f"Coordinate Y: {int(y / 100)}")
    print(board[(int(y / 100)), (int(x / 100))])


def place(board, side):
    counter = 0
    if side == "white": #top side
        x = 0
        y = 3
        for i in range(4):
            board[x, counter] = y
            board[x + 2, counter] = y
            counter += 1
            board[x + 1, counter] = y
            counter += 1
    else: #bottom side
        x = -3
        y = 4
        for i in range(4):  
            board[x + 1, counter] = y
            counter += 1
            board[x, counter] = y
            board[x + 2, counter] = y
            counter += 1
def main():
    global board
    wn = trtl.Screen()
    wn.setup(width=800, height=800)
    wn.title("Project")
    wn._root.resizable(False, False)
    wn.screensize(400, 400)
    wn.tracer(False)

    board = np.zeros((8, 8))
    place(board, "white")
    place(board, "black")
    print(board)

    exist = True
    increment = wn.window_width() / 8
    for ycounter, i in enumerate(board):
        for counter, i in enumerate(board):
            turtle = trtl.Turtle()
            turtle.color("dark gray")
            turtle.penup()
            turtle.goto(((counter * increment) - 350), 350 - (ycounter * increment))
            counter += 1
            turtle.shape("square")
            turtle.shapesize(4.6, 4.6)
            if ycounter % 2 == 1:
                if counter % 2 == 0:
                    turtle.color("light gray")
            else:
                if counter % 2 == 1:
                    turtle.color("light gray")

            turtle.stamp()
            turtle.shape("circle")
            turtle.shapesize(2.5, 2.5)
            if ycounter > 4:
                turtle.color("black")
            elif ycounter < 3:
                turtle.color("white")
            
            if exist == False:
                turtle.ht()

            if exist == True: #alternate pieces for checker-board pattern
                exist = False
                
            else:
                exist = True

        ycounter += 1
        if exist == True: #alternate pieces for checker-board pattern
            exist = False
        else:
            exist = True

    wn.onscreenclick(highlight)
    wn.tracer(True)
    wn.listen()
    wn.mainloop()


main()