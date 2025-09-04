import customtkinter as ctk
class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300+500+100")
        self.title("Калькулятор")
        #self._set_appearance_mode("light")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)

        self.strr = ctk.StringVar()
        self.strr.set("")
        self.string = ctk.CTkEntry(self, width=360,textvariable=self.strr, border_color="white")
        self.string.grid(pady=(10,0), padx=10, sticky="nsew")

        self.buttons_frame = Buttons_frame(master = self)
        self.buttons_frame.grid(row=1, column=0,padx=10, pady=10, sticky="nsew")


    def AddSimbol(self, val):
        self.strr.set(self.strr.get() + str(val))

    def AC(self):
        self.strr.set("")
    
    def delete_last(self):
        now_string = self.string.get()
        self.string.delete(len(now_string)-1, ctk.END)

    def equal(self, strin):
        #print(f"Строка1 {strin}")
        calcul = Calculate(strin, self.strr)
        calcul.calc()



class Buttons_frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="white", width=360, height = 230)

        self.buttonAC = ctk.CTkButton(self, text="AC", width=160, command=lambda:master.AC())
        self.buttonAC.grid(row=0, column=0,columnspan=2, pady=10, padx=10)

        self.buttonDelete = ctk.CTkButton(self, text="⌦", width=70, command=lambda:master.delete_last())
        self.buttonDelete.grid(row=0, column=2, pady=10, padx=10)
        
        self.button9 = ctk.CTkButton(self, text="9", width=70, command=lambda:master.AddSimbol(9))
        self.button9.grid(row=1, column=2, pady=10, padx=10)

        self.button8 = ctk.CTkButton(self, text="8", width=70, command=lambda:master.AddSimbol(8))
        self.button8.grid(row=1, column=1, pady=10, padx=10)

        self.button7 = ctk.CTkButton(self, text="7", width=70, command=lambda:master.AddSimbol(7))
        self.button7.grid(row=1, column=0, pady=10, padx=10)

        self.button6 = ctk.CTkButton(self, text="6", width=70, command=lambda:master.AddSimbol(6))
        self.button6.grid(row=2, column=2, pady=10, padx=10)

        self.button5 = ctk.CTkButton(self, text="5", width=70, command=lambda:master.AddSimbol(5))
        self.button5.grid(row=2, column=1, pady=10, padx=10)

        self.button4 = ctk.CTkButton(self, text="4", width=70, command=lambda:master.AddSimbol(4))
        self.button4.grid(row=2, column=0, pady=10, padx=10)

        self.button3 = ctk.CTkButton(self, text="3", width=70, command=lambda:master.AddSimbol(3))
        self.button3.grid(row=3, column=2, pady=10, padx=10)

        self.button2 = ctk.CTkButton(self, text="2", width=70, command=lambda:master.AddSimbol(2))
        self.button2.grid(row=3, column=1, pady=10, padx=10)

        self.button1 = ctk.CTkButton(self, text="1", width=70, command=lambda:master.AddSimbol(1))
        self.button1.grid(row=3, column=0, pady=10, padx=10)

        self.button0 = ctk.CTkButton(self, text="0", width=70, command=lambda:master.AddSimbol(0))
        self.button0.grid(row=4, column=1, pady=10, padx=10)

        # self.buttonTen = ctk.CTkButton(self, text=",", width=70, command=lambda:master.AddSimbol(","))
        # self.buttonTen.grid(row=4, column=0, pady=10, padx=10)
        #fghgfhfghfg
        self.buttonCut = ctk.CTkButton(self, text="÷", width=70, command=lambda:master.AddSimbol("÷"))
        self.buttonCut.grid(row=0, column=3, pady=10, padx=10)

        self.buttonX = ctk.CTkButton(self, text="×", width=70, command=lambda:master.AddSimbol("×"))
        self.buttonX.grid(row=1, column=3, pady=10, padx=10)

        self.buttonMinus = ctk.CTkButton(self, text="-", width=70, command=lambda:master.AddSimbol("-"))
        self.buttonMinus.grid(row=2, column=3, pady=10, padx=10)

        self.buttonPlus = ctk.CTkButton(self, text="+", width=70, command=lambda:master.AddSimbol("+"))
        self.buttonPlus.grid(row=3, column=3, pady=10, padx=10)

        self.buttonEqual = ctk.CTkButton(self, text="=", width=160, command=lambda:master.equal(master.string.get()))
        self.buttonEqual.grid(row=4, column=2,columnspan=2, pady=10, padx=10)
        
        # self.buttonAbout = ctk.CTkButton(self, text="sh", width=70)
        # self.buttonAbout.grid(row=4, column=0, pady=10, padx=10)
        


class Calculate:
    def __init__(self, strin, entry):
        self.string = strin
        self.entry = entry
        #print(f"Строка2 {strin}")
    def calc(self):
        #print(f"Строка3 {self.string}")
        lst = []
        num = ""
        for i in self.string:
            to_normal = {
                "×":"*",
                "÷":'/',
                "+":"+",
                "-":"-"
            }
            if i.isdigit() or i == '.':
                num += i
            else:
                if num:
                    lst.append(num)
                    num = ""
                lst.append(to_normal[i])
        if num:
            lst.append(num)
        self.to_OPZ(lst)

    def is_number(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def to_OPZ(self, lst):
        win = {
            "+":1,
            "-":1,
            "*":2,
            "/":2
        }
        output = []
        operators = []

        for s in lst:
            if self.is_number(s):
                output.append(s)
            else:
                while operators and win[operators[-1]] >= win[s]:
                    output.append(operators.pop())
                operators.append(s)
        while operators:
            output.append(operators.pop())

        self.calcula(output)




    def calcula(self, opz):
        stak = []
        for num in opz:
            try:
                stak.append(float(num))
            except ValueError:
                a = stak.pop()
                b = stak.pop()
                try:
                    c = eval(f'{b}{num}{a}')
                except ZeroDivisionError:
                    self.entry.set("Нельзя делить на 0")
                    return
                stak.append(c)
    
        self.entry.set(stak[0])
    


ctk.set_appearance_mode("light")
app = Window()
app.mainloop()