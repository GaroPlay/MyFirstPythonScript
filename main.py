import tkinter

# Флаг переключения ввода числа или оператора.
Start = True
# Последний выбранный оператор пользователем.
LastCommand = "="
Result = 0

def ButtonClick(ButtonText):
    global Start
    global LastCommand
    global DisplayResult
    global Result

    if ButtonText == "C":
        Start = True
        Result = 0
        LastCommand = "="
        DisplayResult.configure(text=str(int(Result)))
        return

    if ButtonText.isdigit() or ButtonText=='.':
        if Start:
            DisplayResult.configure(text="")
            Start=False

        CurrentDisplayText = DisplayResult.cget("text")
        NumberCountForDisplay = 0

        for DisplaySymbol in CurrentDisplayText:
            if DisplaySymbol.isdigit():
                NumberCountForDisplay += 1

        if NumberCountForDisplay < 12 and (ButtonText != '.' or CurrentDisplayText.find('.') == -1):
            DisplayResult.configure(text=(DisplayResult.cget("text")+ButtonText))
    else:
        if Start:
            LastCommand=ButtonText
        else:
            CalculateNumber(float(DisplayResult.cget("text")))
            LastCommand = ButtonText
            Start = True

def CalculateNumber(x):
    global Result
    global LastCommand
    global DisplayResult

    if LastCommand == "+":
        Result = Result + x
    elif LastCommand == "-":
        Result = Result - x
    elif LastCommand == "*":
        Result = Result * x
    elif LastCommand == "/":
        try:
            Result = Result / x
        except ZeroDivisionError:
            pass
    elif LastCommand == "=":
        Result=x

    if Result == int(Result):
        DisplayResult.configure(text=str(int(Result)))
    else:
       DisplayResult.configure(text=str(round(Result,12)))


# Визуальный эффект наведения на кнопку.
def ButtonHoverEnter(ButtonEvent):
    ButtonEvent.widget.config(bg="lightsteelblue", fg="white")

# Визуальный эффект покидания кнопки.
def ButtonHoverLeave(ButtonEvent):
    ButtonEvent.widget.config(bg="slategray", fg="whitesmoke")

WindowsProgramRoot = tkinter.Tk()
WindowsProgramRoot.title("Калькулятор")
WindowsProgramRoot.configure(bg="midnightblue")

# Кортеж кортежей со значениями для конфигурационной опции text у кнопок.
TupleButtons = (("7","8","9","/"),
                ("4","5","6","*"),
                ("1","2","3","-"),
                ("0",".","=","+"))

DisplayResult = tkinter.Label(WindowsProgramRoot,text="0",font=("Times New Roman", 32, "bold"),bg="darkslategray",
                              fg="whitesmoke",bd=15, relief="sunken",padx=20,pady=10, anchor="e")
DisplayResult.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

ButtonClear = tkinter.Button(WindowsProgramRoot, text="Clear", font="Tahoma 20 bold",
                             bg="tomato", fg="white",activebackground="red", activeforeground="white",
                             bd=4, relief="raised",command=lambda: ButtonClick("C"))
ButtonClear.grid(row=1, column=0, columnspan=4, padx=5, pady=5, ipadx=20, ipady=15, sticky="nsew")


for row in range(4):
    for column in range(4):
        button = tkinter.Button(WindowsProgramRoot,text=TupleButtons[row][column],font="Tahoma 20",bg="slategray",
                                fg="whitesmoke",activebackground = "steelblue",activeforeground="white",
                                bd=4,relief="raised",command=lambda text = TupleButtons[row][column]:ButtonClick(text))
        button.grid(row=row+2,column=column,padx=5,pady=5,ipadx=20,ipady=20,sticky="nsew")
        button.bind("<Enter>", ButtonHoverEnter)
        button.bind("<Leave>", ButtonHoverLeave)

for i in range(6):
    WindowsProgramRoot.grid_rowconfigure(i, weight=1)
    if i < 4:
        WindowsProgramRoot.grid_columnconfigure(i, weight=1)

WindowsProgramRoot.update_idletasks()

# Получили ширину и высоту окна программы которое способно вместить в себя все дочерние виджеты.
CalculatorWidthForWidget = WindowsProgramRoot.winfo_reqwidth()
CalculatorHeightForWidget = WindowsProgramRoot.winfo_reqheight()

WindowsProgramRoot.minsize(CalculatorWidthForWidget, CalculatorHeightForWidget)
WindowsProgramRoot.maxsize(600, 700)

# Получили ширину и высоту экрана пользователя.
UserMonitorWidth = WindowsProgramRoot.winfo_screenwidth()
UserMonitorHeight = WindowsProgramRoot.winfo_screenheight()

# Получи точку для размещения калькулятора по центру экрана пользователя.
WindowsProgramRootLeftAngleWidth = int(UserMonitorWidth/2 - CalculatorWidthForWidget/2)
WindowsProgramRootLeftAngleHeight = int(UserMonitorHeight/2 - CalculatorHeightForWidget/2)

# Задали позицию верхнего левого угла для окна калькулятора.
WindowsProgramRoot.geometry(f"+{WindowsProgramRootLeftAngleWidth}+{WindowsProgramRootLeftAngleHeight}")

WindowsProgramRoot.mainloop()