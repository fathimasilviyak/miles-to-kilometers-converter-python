from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)
answer_label = Label(text="0")
answer_label.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def mile_to_km():
    mile_value = float(miles_input.get())
    km = round(1.609 * mile_value)
    answer_label.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
