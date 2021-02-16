from tkinter import *


root = Tk()
root.title("Temperature Converter")
root.geometry("600x500")

def convert_C():
#     # [°C] = ([°F] − 32) × 5/9
    if entry_C:
       fahrenheit= float(entry_C.get())
       celcius = (fahrenheit-32)*5/9
       result_1.insert(0, celcius)
# # Result_ C-F
result_1= Entry(root, bg="red", fg="white")
result_1.pack()
result_1.place(x=260,y=330)

def convert_F():
    # [°F] = [°C] × 9/5 + 32
    if entry_F:
       celcius = float(entry_F.get())
       fahrenheit = (celcius* 9.0 / 5)+32
       result_2.insert(0, fahrenheit)
# #Result F-C
result_2= Entry(root, bg="red", fg="white")
result_2.pack()
result_2.place(x=260,y=380)

# Celcius LabelFrame
labelframe_C = LabelFrame (root, text= "Celcius To Fahrenheit", padx= 40, pady=40)
labelframe_C.pack(fill="both")
labelframe_C.place(x=30,y=50)

# Celcius Entry
entry_C = Entry(labelframe_C, state="disable", bg="red", fg="white")
entry_C.pack()

# Fahrenheit LabelFrame
labelframe_F = LabelFrame (root, text= "Fahrenheit To Celcius ", padx= 40, pady=40)
labelframe_F.pack(fill="both")
labelframe_F.place(x=310,y=50)

# Fahrenheit Entry
entry_F= Entry(labelframe_F, state="disable", bg="red", fg="white")
entry_F.pack()


def act_1():
    entry_C.configure(state="normal")
# Celcius Button
btn_C = Button(root, text=" Activate - Celcius To Fahrentheit", command= act_1)
btn_C.pack(side= LEFT)
btn_C.place(x=30,y=250)

def act_2():
    entry_F.configure(state="normal")
 # Fahrenheit Button
btn_F = Button(root, text="Activate - Fahrenheit To Celcius", command= act_2)
btn_F.pack(side= RIGHT)
btn_F.place(x=310,y=250)

# Calculate Button 1
btn_calculate= Button(root, text="Convert Celcius-Fahrenheit", fg="white", command=convert_C, bg="black")
btn_calculate.pack()
btn_calculate.place(x=30,y=330 )

# Calculate Button 2
btn_calculate= Button(root, text="Convert Fahrenheit-Celcius", fg="white", command=convert_F, bg="black")
btn_calculate.pack()
btn_calculate.place(x=30,y=380 )

# Clear Button
def clear():
    entry_C.delete(0,END)
    entry_F.delete(0,END)
    result_1.delete(0,END)
    result_2.delete(0, END)
btn_clear= Button (root, text="Clear", fg="white",bg="black",command=clear)
btn_clear.pack(side= RIGHT)
btn_clear.place(x=480,y=420)


def ext_program():
    root.destroy()
    # Exit Button
btn_ext = Button(text="Exit Program", fg="white", command=ext_program, bg="black")
btn_ext.place(x=480,y=450)

root.mainloop()


