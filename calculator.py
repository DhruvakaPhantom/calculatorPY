
from tkinter import *


calc = Tk()
calc.geometry("395x450")
calc.title("CALCULATOR")
calc.configure(bg='black')

enter = Entry(calc, width = 27, font=('Arial 18'), justify = "right")
enter.place(x= 20, y = 20)

def myclick(self):
	current = enter.get()
	enter.delete(0, END) 
	enter.insert(0, str(current) + str(self))

def b_add():
	first_number = enter.get()
	global first_num
	global math
	math = "add"
	first_num = int(first_number)
	enter.delete(0, END)

def b_subt():
	first_number = enter.get()
	global first_num
	global math
	math = "subt"
	first_num = int(first_number)
	enter.delete(0, END)

def b_mul():
	first_number = enter.get()
	global first_num
	global math
	math = "mul"
	first_num = int(first_number)
	enter.delete(0, END)

def b_div():	
	first_number = enter.get()
	global first_num
	global math
	math = "div"
	first_num = int(first_number)
	enter.delete(0, END)


def b_equal():
	second_number = enter.get()
	enter.delete(0, END)
	
	if math == "add":
		enter.insert(0, first_num + int(second_number)) 
	if math == "subt":
		enter.insert(0, first_num - int(second_number))
	if math == "mul":
		enter.insert(0, first_num * int(second_number))
	if math == "div":
		enter.insert(0, first_num / int(second_number))

def b_clear():
	enter.delete(0, END)
	
class buttons:
	
	def button1(self):
		button1=Button(calc, text= "1" ,padx = 35, pady = 30, command =lambda:myclick("1"), font= ("Arial 10 bold"))
		button1.place(x=20, y=250)
		
		
	def button2(self):
		button2=Button(calc, text = "2" ,padx = 35, pady = 30, command =lambda:myclick("2"), font= ("Arial 10 bold"))
		button2.place(x=110, y=250)
		

	def button3(self):
		button3=Button(calc, text = "3" ,padx = 35, pady = 30, command =lambda:myclick("3"), font= ("Arial 10 bold"))
		button3.place(x=200, y=250)
		

	def button4(self):
		button4=Button(calc, text = "4" ,padx = 35, pady = 30, command =lambda:myclick("4"), font= ("Arial 10 bold"))
		button4.place(x=20, y=160)
		

	def button5(self):
		button5=Button(calc, text = "5" ,padx = 35, pady = 30, command =lambda:myclick("5"), font= ("Arial 10 bold"))
		button5.place(x=110, y=160)
		

	def button6(self):
		button6=Button(calc, text = "6" ,padx = 35, pady = 30, command =lambda:myclick("6"), font= ("Arial 10 bold"))
		button6.place(x=200, y=160)
		

	def button7(self):
		button7=Button(calc, text = "7" ,padx = 35, pady = 30, command =lambda:myclick("7"), font= ("Arial 10 bold"))
		button7.place(x=20, y=70)
		

	def button8(self):
		button8=Button(calc, text = "8" ,padx = 35, pady = 30, command =lambda:myclick("8"), font= ("Arial 10 bold"))
		button8.place(x=110, y=70)
		

	def button9(self):
		button9=Button(calc, text = "9" ,padx = 35, pady = 30, command =lambda:myclick("9"), font= ("Arial 10 bold"))
		button9.place(x=200, y=70)
		

	def button0(self):
		button0=Button(calc, text = "0" ,padx = 35, pady = 30, command =lambda:myclick("0"), font= ("Arial 10 bold"))
		button0.place(x=110, y=340)
		

	def button_clear(self):
		button_clear=Button(calc, text = "clear" ,padx = 22, pady = 30, command =b_clear, font= ("Arial 10 bold"))
		button_clear.place(x=20, y=340)

	def button_add(self):
		button_add=Button(calc, text = "+" ,padx = 34, pady = 30,command =b_add, font= ("Arial 10 bold"))
		button_add.place(x=290, y=70)

	def button_subt(self):
		button_subt=Button(calc, text = "-" ,padx = 34, pady = 27,command =b_subt, font= ("Arial 12 bold"))
		button_subt.place(x=290, y=160)

	def button_mul(self):
		button_mul=Button(calc, text = "*" ,padx = 35, pady = 30,command =b_mul, font= ("Arial 10 bold"))
		button_mul.place(x=290, y=340)

	def button_div(self):
		button_div=Button(calc, text = "/" ,padx = 36, pady = 30,command =b_div, font= ("Arial 10 bold"))
		button_div.place(x=290, y=250)

	def button_equal(self):
		button_equal=Button(calc, text = "=" ,padx = 34, pady = 30,command =b_equal, font= ("Arial 10 bold"))
		button_equal.place(x=200, y=340)

buttons().button0()
buttons().button1()
buttons().button2()
buttons().button3()
buttons().button4()
buttons().button5()
buttons().button6()
buttons().button7()
buttons().button8()
buttons().button9()
buttons().button_add()
buttons().button_subt()
buttons().button_mul()
buttons().button_div()
buttons().button_clear()
buttons().button_equal()
	
calc.mainloop()