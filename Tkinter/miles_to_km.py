from tkinter import *
root = Tk()
root.title('My Mile to KIlometre Convertor.')
root.config(padx=15, pady=15)

def mileToKm():
    miles = float(mile_entry.get())
    km = round(miles * 1.609)
    km_result_label.config(text=str(km))

mile_entry = Entry(width=5)
mile_entry.grid(row=0, column=1)
mile_entry_label = Label(text='Miles')
mile_entry_label.grid(row=0, column=2)
is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1, column=0)
km_entry_label = Label(text='Km')
km_entry_label.grid(row=1, column=2)
km_result_label = Label(text='0')
km_result_label.grid(row=1, column=1)
button_entry = Button(text='calculate', command=mileToKm)
button_entry.grid(column=1, row=2)

root.mainloop()