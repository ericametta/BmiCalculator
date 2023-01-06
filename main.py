import tkinter

#create function

def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"
    # print(round(bmi, 2))

"""DISPLAY LABELS"""
root = tkinter.Tk()  # the overall box
root.title("BMI calculator")  # the top title

label_kg = tkinter.Label(root, text = "KG: ") #label
label_kg.grid(column=0, row=0) #pack is a geometry manager that manages the placement of the elements
# input kg
entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row=0)

label_height = tkinter.Label(root, text = "HEIGHT: ") #label
label_height.grid(column=0, row=1) #pack is a geometry manager that manages the placement of the elements
# input height
entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text = "Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2)

label_result = tkinter.Label(root, text = "BMI: ") #label
label_result.grid(column=1, row=2) #pack is a geometry manager that manages the placement of the elements

"""INPUT"""

root.mainloop()