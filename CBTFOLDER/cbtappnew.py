#A CBT application using python
#####################################################about the app##############################################################################################
__author__="DaVinci kay"
__authoremail__="kayzeebiz@gmail.com"
__project__=" A Computer base test application"
__description__="""this application is a computer base test application"""
__date__="8-04-2016"
__version__="version 1.0"

#################################################################################################################################################################
#platform for the cbt application for the
try:
    import tkinter
    from tkinter import Frame as frame
    from tkinter import StringVar,IntVar,Tk,PhotoImage
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import sqlite3 as lite
    from re import *
    from random import *
    
except ImportError:
    import Tkinter
    from Tkinter import Frame as frame
    from Tkinter import StringVar,IntVar,Tk,PhotoImage
    from Tkinter.ttk import *
    from Tkinter.messagebox import *
    print("An error occured while importing a module")

app=Tk()
#for the big srceen
app.geometry("1355x730+0+0")
app.resizable(False,False)
app.config(bg="#ffffff")
app.title("CBT APPLICATION")
app.iconname("CBT ADMIN")

#the  styles for the widgets
style=Style()
style.theme_use("clam")
#print(style.theme_names())
style.configure('TLabel',background="#ffffff",foreground="steelblue",font=("Verdana",12,'bold'))
style.configure('TEntry',background="#ffffff",foreground="black",font=("Verdana",12,'bold'))
style.configure('TCombobox',background="#ffffff",foreground="steelblue",font=("Verdana",15))
style.configure('TButton',background='steelblue',foreground='#ffffff',activebackground="#22ff00",font=("Verdana",15,"bold"))
style.configure('header.TLabel',background='steelblue',foreground='#ffffff',font=("Verdana",15,"bold"))
style.configure('TFrame',background="#ffffff")
style.configure('link.TButton',background="#ffffff",foreground="steelblue",activeforeground="pink",font=('Verdana',12,'bold'),borderwidth=0,padx=0)
style.configure('warn.TLabel',background="#ffffff",foreground="red",font=("Verdana",12,'bold'))
style.configure("TRadiobutton",background="#ffffff",foreground="#000000",font=("Verdana",12,"bold"))
style.configure('quest.TLabel',background='#ffffff',foreground='#000000',font=("Verdana",12,"bold"),justify='LEFT')
style.configure('time.TLabel',background='white',foreground='red',font=("Verdana",15,"bold"))
style.configure('note.TLabel',background='white',foreground='red',font=("Verdana",15,"bold","underline"))
style.configure('number.TLabel',background='#ffffff',foreground='#000000',font=("Verdana",12,"bold"))
style.configure('TProgressbar',background='steelblue',foreground='#ffffff')



#the frame function used throughout the app
def frames(parent,side,expand=None,fill=None,anchor=None,bd=None,hei=None,wid=None):
    """the function for the frames"""
    frame_name=Frame(parent,style='TFrame',borderwidth=bd,height=hei,width=wid)
    frame_name.pack(side=side,expand=expand,anchor=anchor,fill=fill)
    return frame_name

##############images for the application###################
addimg=PhotoImage(file="Add.png")
correctimg=PhotoImage(file="Check.png")
wrongimg=PhotoImage(file="Delete.png")
passwordimg=PhotoImage(file="Key.png")
forwardimg=PhotoImage(file="Next.png")
previousimg=PhotoImage(file="Previous.png")
userimg=PhotoImage(file="User.png")
refreshimg=PhotoImage(file="Refresh.png")
logoutimg=PhotoImage(file="Logout.png")
favoriteimg=PhotoImage(file="Favorite.png")
loginimg=PhotoImage(file="Play.png")
submitimg=PhotoImage(file="Save.png")
headerimg=PhotoImage(file="header.png")
splashimg=PhotoImage(file="splash.png")
################end of images########################

class Timer():
    """the timer of the application"""
    def __init__(self,lab1,mins,sec):
        """the init method"""
        #the timer for my cbt app
        self.mins=mins
        self.sec=sec
        self.lab1=lab1
        

    def timer(self):
        def count():
            self.sec-=1
            if self.sec==0:
                self.mins-=1
                self.sec=59
            if self.mins==0 and self.sec==0:
                app.destroy()
            else:
                self.lab1.config(text="%2d : %2d"%(self.mins,self.sec))
                self.lab1.after(1000,count)
        count()
    def reset(self,mins,sec):
        """the method for resetting the timer"""
        self.lab1.config(text="")
        self.mins=mins
        self.sec=sec

