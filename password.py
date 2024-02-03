from tkinter import *
from random import randint


root=Tk()
root.title("Random Password Generator")
root.geometry("500x400")


my_password=chr(randint(33,126))

#generate random password
def new_rand():
    #Clear our entry box
    pw_entry.delete(0,END)

    #get PW length and convert to integer
    pw_length=int(my_entry.get())
    
    # create a variable to hold password
    my_password = ''

    
    for x in range(pw_length):
        my_password+=chr(randint(33,126))
        
    pw_entry.insert(0,my_password)


def clipper():
    root.clipboard_clear()
    #copy to clipboard
    root.clipboard_append(pw_entry.get())
    

# Label Frame
lf=LabelFrame(root, text="Enter your password length :",fg="black",bg="grey")
lf.pack(pady=40)


# Create Entry Box to Designate Number of Characters
my_entry = Entry(lf, font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)


# Create Entry Box for our Returned Password
pw_entry = Entry(lf, text=' ', font=("Helvetica",24),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)


# Create a frame for the buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create a button
my_button = Button(my_frame, text="Generate Strong Password",command=new_rand, width=25,height=2,bg="orange",fg="white")
my_button.grid(row=0,column=0,padx=10)


clip_button = Button(my_frame, text="Copy to Clipboard",command=clipper, width=25, height=2, bg="blue", fg="white")
clip_button.grid(row=0, column=1, padx=10)



label1=Label(text="Created by: Rajput Sujal")
label1.pack(padx=0, pady=20)
root.mainloop()