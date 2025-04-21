import tkinter as tk

my_window = tk.Tk()
my_window.title("BMI Calculator")
my_window.minsize(500, 500)

height_input = tk.IntVar()
weight_input = tk.IntVar()


height_label = tk.Label(my_window, text="Enter your Height (cm)")
height_label.place(x=200, y=50)

height_entry = tk.Entry(my_window, textvariable=height_input)
height_entry.place(x=180, y=75)

weight_label = tk.Label(my_window, text="Enter your Weight (kg)")
weight_label.place(x=200, y=100)

weight_entry = tk.Entry(my_window, textvariable=weight_input)
weight_entry.place(x=180, y=125)

result_label = tk.Label(my_window)
result_label.place(x=160, y=160)

def calculate():

  height_calc = height_input.get() / 100
  result = (weight_input.get() / (height_calc * height_calc))
  if result <= 18.4:
      result_label.configure(text="Your BMI is: "+ str(result) +  " Underweight")
  elif (result >= 18.5) and (result <= 24.9):
      result_label.configure(text="Your BMI is: "+ str(result) +  " Normal")
  elif (result >= 25.0) and (result <= 39.9):
      result_label.configure(text="Your BMI is: " + str(result) + " Overweight")
  else:
      result_label.configure(text="Your BMI is: " + str(result) + " Obese")



calculator_button = tk.Button(my_window, text="Calculate",command=calculate)
calculator_button.place(x=225, y=200)




my_window.mainloop()

