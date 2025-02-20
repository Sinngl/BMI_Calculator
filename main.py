import tkinter

window = tkinter.Tk()
window.minsize(250,250)
window.config(background="light gray")
window.title("BMI Calculator")
window.config(padx=30, pady=30)


def bmi_calculator():
    try:
        height = float(height_input.get())
        weight = float(weight_input.get())

        if weight == "" or height == "":
            result_label.config(text="Please, enter positive numbers!")
            return

        bmi_result = weight / ((height / 100) ** 2)

        if bmi_result <= 18.4:
            result_label.config(text=f"Your BMI is {round(bmi_result, 2)}. You are Underweight")
        elif 18.4 < bmi_result < 25:
            result_label.config(text=f"Your BMI is {round(bmi_result, 2)}. You are Normal")
        elif 25 <= bmi_result < 40:
            result_label.config(text=f"Your BMI is {round(bmi_result, 2)}. You are High Weight")
        else:
            result_label.config(text=f"Your BMI is {round(bmi_result, 2)}. You are Obese")

    except ValueError:
        result_label.config(text="Please, enter a valid number!")


weight_label = tkinter.Label(text="Enter your Weight (kg)")
weight_label.pack()
weight_label.config(background="light gray", foreground="black")

weight_input = tkinter.Entry(width=10, background="white", foreground="black", highlightthickness=0)
weight_input.pack()

height_label = tkinter.Label(text="Enter your Height (cm)", background="light gray", foreground="black")
height_label.pack()

height_input = tkinter.Entry(width=10, background="white", foreground="black", highlightthickness=0)
height_input.pack()

result_button = tkinter.Button(text="Calculate", command=bmi_calculator, highlightthickness=0)
result_button.pack(padx=10, pady=10)

result_label = tkinter.Label(background="light gray", foreground="black")
result_label.pack()

window.mainloop()
