#import random
#name1 = str(input("enter name"))

##rock =1
#paper =2
#scissor =3
#x=y=z=0
#
#while True:
#    print("Press 1 Rock 2 Paper 3 Scissor")
#    user1 =int(input("choose choice"))
#    comp =[1,2,3]
#    random.shuffle(comp)
#    computer = random.randint(1,3)
#    
#    
#    if user1==computer:
#        print("Draw")
#        z+=1
#    
#    
#        
#    if user1==1 and computer==2 :
#        print(computer," computer wins")
#        y+=1
#        
#    elif user1==1 and computer==3:
#        print(name1,"wins")
#        x+=1
#        
#    elif user1==2 and computer==3:
#        print(computer,"wins")
#        y+=1
#        
#    elif user1==2 and computer==1:
#        print(name1,"wins")
#        x+=1
#        
#    elif user1==3 and computer==1:
#        print(computer,"wins")
#        y+=1
#        
#    elif user1==3 and computer==2:
#        print(name1,"wins")
#        x+=1
#    print("computer wins :",x)
#    print(name1,"wins :",y)
#        
    
from tkinter import *
from tkinter import messagebox
import random


def R(no):
    global operator
    Rvalue = "Rock"
    operator = operator + str(no)
    text_input.set(operator)
    a = ["               Rock","               Paper","           Scissor"]
    random.shuffle(a)
    Cvalue = a[0]
    operator = operator + str(Cvalue)
    text_input.set(operator)
    
    if Rvalue == "Rock" and Cvalue=="               Rock":
        ans = "Match Draw"
        messagebox.showinfo("Draw",ans)
        
        
    elif Rvalue == "Rock" and Cvalue=="               Paper":
        ans = "Computer Wins"
        messagebox.showinfo("Computer",ans)
        
    elif Rvalue == "Rock" and Cvalue=="           Scissor":
        ans = "User wins"
        messagebox.showinfo("User",ans)
    
    
    
    
def P(no):
    global operator
    Pvalue = "Paper"
    operator = operator + str(no)
    text_input.set(operator)
    
    a = ["               Rock","               Paper","           Scissor"]
    random.shuffle(a)
    Cvalue = a[0]
    operator = operator + str(Cvalue)
    text_input.set(operator)
    
    
    if Pvalue == "Paper" and Cvalue=="               Rock":
        ans = "User wins"
        messagebox.showinfo("User",ans)
        
    elif Pvalue == "Paper" and Cvalue=="               Paper":
        ans = "Match Draw"
        messagebox.showinfo("Draw",ans)
        
    elif Pvalue == "Paper" and Cvalue=="           Scissor":
        ans = "Computer Wins"
        messagebox.showinfo("Computer",ans)
    
    

def S(no):
    global operator
    Svalue = "Scissor"
    operator = operator + str(no)
    text_input.set(operator)
    
    a = ["               Rock","               Paper","           Scissor"]
    random.shuffle(a)
    Cvalue = a[0]
    operator = operator + str(Cvalue)
    text_input.set(operator)
    
    
    if Svalue == "Scissor" and Cvalue == "               Rock":
        ans = "Computer wins"
        messagebox.showinfo("Computer",ans)
        
    elif Svalue == "Scissor" and Cvalue == "               Paper":
        ans = "User wins"
        messagebox.showinfo("User",ans)
        
    elif Svalue == "Scissor" and Cvalue == "           Scissor":
        ans = "Match Draw"
        messagebox.showinfo("Draw",ans)

    

def clear():
    global operator
    operator =""
    text_input.set(operator)
        


root = Tk()
text_input = StringVar()
operator =""

label = Label(root,text="Rock Paper Scissor",font=("aerial",20,"bold"),fg ="Tomato",bg="powder blue",padx=10,pady=10,).grid(columnspan=8)

label1 = Label(root,text="User Input",font=("aerial",30,"bold"),fg ="black",bg="powder blue",padx=10,pady=10).grid(row=1,column=0)

rock=Button(root,text="Rock",font=("aerial",10,"bold"),fg ="black",bg="powder blue",padx=40,pady=20,command=lambda :R(" Rock")).grid(row=2,column=0)

paper=Button(root,text="PAPER",font=("aerial",10,"bold"),fg ="black",bg="powder blue",padx=40,pady=20,command=lambda :P(" Paper")).grid(row=3,column=0)

textdisplay=Entry(root,font=('aerial',20,'bold'),textvariable=text_input,bd=10,
                  insertwidth=4,bg='powder blue',justify='left').grid(row=3,column=3)

scissor=Button(root,text="SCISSOR",font=("aerial",10,"bold"),fg ="black",bg="powder blue",padx=40,pady=20,command=lambda :S(" Scissor")).grid(row=4,column=0)

clear=Button(root,text="clear",font=("aerial",10,"bold"),fg ="black",bg="powder blue",padx=40,pady=20,command=clear).grid(row=4,column=3)

computer=Label(root,text="COMPUTER",font=("aerial",10,"bold"),fg ="black",bg="powder blue",padx=15,pady=15,justify="right").grid(row=3,column=4)




root.mainloop()
#
