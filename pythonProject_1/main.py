# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tkinter

window = tkinter.Tk()
window.title('Мой калькулятор')
window.geometry('300x300')


def add():
    num1 = int(text1.get())
    num2 = int(text2.get())
    num3 = num1 + num2
    text3.delete(0, 'end')
    text3.insert(0, num3)


def sub():
    num1 = int(text1.get())
    num2 = int(text2.get())
    num3 = num1 - num2
    text3.delete(0, 'end')
    text3.insert(0, num3)


button1 = tkinter.Button(window, text='+', command=add)
button1.place(x=95, y=110)
button2 = tkinter.Button(window, text='-', command=sub)
button2.place(x=160, y=110)

text1 = tkinter.Entry(window, width=10)
text1.place(x=95, y=40)
text2 = tkinter.Entry(window, width=20)
text2.place(x=95, y=81)
text3 = tkinter.Entry(window, width=20)
text3.place(x=95, y=221)