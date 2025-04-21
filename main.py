import tkinter as tk

my_window = tk.Tk()
my_window.title("BMI Calculator")
my_window.config(padx=50, pady=50)

height_input = tk.IntVar()
weight_input = tk.IntVar()


height_label = tk.Label(my_window, text="Enter your Height (cm)")
height_label.pack()

height_entry = tk.Entry(my_window, textvariable=height_input)
height_entry.pack()

weight_label = tk.Label(my_window, text="Enter your Weight (kg)")
weight_label.pack()

weight_entry = tk.Entry(my_window, textvariable=weight_input)
weight_entry.pack()

result_label = tk.Label(my_window)
result_label.pack()

def calculate():

  height_calc = height_input.get() / 100
  result = weight_input.get() / height_calc ** 2
  if height_input.get() == 0 or weight_input.get() == 0:
      result_label.config(text="Enter both weight and height")
  elif result <= 18.4:
      result_label.configure(text="Your BMI is: "+ str(result) +  " Underweight")
  elif (result >= 18.5) and (result <= 24.9):
      result_label.configure(text="Your BMI is: "+ str(result) +  " Normal")
  elif (result >= 25.0) and (result <= 39.9):
      result_label.configure(text="Your BMI is: " + str(result) + " Overweight")
  else:
      result_label.configure(text="Your BMI is: " + str(result) + " Obese")



calculator_button = tk.Button(my_window, text="Calculate",command=calculate)
calculator_button.pack()




my_window.mainloop()

