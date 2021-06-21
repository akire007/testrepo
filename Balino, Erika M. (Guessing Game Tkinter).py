from tkinter import*
import random

    
main_Container = Tk()
main_Container.title("NUMBER GUESSING GAME")
main_Container.geometry("500x350")

title_Container=Frame(main_Container)
title_Container.pack(side=TOP)
name_Container = Frame(main_Container)
name_Container.pack(side=TOP)
option_Container = Frame(main_Container)
option_Container.pack(side=TOP)
guess_Container = Frame(main_Container)
guess_Container.pack(side=TOP)

Name=StringVar()
Hello =StringVar()
self =Button
text = StringVar() 
attempts = 0
answer = random.randint(1,10)


def Play():
    def Check():
        global attempts
        global text
     
        guess = int(entry_guess.get())
        attempts += 1 
    
        if guess == answer:
            text.set("Congratulations you guessed the number!! \nNumber of tries: " + str(attempts))
            btn_check.pack_forget()
        elif attempts==3:
            text.set("You are out of attempts. You Lost!!")
            btn_check.pack_forget()
        elif guess < answer:
            text.set("Guess Higher...")
        elif guess > answer:    
            text.set("Guess Lower...")
            
    game_Descpt = Label(guess_Container, font=('arial',12), text="\nI'm thinking a number between 1 and 10\nYou have to guess a number in 3 tries")
    game_Descpt.pack()

    entry_guess = Entry(guess_Container, width=48, borderwidth=4)
    entry_guess.pack()

    btn_check = Button(guess_Container, padx=5, bd=3, font=('arial', 8), width=5, text="Check", bg="Gold",command=Check)
    btn_check.pack()

    btn_quit = Button(guess_Container, padx=5, bd=3, font=('arial', 8), width=5, text="Quit", bg="Gold", command=main_Container.destroy)
    btn_quit.pack()

    guess_attempts =Label(guess_Container, textvariable=text) 
    guess_attempts.pack()
    
    hello_Msg.grid_forget()
    self.btn_Yes.grid_forget()
    self.btn_No.grid_forget()
    
def Enter():
    getting_name = (Name.get())
    Hello.set(f"\nHello! {getting_name} \nWould you like to play a game?")
    
    self.btn_Yes = Button(option_Container, padx=5, bd=3, font=('arial', 8), width=5, text="Yes", bg="Gold", command=Play)
    self.btn_Yes.grid(row=6,column=2)
    self.btn_No = Button(option_Container, padx=5, bd=3, font=('arial', 8), width=5, text="No", bg="Gold",command=main_Container.destroy)
    self.btn_No.grid(row=6,column=3)
    
    Uname.grid_forget()
    Uname_Entry.grid_forget()
    btn_Enter.grid_forget()    

game_Title= Label (title_Container, font=('arial',30, 'bold'),text="Number Guessing Game",fg="Gold")
game_Title.pack(side=LEFT)

Uname= Label (name_Container, font=('arial',12),text="Enter your name:", fg="Black")
Uname.grid(row=1,column=0)

Uname_Entry = Entry(name_Container, font=('arial',12), bd=5, insertwidth=4, bg="White", justify='left',textvariable=Name)
Uname_Entry.grid(row=1,column=1)

btn_Enter = Button(name_Container, padx=5, bd=3, font=('arial', 8), width=5, text="ENTER", bg="Gold", command= Enter)
btn_Enter.grid(row=1,column=2)

hello_Msg = Label(name_Container, font=('arial',12), bd=0, justify='left', textvariable=Hello)
hello_Msg.grid(row=0,column=0)

main_Container.mainloop()