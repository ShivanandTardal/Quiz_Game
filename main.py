from tkinter import*
from tkinter.ttk import Progressbar

root=Tk()
root.state('zoomed')
root.config(bg='black')


def start():
    root.destroy()
    root1=Tk()
    root1.state('zoomed')
    root1.title("Quiz Game KBC")
    root1.config(bg="black")



    def select(event):

        progressbarA.place_forget()
        progressbarB.place_forget()
        progressbarC.place_forget()
        progressbarD.place_forget()

        progresslableA.place_forget()
        progresslableB.place_forget()
        progresslableC.place_forget()
        progresslableD.place_forget()

        for i in range(15):
            b=event.widget
            value=b['text']
            if value == correct_answers[i]:
                if value == correct_answers[14]:
                    def close():
                        root3.destroy()
                        root1.destroy()
                        

                    def tryagain():
                        audiancepolebutton2.config(state=NORMAL, image=audiancepole)
                        lifelinebutton1.config(state=NORMAL, image=image50)
                        root3.destroy()
                        questionsarea.delete(1.0,END)
                        questionsarea.insert(END,questions[0])

                        option1btn.config(text=first_option[0])
                        option2btn.config(text=second_option[0])
                        option3btn.config(text=third_option[0])
                        option4btn.config(text=fourth_option[0])
                            
                    root3=Toplevel()
                    root3.overrideredirect(True)
                    root3.config(bg='black')
                    root3.geometry("500x400+470+30")
                    root3.title("You Want 0 Rs")
                    imglabal=Label(root3,image=centerimage,bd=0,bg="black")
                    imglabal.pack(pady=30)

                    wonlable=Label(root3,text="You Won",font=('arial',30,'bold'),bg="black",fg='white')
                    wonlable.pack()

                    playagainbtn=Button(root3,text="Play Again",font=('arial',20,'bold'),bd=0,bg="black",fg='white',activebackground="black",activeforeground="white",cursor="hand2",command=tryagain)
                    playagainbtn.pack()

                    closeagainbtn=Button(root3,text="Close",font=('arial',20,'bold'),bd=0,bg="black",fg='white',activebackground="black",activeforeground="white",cursor="hand2",command=close)
                    closeagainbtn.pack()

                    happyimage=PhotoImage(file="happy.png")
                    happylable=Label(root3,image=happyimage,bg="black")
                    happylable.place(x=42,y=242)

                    happylable1=Label(root3,image=happyimage,bg="black")
                    happylable1.place(x=382,y=242)

                    root3.mainloop()           
                    break

                questionsarea.delete(1.0,END)
                questionsarea.insert(END,questions[i+1])

                option1btn.config(text=first_option[i+1])
                option2btn.config(text=second_option[i+1])
                option3btn.config(text=third_option[i+1])
                option4btn.config(text=fourth_option[i+1])
                break   

            if value  not in correct_answers:
                def close():
                    root2.destroy()
                    root1.destroy()
                    

                def tryagain():
                    audiancepolebutton2.config(state=NORMAL, image=audiancepole)
                    lifelinebutton1.config(state=NORMAL, image=image50)
                    root2.destroy()
                    questionsarea.delete(1.0,END)
                    questionsarea.insert(END,questions[0])

                    option1btn.config(text=first_option[0])
                    option2btn.config(text=second_option[0])
                    option3btn.config(text=third_option[0])
                    option4btn.config(text=fourth_option[0])

                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry("500x400+470+30")
                root2.title("You Want 0 Rs")

                imglabal=Label(root2,image=centerimage,bd=0,bg="black")
                imglabal.pack(pady=30)

                loselable=Label(root2,text="You Lose",font=('arial',30,'bold'),bg="black",fg='white')
                loselable.pack()

                tryagainbtn=Button(root2,text="Try Again",font=('arial',20,'bold'),bd=0,bg="black",fg='white',activebackground="black",activeforeground="white",cursor="hand2",command=tryagain)
                tryagainbtn.pack()

                closeagainbtn=Button(root2,text="Close",font=('arial',20,'bold'),bd=0,bg="black",fg='white',activebackground="black",activeforeground="white",cursor="hand2",command=close)
                closeagainbtn.pack()

                sadimage=PhotoImage(file="sad.png")
                sadlable=Label(root2,image=sadimage,bg="black")
                sadlable.place(x=42,y=242)

                sadlable1=Label(root2,image=sadimage,bg="black")
                sadlable1.place(x=382,y=242)

                root2.mainloop()           
                break

    def lifeline50():
        lifelinebutton1.config(image=image50x)
        lifelinebutton1.config(state=DISABLED)

        if questionsarea.get(1.0, 'end-1c') == questions[0]:
            option2btn.config(text='')
            option4btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[1]:
            option2btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[2]:
            option1btn.config(text='')
            option4btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[3]:
            option1btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[4]:
            option2btn.config(text='')
            option4btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[5]:
            option3btn.config(text='')
            option1btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[6]:
            option1btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[7]:
            option1btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[8]:
            option1btn.config(text='')
            option4btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[9]:
            option1btn.config(text='')
            option4btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[10]:
            option2btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[11]:
            option1btn.config(text='')
            option4btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[12]:
            option2btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[13]:
            option2btn.config(text='')
            option3btn.config(text='')
        if questionsarea.get(1.0, 'end-1c') == questions[14]:
            option1btn.config(text='')
            option4btn.config(text='')

    def audiancepolelifeline():

        audiancepolebutton2.config(image=audiancepolex,state=DISABLED)

        progressbarA.place(x=1080,y=200)
        progressbarB.place(x=1120,y=200)
        progressbarC.place(x=1160,y=200)
        progressbarD.place(x=1200,y=200)

        progresslableA.place(x=1080,y=320)
        progresslableB.place(x=1120,y=320)
        progresslableC.place(x=1160,y=320)
        progresslableD.place(x=1200,y=320)

        if questionsarea.get(1.0, 'end-1c') == questions[0]:
            progressbarA.config(value=23)
            progressbarB.config(value=63)
            progressbarC.config(value=93)
            progressbarD.config(value=83)
        if questionsarea.get(1.0, 'end-1c') == questions[1]:
            progressbarA.config(value=13)
            progressbarB.config(value=33)
            progressbarC.config(value=73)
            progressbarD.config(value=96)
        if questionsarea.get(1.0, 'end-1c') == questions[2]:
            progressbarA.config(value=23)
            progressbarB.config(value=83)
            progressbarC.config(value=93)
            progressbarD.config(value=73)
        if questionsarea.get(1.0, 'end-1c') == questions[3]:
            progressbarA.config(value=33)
            progressbarB.config(value=63)
            progressbarC.config(value=33)
            progressbarD.config(value=93)
        if questionsarea.get(1.0, 'end-1c') == questions[4]:
            progressbarA.config(value=99)
            progressbarB.config(value=83)
            progressbarC.config(value=73)
            progressbarD.config(value=53)
        if questionsarea.get(1.0, 'end-1c') == questions[5]:
            progressbarA.config(value=33)
            progressbarB.config(value=99)
            progressbarC.config(value=3)
            progressbarD.config(value=13)
        if questionsarea.get(1.0, 'end-1c') == questions[6]:
            progressbarA.config(value=23)
            progressbarB.config(value=93)
            progressbarC.config(value=73)
            progressbarD.config(value=63)
        if questionsarea.get(1.0, 'end-1c') == questions[7]:
            progressbarA.config(value=23)
            progressbarB.config(value=33)
            progressbarC.config(value=63)
            progressbarD.config(value=93)
        if questionsarea.get(1.0, 'end-1c') == questions[8]:
            progressbarA.config(value=23)
            progressbarB.config(value=83)
            progressbarC.config(value=93)
            progressbarD.config(value=43)
        if questionsarea.get(1.0, 'end-1c') == questions[9]:
            progressbarA.config(value=23)
            progressbarB.config(value=91)
            progressbarC.config(value=73)
            progressbarD.config(value=70)
        if questionsarea.get(1.0, 'end-1c') == questions[10]:
            progressbarA.config(value=23)
            progressbarB.config(value=43)
            progressbarC.config(value=72)
            progressbarD.config(value=99)
        if questionsarea.get(1.0, 'end-1c') == questions[11]:
            progressbarA.config(value=81)
            progressbarB.config(value=73)
            progressbarC.config(value=97)
            progressbarD.config(value=23)
        if questionsarea.get(1.0, 'end-1c') == questions[12]:
            progressbarA.config(value=93)
            progressbarB.config(value=83)
            progressbarC.config(value=33)
            progressbarD.config(value=43)
        if questionsarea.get(1.0, 'end-1c') == questions[13]:
            progressbarA.config(value=43)
            progressbarB.config(value=33)
            progressbarC.config(value=73)
            progressbarD.config(value=93)
        if questionsarea.get(1.0, 'end-1c') == questions[14]:
            progressbarA.config(value=23)
            progressbarB.config(value=83)
            progressbarC.config(value=93)
            progressbarD.config(value=63)

    correct_answers = ["Guido van Rossum", "all of the mentioned", ".py", "None of the mentioned", "Indentation", "#",
                    "Linux", "sys.version", "Preferred Installer Program", "getopt", "set()", "Both A and B", "9.0", "Apple",
                    "Bill Gates"]


    questions = ["1. Who developed Python Programming Language?",
                "2. Which type of Programming does Python support?",
                "3. Which of the following is the correct extension of the Python file?",
                "4. All keywords in Python are in _________",
                "5. Which of the following is used to define a block of code in Python language?",
                "6. Which of the following character is used to give single-line comments in Python?",
                "7. Which one is the first fully supported 64-bit operating system?",
                "8. Which of the following functions can help us to find the version of python that we are currently working on?",
                "9. What does pip stand for python?",
                "10. Which module in the python standard library parses options received from the command line?",
                "11. Which of the following statements is used to create an empty set in Python?",
                "12. What are the two main types of functions in Python?How many continents are there in the world?",
                "13. What is output of print(math.pow(3, 2))?",
                "14. ipad is manufactured by?",
                "14. Who founded Microsoft?"]

    first_option = ["Wick van Rossum", "object-oriented programming",
                    ".python", "Capitalized",
                    "Indentation", "//",
                    "Windows 7", "sys.version(1)", "Pip Installs Python", "getarg",
                    "( )", "Built-in function",
                    "9.0", "Google", "Monty Ritz"]

    second_option = ["Rasmus Lerdorf", "structured programming",
                    ".pl", "lower case",
                    "Key", "#",
                    "Linux", "sys.version(0)", "Pip Installs Packages", "getopt",
                    "[ ]", "User defined function",
                    "9",
                    "Microsoft", "Danis Lio"]

    third_option = ["Guido van Rossum", "functional programming",
                    ".py", "UPPER CASE",
                    "Brackets", "/*",
                    "Mac", "sys.version()", "Preferred Installer Program", "main",
                    "{ }", "Both A and B",
                    "None",
                    "Amazon", "Bill Gates"]

    fourth_option = ["Niene Stom", "all of the mentioned",
                    ".p", "None of the mentioned",
                    "All of the mentioned", "!",
                    "Windows XP", "sys.version", " All of the mentioned", "os",
                    "set()",
                    "User function",
                    "None of the mentioned", "Apple",
                    "Jeff Bezos"]



    topframe=Frame(root1,bg="black",pady=20)
    topframe.place(x=549,y=23)

    centerframe=Frame(root1,bg="black",pady=20)
    centerframe.place(x=573,y=163)

    botumframe=Frame(root1,bg="black",width=1290,height=370)
    botumframe.place(x=323,y=423)

    image50=PhotoImage(file="50-50.png")
    image50x=PhotoImage(file="50-50-X.png")

    lifelinebutton1=Button(topframe,image=image50,bg="black",bd=0,activebackground="black",width=180,height=80,command=lifeline50)
    lifelinebutton1.grid(row=0,column=0)

    audiancepole=PhotoImage(file="audiencePole.png")
    audiancepolex=PhotoImage(file="audiencePoleX.png")

    audiancepolebutton2=Button(topframe,image=audiancepole,bg="black",bd=0,activebackground="black",width=180,height=80,command=audiancepolelifeline)
    audiancepolebutton2.grid(row=0,column=1)

    centerimage=PhotoImage(file="center.png")

    centerlabal=Label(centerframe,image=centerimage,bg="black",width=300,height=200)
    centerlabal.grid(row=0,column=0)



    questionsarea=Text(botumframe,font=('arial', 18, 'bold'), bg='black', fg='white', width=73, height=2,bd=0)
    questionsarea.insert(END, questions[0])
    questionsarea.place(x=13,y=3)

    option1lable=Label(botumframe,text="A:",bg="black",fg="white",font=('arial', 18, 'bold'))
    option1lable.place(x=16,y=95)

    option1btn=Button(botumframe,text=first_option[0],font=('arial', 18, 'bold'),bg="black",fg="white",bd=0)
    option1btn.place(x=45,y=89)

    option2lable=Label(botumframe,text="B:",bg="black",fg="white",font=('arial', 18, 'bold'))
    option2lable.place(x=16,y=225)

    option2btn=Button(botumframe,text=second_option[0],font=('arial', 18, 'bold'),bg="black",fg="white",bd=0)
    option2btn.place(x=45,y=219)

    option3lable=Label(botumframe,text="C:",bg="black",fg="white",font=('arial', 18, 'bold'))
    option3lable.place(x=526,y=95)

    option3btn=Button(botumframe,text=third_option[0],font=('arial', 18, 'bold'),bg="black",fg="white",bd=0)
    option3btn.place(x=555,y=89)

    option4lable=Label(botumframe,text="D:",bg="black",fg="white",font=('arial', 18, 'bold'))
    option4lable.place(x=526,y=225)

    option4btn=Button(botumframe,text=fourth_option[0],font=('arial', 18, 'bold'),bg="black",fg="white",bd=0)
    option4btn.place(x=555,y=219)

    progressbarA=Progressbar(root1,orient=VERTICAL,length=120)
    progressbarB=Progressbar(root1,orient=VERTICAL,length=120)
    progressbarC=Progressbar(root1,orient=VERTICAL,length=120)
    progressbarD=Progressbar(root1,orient=VERTICAL,length=120)

    progresslableA=Label(root1,text='A',font=('arial',20,'bold'),bg='black',fg='white')
    progresslableB=Label(root1,text='B',font=('arial',20,'bold'),bg='black',fg='white')
    progresslableC=Label(root1,text='C',font=('arial',20,'bold'),bg='black',fg='white')
    progresslableD=Label(root1,text='D',font=('arial',20,'bold'),bg='black',fg='white')

    option1btn.bind('<Button>',select)
    option2btn.bind('<Button>',select)
    option3btn.bind('<Button>',select)
    option4btn.bind('<Button>',select)

    root1.mainloop()




bgimage=PhotoImage(file="center.png")
bgimagelable=Label(root,image=bgimage,bg='black')
bgimagelable.place(x=533,y=294)

bghappyimg=PhotoImage(file='happy.png')
bghappyimglable=Label(root,image=bghappyimg,bg='black',width=110)
bghappyimglable.place(x=140,y=87)
bghappyimglable1=Label(root,image=bghappyimg,bg='black',width=110)
bghappyimglable1.place(x=1220,y=85)

lable1=Label(root,text="WELCOME TO PYTHON QUIZ",font=('arial',50,'bold'),bg='black',fg='white')
lable1.place(x=275,y=76)

startbtn=Button(root,text='  Start  ',font=('arial',20,'bold'),bg='black',fg='white',command=start)
startbtn.place(x=650,y=622)
root.mainloop()