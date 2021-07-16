from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')


# heading
heading_label = Label(root,text="---------  DEVELOPERS  ---------",font=('Orbitron',15),bg="black",fg="white")
heading_label.pack(fill=X)


# NAME LABELS
m_label=Label(root,text="Raviraj Dange",font=('Orbitron',20))
l_label=Label(root,text="Akshay Jadhav",font=('Orbitron',20))
r_label=Label(root,text="Suprit Giri",font=('Orbitron',20))

m_label.place(relx=0.30,rely=0.165)
l_label.place(relx=0.50,rely=0.165)
r_label.place(relx=0.70,rely=0.165)

root.mainloop()