#the cbt object
class Cbt(frame):
    """the object class called the cbt"""
    def __init__(self,master):
        frame.__init__(self,master)
        self.master=master
        self.index=0#the index for the questions
        

        #calling the methods
        self.CreateFrame()
        self.LoginPage()
        self.RegPage()
        self.TestPage()
        self.FinalPage()
        

    def LoginPage(self):
        """designing the login page"""
        #frame for the header
        headerFrame=frames(self.LoginFrame,"top")
        #the list for the labels
        headerLabel=Label(headerFrame,style='header.TLabel',text='\t\t\t\t\tCBT Login Page',justify='center',width=100)
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        #label for the image
        imageLabel=Label(headerFrame,style='TLabel',text='',justify='center',width=100,image=headerimg,compound="center")
        imageLabel.pack(side='top',padx=30,pady=5,fill='x')
        
        
        #guiding text for the label
        text="Enter your username, password and choose your subject choice to login for the test"
        #guiding label
        label=Label(headerFrame,style='TLabel',text=text,width=70)
        label.pack(side='top',pady=5,padx=5)

       #string variables for the entries
        self.user=StringVar()
        self.passw=StringVar()

        #list for the stringvariables
        var=[self.user,self.passw]
        #list for the labels and entries
        entrylist=[["Username :","Username"],["Password :","password"]]

        #list for the images
        images=[userimg,passwordimg]
        #creating the labels and entries
        index=0
        for i in entrylist:
            label,entry=i
            entframe=Frame(self.LoginFrame,style="TFrame")
            entframe.pack(side="top",anchor="center",pady=30)
            label=Label(entframe,style="TLabel",width=20,text=label,image=images[index],compound='left')
            label.pack(side='left',anchor='center',pady=2,padx=10)
            ent=Entry(entframe,style="TEntry",width=30,textvariable=var[index])
            ent.pack(side='left',anchor="center",pady=2)
            index+=1
        ent.config(show='*')

        #getting the values of the combobox from database
        values=[]
        conn=lite.connect("cbtapp.db")
        subjects=conn.execute("select * from subjecttab")
        for i in subjects:
            values.append(i[1])

        #combobox for the subject choice
        self.choice=StringVar()#variable for the combobox
        choicelist=["Subject :","subject"]
        entframe=Frame(self.LoginFrame,style="TFrame")
        entframe.pack(side="top",anchor="center",pady=30)
        label,combo=choicelist
        lab=Label(entframe,style="TLabel",width=20,text=label,image=favoriteimg,compound="left")
        lab.pack(side="left",anchor='center',pady=2,padx=10)
        comb=Combobox(entframe,style="TCombobox",width=27,values=values,textvariable=self.choice)
        comb.pack(side="left",anchor="center",pady=2)

           
        #warning label
        self.label=Label(self.LoginFrame,style="warn.TLabel",width=40)
        self.label.pack(side='top')

        #creating list buttons' properties on the login page
        butlist=['Clear','Login','Close']
        butcommand=[self.Clear,self.Login,self.Close]
        butimages=[refreshimg,loginimg,logoutimg]#images for the buttons
        index=0

        #creating the buttons
        butframe=frames(self.LoginFrame,'top')#frame for the button

        for i in butlist:
            i=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound="left")
            i.pack(side='left',padx=5,pady=5)
            index+=1

        #changing password
        butframe=frames(self.LoginFrame,"top")#frame for the button

        text="if you are new to this app register"#text for the label
        label=Label(butframe,style='TLabel',width=28,text=text)
        label.pack(side='left',pady=9)
        #link button
        but=Button(butframe,style='link.TButton',text="here",width=4,command=self.Here)
        but.pack(side='left')

    def RegPage(self):
        """method that designs the registation page"""
        #frame for the header
        headerFrame=frames(self.RegFrame,"top")
        #the list for the labels
        headerLabel=Label(headerFrame,style='header.TLabel',text='\t\t\t\t\tCBT Registration Page',justify='center',width=100)
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        #label for the image
        imageLabel=Label(headerFrame,style='TLabel',text='',justify='center',width=100,image=headerimg,compound="center")
        imageLabel.pack(side='top',padx=30,pady=5,fill='x')
        
        #guiding text for the label
        text="Enter your prefered username and password submit to register"
        #guiding label
        label=Label(headerFrame,style='TLabel',text=text,width=60)
        label.pack(side='top',pady=5,padx=5)

        #string variables for the entries
        self.NewUser=StringVar()
        self.NewPass=StringVar()

        #list for the stringvariables
        var=[self.NewUser,self.NewPass]

        #list for the images
        images=[userimg,passwordimg]
        
        #list for the labels and entries
        entrylist=[["Username :","Username"],["Password :","password"]]
        #creating the labels and entries
        index=0
        for i in entrylist:
            label,entry=i
            entframe=Frame(self.RegFrame,style="TFrame")
            entframe.pack(side="top",anchor="center",pady=30)
            label=Label(entframe,style="TLabel",width=14,text=label,image=images[index],compound='left')
            label.pack(side='left',anchor='center',pady=2,padx=3)
            ent=Entry(entframe,style="TEntry",width=30,textvariable=var[index])
            ent.pack(side='left',anchor="center",pady=2)
            index+=1
        ent.config(show='*')
            
           
        #warning label
        self.regLabel=Label(self.RegFrame,style="warn.TLabel",width=40)
        self.regLabel.pack(side='top')

        #functions for the regpage
        def Prev():
            """navigating back to the login page"""
            self.RegFrame.pack_forget()
            self.regLabel.config(text="")
            self.LoginFrame.pack(side="top",expand="yes",fill="both")
        def Clear():
            """clearing the entries"""
            self.NewUser.set("")
            self.NewPass.set("")
            self.regLabel.config(text="")
        def Submit():
            """method responsible for sumission of password """
            a=self.NewUser.get()
            b=self.NewPass.get()
            if a!="" and b!="":#checking if any entry is empty
                try:#checking if the username already exists
                    conn=lite.connect("cbtapp.db")
                    cur=conn.cursor()
                    cur.execute("insert into userdetails(username,password) values(?,?)",(a,b))
                    conn.commit()
                    self.RegFrame.pack_forget()
                    self.LoginFrame.pack(side="top",expand="yes",fill="both")
                    self.regLabel.config(text="")
                    app.title("Login page")
                    
                except:
                    self.regLabel.config(text="Username has been used")
            else:
                self.regLabel.config(text="One or more entries empty")

        #creating buttons on page
        butlist=["Prev",'Clear','Submit','Close']
        butcommand=[Prev,Clear,Submit,self.Close]
        butimages=[previousimg,refreshimg,submitimg,logoutimg]
        index=0

        #creting the buttons
        butframe=frames(self.RegFrame,'top')#frame for the button

        for i in butlist:
            i=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound="left")
            i.pack(side='left',padx=5,pady=5)
            index+=1

        #changing password
        butframe=frames(self.RegFrame,"top")#frame for the button

    def TestPage(self):
        """method that designs the test page"""
        #frame for the header
        headerFrame=frames(self.TestFrame,"top")
        #the list for the labels
        headerLabel=Label(headerFrame,style='header.TLabel',text='\t\t\t\t\tTest Page',justify='center',width=100)
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')
        #guiding text for the label
        text="Note: Dont click on the submit button if you are not through with your test"
        #guiding label
        label=Label(headerFrame,style='note.TLabel',text=text,width=70)
        label.pack(side='top',pady=5,padx=5)

        #designing username label on the Testpage
        self.userlist=["Username :",'']
        userframe=frames(self.TestFrame,"top",anchor="nw",)
        for i in range(2):#creating the labels for the username
            self.userlist[i]=Label(userframe,width=12,style="TLabel",text=self.userlist[i])
            self.userlist[i].pack(side="left",padx=4)
        
        

        #designing the timer for the app
        self.lablist=["Time :",'min']
        timeframe=frames(self.TestFrame,"top",anchor="ne",)
        for i in range(2):#creating the labels for the timer
            self.lablist[i]=Label(timeframe,width=6,style="time.TLabel",text=self.lablist[i])
            self.lablist[i].pack(side="left")

        #designing the widget for the questions
        questframe=frames(self.TestFrame,"top")#frame for the question and the question number
        #the question label
        self.num=StringVar()#integer variable for the questions

        #label for the question label
        numlabel=Label(questframe,width=3,style="number.TLabel",textvariable=self.num)
        numlabel.pack(side="left")
        self.question=StringVar()#the string variable for the questipon label
        Question=Label(questframe,style="quest.TLabel",textvariable=self.question,width=70)
        Question.pack(side='left',anchor="center",)

        #designing the radiobutton for the options
        radframe=Frame(self.TestFrame,style="TFrame")
        radframe.pack(side="top",pady=55)
        self.answer=StringVar()
        self.option=["A","B","C","D"]
        for i in range(4):
            self.option[i]=Radiobutton(radframe,value=self.option[i],variable=self.answer,style="TRadiobutton",width=60,command=self.Answer)
            self.option[i].pack(side="top",anchor="center",pady=10)
        #fuctions for the buttons on the page
        

        
        def Prev():
            """the method for navigating the questions backwards"""
            
            if self.index>0:
                self.index-=1
                self.answer.set(self.choosedans[self.index])
            else:
                app.bell()
                
            self.num.set("%d."%(self.index+1))
            self.question.set(self.questlist[self.index][1])
            self.option[0].config(text=self.questlist[self.index][2])
            self.option[1].config(text=self.questlist[self.index][3])
            self.option[2].config(text=self.questlist[self.index][4])
            self.option[3].config(text=self.questlist[self.index][5])
            
            
        
        def Next():
            """the method for navigating the questions forward"""
            if self.index <len(self.questlist)-1:
                self.index+=1
                self.answer.set(self.choosedans[self.index])
                
            else:
                app.bell()
                
                
                
                print(self.correctans,"correctans")#printing the correct answer's list
                print(self.choosedans,"choosed ans")#printing the choosed answer's list
                
            self.num.set("%d."%(self.index+1))#setting the numberings for the questions
            self.question.set(self.questlist[self.index][1])
            self.option[0].config(text=self.questlist[self.index][2])
            self.option[1].config(text=self.questlist[self.index][3])
            self.option[2].config(text=self.questlist[self.index][4])
            self.option[3].config(text=self.questlist[self.index][5])
            #self.answer.set("")
            
            
            
        def Save():
            """printing the result of the test"""
            self.result=0
            #########
            sub=askyesno(message="Are you sure you want to submit?")
            if sub:
                for i in range(len(self.correctans)):
                    if (self.correctans[i]==self.choosedans[i]) and (self.choosedans[i]!=""):
                        self.result+=1#incrementing the score
                self.finalResult=(self.result/len(self.questlist))*100#converting the score to percentsge
                self.FinalText=r"Your result is %.0f percent"%(self.finalResult)#the result text
                self.finalResultLabel.config(text=self.FinalText)#putting the result on the final page
                self.FinalFrame.pack(side="top",expand="yes",fill="both")
                self.TestFrame.pack_forget()
                app.title("Result Page")


        #the frame for the buttons on the test page
        butframe=frames(self.TestFrame,"left",fill="x")
        butlist=["Prev","Next"]
        butcommand=[Prev,Next]
        butimages=[previousimg,forwardimg]
        imagePosition="left"
        index=0
        for i in butlist:
            but=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound=imagePosition)
            but.pack(side="left",padx=8)
            index+=1
            imagePosition="right"

        #designing the submit button
        submitbut=Button(butframe,style="TButton",width=7,command=Save,text="Submit",image=submitimg,compound="left")
        submitbut.pack(side="right",anchor="w",padx=450)
    
    def Answer(self):
        """method for the answer"""
        self.correctans[self.index]=self.questlist[self.index][6]#adding the correct answers to the list of correct answers
        self.choosedans[self.index]=self.answer.get()#addind the chosen answers to the choosedans list
        
        
    def CreateFrame(self):
        """this method creates all the frames for the application"""
        self.LoginFrame=frames(self.master,"top",expand="yes",fill="both")
        self.RegFrame=frames(self.master,"top",expand="yes",fill="both")
        self.RegFrame.pack_forget()
        self.TestFrame=frames(self.master,"top",expand="yes",fill="both")
        self.TestFrame.pack_forget()
        self.FinalFrame=frames(self.master,"top",expand="yes",fill="both")
        self.FinalFrame.pack_forget()
                             
    def Here(self):
        """method that navigates to the navigation page"""
        self.RegFrame.pack(side="top",expand="yes",fill="both")
        self.LoginFrame.pack_forget()
        self.label.config(text="")
        app.title("Registration page")
    def Clear(self):
        """for clearing the entries"""
        self.user.set("")
        self.passw.set("")
        self.choice.set("")
        self.label.config(text="")
        
    def Login(self):
        """method for login in to the test page"""
        a=self.user.get()
        b=self.passw.get()
        c=self.choice.get()
        mins=29;sec=59#the minute and second for the timer of the cbt app
        if a!="" and b!="" and c!="":
            try:
                conn=lite.connect("cbtapp.db")
                cur=conn.cursor()
                details=cur.execute('select * from userdetails')
                sub=conn.execute("select * from subjecttab")
                for j in sub:
                    if c==j[1]:
                        break
                for i in details:
                    if a==i[1] and b==i[2]:
                        if c==j[1]:
                            questions=conn.execute("select * from %s"%c)#getting the questions from the database
                            self.TestFrame.pack(side="top",expand="yes",fill="both")
                            self.LoginFrame.pack_forget()

                            #timer of the application
                            self.val=Timer(self.lablist[1],29,59)#calling the timer class
                            self.val.timer()#calling the timer method

                            self.userlist[1].config(text=self.user.get().capitalize())#displaying the cAPITALIZE FORMAT OF THE USERNAME
                            self.Clear()#calling the clear method to clear all entries
                            app.title("Test Page")
                            self.questlist=questions.fetchall()#getting the questions from the database
                            shuffle(self.questlist)#shuffling the questions from the database

                            #CREATING AN EMPTYLIST FOR THE ANSWERS
                            self.choosedans=[]
                            self.correctans=[]
                            for i in range(len(self.questlist)):
                                self.choosedans.append("")
                                self.correctans.append("")
                            
                            
                                
                            
                            self.num.set("%d."%(self.index+1))#number for the questions
                            self.question.set(self.questlist[0][1])#initialising the question label with a question
                            self.option[0].config(text=self.questlist[0][2])#initialising the option A  with an option
                            self.option[1].config(text=self.questlist[0][3])#initialising the option B  with an option
                            self.option[2].config(text=self.questlist[0][4])#initialising the option C  with an option
                            self.option[3].config(text=self.questlist[0][5])#initialising the option D  with an option
                            
                            
                            
                        else:
                            self.label.config(text="Subject not in database")
                    else:
                        self.label.config(text="Invalid username or password")
            except:
                self.label.config(text="Subject not in Database")
        else:
            self.label.config(text="One or more entries empty")

    def Home(self):
        """navigating back to the home page"""
        self.FinalFrame.pack_forget()
        self.label.config(text="")
        #initializing the answer choice
        self.answer.set("")
        app.title("CBT Application")
        self.val.reset(29,59)#reseting timer
        self.index=0
        self.LoginFrame.pack(side="top",expand="yes",fill="both")
        
    def FinalPage(self):
        #"""the method that designs the result page"""
        #frame for the header
        headerFrame=frames(self.FinalFrame,"top")

        
        headerLabel=Label(headerFrame,style='header.TLabel',text='\t\t\t\t\tResult',justify='center',width=100)
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')
        #####end of the header######
        
        
        self.finalResultLabel=Label(self.FinalFrame,style="TLabel",width=50)#displaying the score on a label
        self.finalResultLabel.pack(side="left",anchor="n",padx=20,pady=40)

        #the home button on the result page
        homeButton=Button(self.FinalFrame,style="TButton",width=5,text="Home",command=self.Home)
        homeButton.pack(side="right",anchor="ne",padx=5)
    
    
    def Close(self):
        """method that closes the application"""
        msg=askyesno(title="EXIT?",message="Are you sure you want to exit this app ?")
        if msg:
            app.destroy()

        
    
class SplashScreen(frame):
    """class that performs the splash screen"""
    def __init__(self,master):
        """init method"""
        frame.__init__(self,master)
        self.master=master
        self.SplashPage()

    def SplashPage(self):
        """splash page"""
        self.splashframe=Frame(self.master,style="TFrame")
        self.splashframe.pack(side="top",expand="yes",fill="both")
        label=Label(self.splashframe,style="TLabel",width=100,image=splashimg,compound="top",text="Loading...")
        label.pack(side="top")

        #creating an instance of the progress bar
        self.progress=Progressbar(self.splashframe,style="TProgressbar",length=200,mode="determinate",maximum=100)
        self.progress.pack(side="top")
        self.progress.start(50)#starting the progress bar
        self.splashframe.after(6000,self.Homepage)#calling the cbt class

    def Homepage(self):
        """moving to the home page"""
        self.splashframe.pack_forget()
        self.progress.stop()#stopping the progressbar
        Cbt(app)

SplashScreen(app)
app.mainloop()

