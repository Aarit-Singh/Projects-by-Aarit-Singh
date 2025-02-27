'''
  This was my first true, somewhat complicated project, and thus it is very close to my heart
  pleaes excuse the objectively awful code and the fact that the Encryption key is just sitting in a file that would be written. i did not want to create a password protected
  file or a server-side database.
  this project taught me so many lessons in TKinter (pythons GUI creation library), and was very fun to do!
  it can generate a password, view all saved passowrd-username pairs, and save your passwords. very simple, but EVERYTHING is encrypted. 
'''
import tkinter as tk 
import os
from tkinter import filedialog, Text
from tkinter import *
import random
import string
import time
import subprocess
from cryptography.fernet import *
key = Fernet.generate_key()
fernet = Fernet(key)

window = Tk()
window.title("Password Manager: Login Frontend")
window.geometry("2000x2000")

data1=StringVar()
data2=StringVar()
Passlength = 0
useless = 0 
frame = Frame(window, width=2000, height = 2000)
emptyframe = Frame(window, width =2000, height = 2000)
emptyframe.place()

c1 = tk.StringVar()
passdata = StringVar()

data3 = "A"
data4 = "A"
frame1 = Frame(window, width = 2000, height = 2000)

def homescreen():
  frame1.place(x = 0, y = 0)
  frame1.tkraise()
  b8_text = tk.StringVar()
  b8_text.set("Password Notebook")
  b8= Button(frame1, textvariable=b8_text, command = FRame2)
  b8.grid(row = 1, column = 2, padx = 10, pady = 10)
  b7_text = tk.StringVar()
  b7_text.set("Password Generator")
  b7 = Button(frame1, textvariable= b7_text, command= proceed)
  b7.grid(row = 0, column = 2, padx = 10, pady = 10)
  label1.destroy()
  lable2.destroy()
  textbox1.destroy()
  textbox2.destroy()
  ebutton.destroy()
  eb2.destroy()
  


def proceed(): 
  global c1 
  c1.set("2")
  print(c1.get())
  if c1.get() == "2" :
   

  
    
    frame.grid(column = 0, row = 0)

    frame.tkraise()
    emptyframe.lower(frame)
    b1_text = tk.StringVar()
    b1_text.set("Password Length: " + str(Passlength))


    def counter():
        global Passlength 
        Passlength += 1 
        b1_text.set("Password Length: " + str(Passlength))
        b3_text.set("Reduce password length. Current password length:" + str(Passlength))

    b1 = Button(frame, textvariable = b1_text, command=counter)
    b1.place(x=0, y=0)
    b2_text = tk.StringVar()
    
    def generator():
        alphabet = string.ascii_letters
        Length  = range(abs(Passlength))
    
        global password 
        password = " "    
        for i in Length : 
          password += random.choice(alphabet)
        b2_text.set ("Your generated password is: " + str(password) )
    
    b2_text.set("Your generated password will replace this.")
    b2 = Button(frame, textvariable= b2_text, command=generator)
    b2.place(x=0, y=28)
    b3_text = tk.StringVar()
    b3_text.set("Reduce password length. Current password length:")


    def subtract():
       global Passlength
      
       if (Passlength >= 3):
        Passlength = Passlength - 1
        b3_text.set("Reduce password length. Current password length: " + str(Passlength) )
        b1_text.set("Password Length: " + str(Passlength))
       
    b3 = Button(frame, textvariable= b3_text, command=subtract)
    b3.place(x=0, y=56)
    b4_text = tk.StringVar()
    b4_text.set("⎘")

    def copy_cmd():
      data = password
      subprocess.run("pbcopy", text=True, input = data)
    def thisshouldplaceframe1again_2() :
       frame1.tkraise()
       emptyframe.lower(frame1)
       b4.place_forget()
       b6_2.place_forget()
       b3.place_forget()
       b2.place_forget()
       b1.place_forget()
    b4 = Button(frame, textvariable = b4_text, command = copy_cmd)
    b4.place( x = 300, y = 28)
    b6_2_text = tk.StringVar()
    b6_2_text.set("🏠, Home Page")
    b6_2 = Button(frame, textvariable= b6_2_text,  command = thisshouldplaceframe1again_2)
    b6_2.place(x = 0, y = 750)


 
