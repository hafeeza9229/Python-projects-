from tkinter import *


def equals():
    global equation_text
    total = str(eval(equation_text))
    equation_label.set(total)


def button_press(digit):
    global equation_text

    equation_text = equation_text + str(digit)
    equation_label.set(equation_text)
    # except ZeroDivisionError:
    #     clear()
    #     equation_label.set("Error")
    #     equation_text = ""


def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)


window = Tk()
window.geometry("289x419")
window.resizable(False, False)
window.title("CALCULATOR")
window.config(bg="black")
# window.config(bg="#707070")

equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=("verdana", 20, "bold"),
              bg="black", fg="white", width=18, height=2)
label.grid(row=0, column=0, columnspan=30, pady=(18, 14), sticky="w")

button7 = Button(window, text=7, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(7))
button7.grid(row=1, column=0)
button8 = Button(window, text=8, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(8))
button8.grid(row=1, column=1)
button9 = Button(window, text=9, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(9))
button9.grid(row=1, column=2)
button_clear = Button(window, text="C", width=5, height=2, font=("Verdana", 14), bg="#f52314", fg="white",
                      command=lambda: clear())
button_clear.grid(row=1, column=3)

button4 = Button(window, text=4, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(4))
button4.grid(row=2, column=0)
button5 = Button(window, text=5, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(5))
button5.grid(row=2, column=1)
button6 = Button(window, text=6, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(6))
button6.grid(row=2, column=2)
button_minus = Button(window, text="-", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                      command=lambda: button_press("-"))
button_minus.grid(row=2, column=3)

button3 = Button(window, text=3, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(3))
button3.grid(row=3, column=0)
button2 = Button(window, text=2, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(2))
button2.grid(row=3, column=1)
button1 = Button(window, text=1, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(1))
button1.grid(row=3, column=2)
button_mul = Button(window, text="*", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                    command=lambda: button_press("*"))
button_mul.grid(row=3, column=3)

button_dec = Button(window, text=".", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                    command=lambda: button_press("."))
button_dec.grid(row=4, column=0)
button0 = Button(window, text=0, width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                 command=lambda: button_press(0))
button0.grid(row=4, column=1)
button_add = Button(window, text="+", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                    command=lambda: button_press("+"))
button_add.grid(row=4, column=2)
button_div = Button(window, text="/", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                    command=lambda: button_press("/"))
button_div.grid(row=4, column=3)

button_open = Button(window, text="(", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                     command=lambda: button_press("("))
button_open.grid(row=5, column=0)
button_close = Button(window, text=")", width=5, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                      command=lambda: button_press(")"))
button_close.grid(row=5, column=1)
button_equal = Button(window, text="=", width=11, height=2, font=("Verdana", 14), bg="#008080", fg="black",
                      command=lambda: equals())
button_equal.grid(row=5, column=2, columnspan=2)



window.mainloop()



