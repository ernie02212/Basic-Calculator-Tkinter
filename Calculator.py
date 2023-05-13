import tkinter as tk

root = tk.Tk()
root.title("Calculator")

data = tk.Entry(root, width=40,  borderwidth= 10)
data.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10)

#Display number
def clicked_button(num):
    first_num = data.get()
    data.delete(0,"end")
    data.insert(0,str(first_num) + str(num))

#Clear all number
def clear_button():
    data.delete(0,"end")

# Addition
def add_button():
    first_num = data.get()
    global num_one
    global sign
    sign = "add"
    num_one = int(first_num)
    data.delete(0,"end")
    return

#Subtraction
def subtract_button():
    first_num = data.get()
    global num_one
    global sign
    sign = "subtract"
    num_one = int(first_num)
    data.delete(0,"end")
    return

def divide_button():
    first_num = data.get()
    global num_one
    global sign
    sign = "divide"
    num_one = int(first_num)
    data.delete(0,"end")
    return

def multiply_button():
    first_num = data.get()
    global num_one
    global sign
    sign = "multiply"
    num_one = int(first_num)
    data.delete(0,"end")
    return

#Solve Equation
def equal_button():
    second_num = data.get()
    num_two = int(second_num)
    data.delete(0,"end")
    if sign == "add":
        data.insert(0, num_one + num_two)
    elif sign == "subtract":
        data.insert(0,num_one - num_two)
    elif sign == "divide":
        data.insert(0,num_one / num_two)
    elif sign == "multiply":
        data.insert(0,num_one * num_two)

# Defining the Buttons
myButton1 = tk.Button(root, text = "1", padx = 30, pady = 20,command = lambda: clicked_button(1))
myButton2 = tk.Button(root, text = "2", padx = 30, pady = 20,command = lambda: clicked_button(2))
myButton3 = tk.Button(root, text = "3", padx = 30, pady = 20,command = lambda: clicked_button(3))

myButton4 = tk.Button(root, text = "4", padx = 30, pady = 20,command = lambda: clicked_button(4))
myButton5 = tk.Button(root, text = "5", padx = 30, pady = 20,command = lambda: clicked_button(5))
myButton6 = tk.Button(root, text = "6", padx = 30, pady = 20,command = lambda: clicked_button(6))

myButton7 = tk.Button(root, text = "7", padx = 30, pady = 20,command = lambda: clicked_button(7))
myButton8 = tk.Button(root, text = "8", padx = 30, pady = 20,command = lambda: clicked_button(8))
myButton9 = tk.Button(root, text = "9", padx = 30, pady = 20,command = lambda: clicked_button(9))

myButton0 = tk.Button(root, text = "0", padx = 30, pady = 20,command = lambda: clicked_button(0))

# Plotting the buttons
myButton1.grid(row = 1, column  = 0)
myButton2.grid(row = 1, column  = 1)
myButton3.grid(row = 1, column  = 2)

myButton4.grid(row = 2, column  = 0)
myButton5.grid(row = 2, column  = 1)
myButton6.grid(row = 2, column  = 2)

myButton7.grid(row = 3, column  = 0)
myButton8.grid(row = 3, column  = 1)
myButton9.grid(row = 3, column  = 2)

myButton0.grid(row = 4, column  = 0)

#Defining the mathematic signs
myButton_add = tk.Button(root, text = "+",padx = 40, pady = 20, command =  add_button)
myButton_equal = tk.Button(root, text = "=",padx = 89, pady = 20, command = equal_button)
myButton_subtract = tk.Button(root, text = "-",padx = 40, pady = 20, command = subtract_button)
myButton_clear = tk.Button(root, text = "Clear",padx = 200, pady = 20, command = clear_button)
myButton_multiply = tk.Button(root, text = "/",padx = 40, pady = 20, command = divide_button)
myButton_divide = tk.Button(root, text = "*",padx = 40, pady = 20, command = multiply_button)

#Plotting the mathematic signs
myButton_add.grid(row = 1, column  = 3)
myButton_subtract.grid(row = 2, column  = 3)
myButton_equal.grid(row = 4, column  = 2, columnspan= 2 )
myButton_clear.grid(row = 5, column  = 0, columnspan= 4)
myButton_divide.grid(row = 4, column = 1 )
myButton_multiply.grid(row = 3, column = 3)

#Run the GUI
root.mainloop()



