from cProfile import label
from tkinter import *
import tkinter
from turtle import bgcolor
window = Tk() 
import telebot;
bot = telebot.TeleBot('%5141577925:AAHm3xgeDbIEyL6QKBKQNyRJSq9OdG8bnVI%');
import client


#функции отправки в консоль   nnnnn
def print_in_CMD_1():
    print('Command for eat')

def print_in_CMD_2():
    print('Command for voice speaker')

#Задаю иконку, цвет, название окна
window.title('example')
window.configure(bg='#FFFFFF')

#Задаю размеры окна и возможность разширения по ширине но не по высоте
window.geometry("316x480+600+50")
window.minsize(316, 477)
window.maxsize(316, 477)
window.resizable(True, False)

#Лейбл первый
label1 = Label(text="Automativ cat live \nSupport: SupCat@mail.ru ", fg="#eee", bg="#333", justify=LEFT, width="22", anchor="sw")
label1.grid(row=0,column=0)
label2 = Label(text=" \n " , fg="#eee", bg="#333", justify=LEFT, width="22", anchor="sw")
label2.grid(row=0,column=1)

#Лейбл второй
poetry_1 = "This application for the comfortable life of your cat"
label3 = Label(text=poetry_1, justify=CENTER, width="22", anchor="sw")
label3.grid(stick='we', row=1,column=0, columnspan=2)

#Кнопки
btn1 = Button(window, text="Feed the cat", width="20", height="2", command=print_in_CMD_1)
btn2 = Button(window, text="Send voice message", width="20", height="2", command=print_in_CMD_2)

btn1.grid(row=3,column=0, stick='we')
btn2.grid(row=3,column=1, stick='we')

#Лейбл со статусом девайсов
poetry_2 = "Label for device status informathion"
label4 = Label(text=poetry_2, justify=CENTER, width="22", height="15", anchor="sw", bg="white")
label4.grid(stick='we', row=4, column=0, columnspan=2)

poetry_3 = "Label for device status informathion"
label4 = Label(text=poetry_3, justify=CENTER, width="22", height="4", anchor="sw", fg="#eee", bg="#333")
label4.grid(stick='we', row=5, column=0, columnspan=2)

#Кнопки нижние
btn3 = Button(window, text="Start Game", width="20", height="2", command=print_in_CMD_1)
btn4 = Button(window, text="Stop Game", width="20", height="2", command=print_in_CMD_2)
btn5 = Button(window, text="Pause Game", width="20", height="2", command=print_in_CMD_1)
btn6 = Button(window, text="Change Game", width="20", height="2", command=print_in_CMD_2)


btn3.grid(row=6,column=0, stick='we')
btn4.grid(row=6,column=1, stick='we')
btn5.grid(row=7,column=0, stick='we')
btn6.grid(row=7,column=1, stick='we')

window.mainloop()