# Python program to create a simple GUI  calculator using Tkinter
from tkinter import *

expression = ""


# Function to update expression
# in the text entry box
def press(num):

    global expression
    expression = expression + str(num)
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():

    try:

        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    gui = Tk()
    # set the background colour of GUI window
    gui.configure(background="black")
    gui.title("Simple Calculator")
    gui.geometry("320x250")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=5, ipadx=100)

    button1 = Button(gui, text=' 1 ', fg='black', bg='grey',
                     command=lambda: press(1), height=2, width=10)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='grey',
                     command=lambda: press(2), height=2, width=10)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='grey',
                     command=lambda: press(3), height=2, width=10)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='grey',
                     command=lambda: press(4), height=2, width=10)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='grey',
                     command=lambda: press(5), height=2, width=10)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='grey',
                     command=lambda: press(6), height=2, width=10)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='grey',
                     command=lambda: press(7), height=2, width=10)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='grey',
                     command=lambda: press(8), height=2, width=10)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='grey',
                     command=lambda: press(9), height=2, width=10)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='grey',
                     command=lambda: press(0), height=2, width=10)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='grey',
                            command=lambda: press("+"), height=2, width=10)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='grey',
                   command=lambda: press("-"), height=2, width=10)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='grey',
                      command=lambda: press("*"), height=2, width=10)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='grey',
                    command=lambda: press("/"), height=2, width=10)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='grey',
                   command=equalpress, height=2, width=10)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='grey',
                   command=clear, height=2, width=10)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='grey',
                     command=lambda: press('.'), height=2, width=10)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