def passwordsread():
  frame3 = Frame(window, height=  2000, width = 2000)
  frame3.place(x = 0, y = 0)
 
  file10 = open("voice.txt","rb")
  x = file10.read()
  file10.close()
  

  decMessage = fernet.decrypt(x)

 
 


  label3 = Label(frame3, text =str(decMessage,  'utf-8'))
  label3.place( x = 0, y =0)
  b10_text = tk.StringVar()
  b10_text.set("← Back")
  b10 = Button(frame3,textvariable=b10_text, command = FRame2 )
  b10.place(x = 500, y = 0)
def FRame2():
  def thisshouldplaceframe1again():
    frame1.tkraise()
    emptyframe.lower(frame1)
    tb1.destroy()
    frame2.lower(emptyframe)
    b6.place_forget()
    b7.place_forget()
    b8.place_forget()
    b9.place_forget()
  frame2 = Frame(window, width =2000, height = 2000)
  frame2.tkraise()
  

 
  tb1 = Text(frame2, bg = "black", fg = "white", font=('Arial', 20), height= 30, width =75, )
  frame2.place( x= 0 , y = 0)
  tb1.place( x= 0, y= 0)
 
  b6_text = tk.StringVar()
  b6_text.set("🏠, Home Page")
  b6 = Button(frame2, textvariable= b6_text,  command = thisshouldplaceframe1again)
  b6.place(x = 0, y = 750)
  b7_text = tk.StringVar()
  b7_text.set("Save typed passwords")
  def filewriter():
    file4 = open("voice.txt", "rb")
    password_contents = file4.readlines()
    file4.close()
    z = password_contents[1]
    y = password_contents[2:END]
    decz = fernet.decrypt(z)
    file5 = open("voice.txt","wb")
    file5.writelines(decz.encode())
    file5.close()

    input2 = tb1.get("1.0", END)
    file = open("voice.txt","ab")
    file.write(input2.encode())
    file.close()
    file2 = open("voice.txt","rb")
    x = file2.read()
    file2.close()
    file3 = open("voice.txt", "wb")
    message=str(x)
    
    encMessage = fernet.encrypt(message.encode())
    file3.writelines(encMessage)
    file3.close()
  
  
    
  b7 = Button(frame2, textvariable = b7_text, command = filewriter)
  b7.place(x = 200, y = 750)
  b8_text = tk.StringVar()
  b8_text.set("Passwords Saved")
  b8 = Button(frame2, textvariable = b8_text, command = passwordsread)
  b8.place(x = 400, y = 750)
  b9_text  = tk.StringVar()
  b9_text.set("Clear Saved Passwords")

  def b9_command():
    if b9_text.get() == "Passwords have been cleared":
      b9_text.set("Clear Saved Passwords")
    
    b9_text.set("Passwords have been cleared")
    file4 = open("voice.txt", "wb")
    file4.write("".encode())
    file4.close()
  
    
     
     

  b9 = Button(frame2, textvariable = b9_text, command = b9_command)
  b9.place( x = 600, y= 750)
  




eb2_text = tk.StringVar()
eb2_text.set("")
eb2 = Button(window, textvariable= eb2_text, command = homescreen)
def passcheck():
  if (data1.get() == data3) & (data2.get() == data4):
    eb2_text.set("Login Sucessful, Proceed to password manager?")
    eb2.grid(row=4, column = 2)
label1=Label(window,text="Username:", fg = 'white')
label1.grid(row=0,column=0, padx= 10, pady=10)
textbox1=Entry(window, textvariable=data1, fg = "white", show="•")
textbox1.grid(row=0, column= 1, padx=10, pady = 10)
lable2=Label(window, text= "Password:", fg = "white")
lable2.grid(row=1, column=0)
textbox2=Entry(window, textvariable=data2, fg = "white", show = "•")
textbox2.grid(row=1, column=1, padx = 10, pady = 10)
ebutton_text = tk.StringVar()
ebutton_text.set("Login")
ebutton = Button(window,textvariable= ebutton_text, command= passcheck)
ebutton.grid(row = 3, column = 2)
window.mainloop()
