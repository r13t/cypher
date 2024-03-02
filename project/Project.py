from tkinter import *   #GUI Library
from tkinter import messagebox    #Type of GUI 
import base64    #Encryption/Decryption Library

#################################################################################
#################################################################################
def decrypt(): # Decryption Design & Function & Password Condition
    password=code.get()
    if password=="1234":
       screen2=Toplevel(screen)
       screen2.title("decryption")
       screen2.geometry("400x200")
       screen2.configure(bg="#00bd56")

       message=text1.get(1.0,END)
       decode_message=message.encode("ascii")
       base64_bytes=base64.b64decode(decode_message)
       decrypt=base64_bytes.decode("ascii")

       Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
       text2=Text(screen2,font="Robot 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
       text2.place(x=10,y=40,width=380,height=150)

       text2.insert(END,decrypt)
    elif password=="":
        messagebox.showerror("decryption","Input Password")
    elif password !="1234":
        messagebox.showerror("decryption","Invalid Password")    
#################################################################################
def encrypt():  # Encryption Design & Function & Password Condition
    password=code.get()
    if password=="1234":
       screen1=Toplevel(screen)
       screen1.title("encryption")
       screen1.geometry("400x200")
       screen1.configure(bg="#ed3833")

       message=text1.get(1.0,END)
       encode_message=message.encode("ascii")
       base64_bytes=base64.b64encode(encode_message)
       encrypt=base64_bytes.decode("ascii")

       Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
       text2=Text(screen1,font="Robot 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
       text2.place(x=10,y=40,width=380,height=150)

       text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("encryption","Input Password")
    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")              
#################################################################################    
#################################################################################
def main_screen():  # Program Interface Design

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    
    #Icon for  Program
    image_icon=PhotoImage(file="kk.png")
    screen.iconphoto(False,image_icon) 
    screen.title("PctApp")
#################################################################################
    def reset(): #Reset Function
        code.set("")
        text1.delete(1.0,END)
#################################################################################        
    Label(text="Enter Text for Encryption & Decryption",fg="black",font=("calibre,13")).place(x=10,y=10) #Text Placement Design
    text1=Text(font="Robot 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
#################################################################################
    Label(text="Enter Secret Key for Encryption & Decryption",fg="black",font=("calibre",13)).place(x=10,y=170) #Password Placement Design
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
#################################################################################
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250) # Encrypt Icon Design
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250) #Decrypt Icon Design
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300) # Reset Icon Design
    screen.mainloop()
main_screen()    