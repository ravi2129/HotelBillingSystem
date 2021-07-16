from subprocess import call
from tkinter import *
from tkinter import messagebox


def onClick(arg):
    print("Welcome")

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin's Login")
        self.root.geometry("1000x1000")

        self.root.resizable(False,False)

        # Adjust size




        Frame_login = Frame(self.root)
        Frame_login.place(x=150, y=150, height=350, width=500)

        title = Label(Frame_login, text="Login Here", font = ("Montserrat", 35, "bold"), fg="#d77337", bg="white").place(x=90, y=30)
        desc=Label(Frame_login, text="Admin's Login Page", font=("Montserrat", 15, "bold"), fg="#d25d17", bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_login, text="Username", font=("Montserrat", 15, ), fg="black", bg="white").place(x=90,y=140)

        self.txt_user=Entry(Frame_login, font=("times new roman",15, ), bg="light grey")

        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Montserrat", 15, ), fg="black",
                         bg="white").place(x=90, y=210)

        self.txt_pass = Entry(Frame_login, font=("Gpudy old style", 15), bg="light grey")

        self.txt_pass.place(x=90, y=240, width=350, height=35)




        Login_btn = Button(self.root,command=self.login_function, cursor="hand2" ,text="Login", bg="#d77337", fg="white", font=("Montserrat",20, "bold")).place(x=300,y=470, width=180, height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get()!="1234" or self.txt_user.get()!= "Admin":
            messagebox.showerror("Error","Invalid Username/Password", parent=self.root)
        else:
                call(["python", "Main_page.py"])



root = Tk()
root.geometry("1000x1000")

# Add image file
bg = PhotoImage(file="bg2.png")

# Create Canvas
canvas1 = Canvas(root, width=1920, height=1080)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")
obj = Login (root)
root.mainloop()