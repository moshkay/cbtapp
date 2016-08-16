#A CBT application using python
#####################################################about the app##############################################################################################
__author__="DaVinci kay"
__authoremail__="kayzeebiz@gmail.com"
__project__="An Admin for a Computer base test application"
__description__="""this application is a computer base test application"""
__date__="27-03-2016"
__version__="version 1.0"

#################################################################################################################################################################

#platform for the admin page for the
try:
    import tkinter
    from tkinter import Menu,Frame as frame
    from tkinter import StringVar,IntVar,Tk,PhotoImage
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import sqlite3 as lite
    from re import *
    
except ImportError:
    print("An error occured while importing a module")





app=Tk()
#for the big srceen
app.geometry("1355x730+0+0")
app.resizable(False,False)
app.config(bg="#ffffff")
app.title("Admin login page")
app.iconname("CBT ADMIN")



#the  styles for the widgets
style=Style()
style.theme_use("clam")
#print(style.theme_names())
style.configure('TLabel',background="#ffffff",foreground="steelblue",font=("Verdana",12,'bold'))
style.configure('TEntry',background="#ffffff",foreground="black",font=("Verdana",12,'bold'))
style.configure('TCombobox',background="#ffffff",foreground="steelblue",font=("Verdana",15))
style.configure('TButton',background='steelblue',foreground='#ffffff',activebackground="#22ff00",font=("Verdana",15,"bold"))
style.configure('header.TLabel',background='steelblue',foreground='#ffffff',width=20,font=("Verdana",15,"bold"))
style.configure('TFrame',background="#ffffff")
style.configure('link.TButton',background="#ffffff",foreground="steelblue",activeforeground="pink",font=('Verdana',12,'bold'),borderwidth=0,padx=0)
style.configure('warn.TLabel',background="#ffffff",foreground="red",font=("Verdana",12,'bold'))
style.configure("TRadiobutton",background="#ffffff",foreground="steelblue",font=("Verdana",12,"bold"))
#fucntion for the frame
def frames(parent,side,expand=None,fill=None,anchor=None,bd=None,hei=None,wid=None):
    frame_name=Frame(parent,style='TFrame',borderwidth=bd,height=hei,width=wid)
    frame_name.pack(side=side,expand=expand,anchor=anchor,fill=fill)
    return frame_name

##############images for the application###################
addimg=PhotoImage(file="Add.png")
correctimg=PhotoImage(file="Check.png")
wrongimg=PhotoImage(file="Delete.png")
deleteimg=PhotoImage(file="Remove.png")
nothingimg=PhotoImage(file="nothing.png")
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
updateimg=PhotoImage(file="update.png")

################end of images########################

class admin(frame):

    #the object of the admin
    def __init__(self,master):
        frame.__init__(self,master)
        self.master=master
    
        #calling the methods
        self.createLabel()
        self.createEntry()
        self.createButton()
        self.AdminDetailsChangePage()
        self.AdminPage()
        self.Database()
        self.CreateMenu()
        

       


    def createLabel(self):
        #frame for the admin login page
        self.AdminLoginPage=Frame(self.master,style='TFrame',width=600,height=600)
        self.AdminLoginPage.pack(side='top',anchor="center",fill='both',expand='yes')

        
        #the header frame
        headerFrame=Frame(self.AdminLoginPage,style='TFrame')
        headerFrame.pack(side='top',anchor='n',fill='x',padx=2,pady=2)

        #the list for the labels
        headerLabel=Label(headerFrame,style='header.TLabel',text='\t\t\t\t\tAdmin Login Page',justify='center')
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        #label for the image
        imageLabel=Label(headerFrame,style='TLabel',text='',justify='center',width=100,image=headerimg,compound="center")
        imageLabel.pack(side='top',padx=30,pady=5,fill='x')

        #guiding text for the label
        text="Enter your username and password to login to the admin section"
        #guiding label
        label=Label(headerFrame,style='TLabel',text=text,width=60)
        label.pack(side='top',pady=5,padx=5)

    def createEntry(self):
        """this creates entries and the labels"""
        #string variables for the entries
        self.user=StringVar()
        self.passw=StringVar()

        var=[self.user,self.passw]

        #list for the labels and list
        lab=[("Username :","Username"),("Password :",'Password')]

        #list for the images
        images=[userimg,passwordimg]

        #creating the labels and entries
        index=0
        for i in lab:
            entframe=Frame(self.AdminLoginPage,style="TFrame")
            entframe.pack(side="top",anchor="center",pady=30)

            label,ent= i
            label=Label(entframe,style="TLabel",width=13,text=label,image=images[index],compound="left")
            label.pack(side='left',anchor='center',pady=2)
            ent=Entry(entframe,style="TEntry",width=30,textvariable=var[index])
            ent.pack(side='left',anchor="center",pady=2)
            index+=1
        ent.config(show='*')
            
           
        #warning label
        self.label=Label(self.AdminLoginPage,style="warn.TLabel",width=40)
        self.label.pack(side='top')
        

    def createButton(self):
        """creating buttons on page"""
        butlist=['Clear','Login','Close']
        butcommand=[self.Clear,self.Login,self.Close]
        butimages=[refreshimg,loginimg,logoutimg]
        index=0

        #creting the buttons
        butframe=frames(self.AdminLoginPage,'top')#frame for the button

        for i in butlist:
            i=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound="left")
            i.pack(side='left',padx=5,pady=5)
            index+=1

        #changing password
        butframe=frames(self.AdminLoginPage,"top")#frame for the button

        text="if you want to change your password and username click "#text for the label
        label=Label(butframe,style='TLabel',width=46,text=text)
        label.pack(side='left',pady=9)
        #link button
        but=Button(butframe,style='link.TButton',text="here",width=4,command=self.Here)
        but.pack(side='left')


    def AdminDetailsChangePage(self):
        self.AdminChange=Frame(self.master,style="TFrame")
        self.oldUser=StringVar()
        self.newUser=StringVar()
        self.oldpass=StringVar()
        self.newpass=StringVar()
        self.renewpass=StringVar()

        #header for the admin change page
        headerLabel=Label(self.AdminChange,style='header.TLabel',text='\t\t\t  \tAdmin Details Changing Page',justify='center')
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        #label for the image
        imageLabel=Label(self.AdminChange,style='TLabel',text='',justify='center',width=100,image=headerimg,compound="center")
        imageLabel.pack(side='top',padx=30,pady=5,fill='x')

        #variable list
        varlist=[self.oldUser,self.newUser,self.oldpass,self.newpass,self.renewpass]

        #list for the images
        images=[userimg,passwordimg]
        
        #label and entry list
        lablist=[("Old username :",""),("New Username :",""),("Old Password :",""),("New Password",""),("Re-enter Password :","")]
        #creating the labels and entries
        index=0;imageindex=0
        for i in lablist:
            label,entry=i
            entframe=frames(self.AdminChange,'top')
            label=Label(entframe,text=label,style="TLabel",width=20,image=images[imageindex],compound="left")
            label.pack(side='left',padx=5,pady=15)
            ent=Entry(entframe,textvariable=varlist[index],style="TEntry",width=20)
            ent.pack(side="left",padx=5,pady=15)

            if index==1:
                imageindex+=1#incrementing the vakue of imageindex

            index+=1
        self.warnlab=Label(self.AdminChange,style="warn.TLabel",width=40)#warning label
        self.warnlab.pack(side="top",padx=10,pady=4)

        #creating the buttons on the admin change page
        butlist=['Prev','Submit','Close']
        butcommand=[self.Prev,self.Submit,self.Close]
        butimages=[previousimg,submitimg,logoutimg]
        index=0

        #creating the buttons
        butframe=frames(self.AdminChange,'top')#frame for the button

        for i in butlist:
            i=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound="left")
            i.pack(side='left',padx=5,pady=5)
            index+=1

    def Here(self):
        """navigation to the changing of details page"""
        app.title("Admin Details Change")
        self.AdminLoginPage.pack_forget()
        self.AdminChange.pack(side='top',expand='yes',fill='both')

    def Prev(self):
        app.title("Admin login")
        self.AdminChange.pack_forget()
        self.AdminLoginPage.pack(side='top',expand='yes',fill='both')
        
        


    def Submit(self):
        """the changing of admin details"""
        a=self.newUser.get()
        b=self.oldUser.get()
        c=self.newpass.get()
        d=self.oldpass.get()
        e=self.renewpass.get()
        
        if a!="" and b!="" and c!="" and d!="" and e!="":
            if c==e:
                try:
                    conn=lite.connect("cbtapp.db")
                    details=conn.execute("select * from admindetails")
                    for i in details:
                        if b==i[1] and d==i[2]:
                            with conn:
                                conn.execute("""update admindetails set username=?,password=? where (username=? and password=?)""",(a,c,b,d))
                            conn.commit()
                            self.warnlab.config(text="username and password changed\nsuccessfully")
                            break
                    else:
                        self.warnlab.config(text="wrong user or password")
                    conn.close()
                            
                except:
                    self.warnlab.config(text="An error occured while\n changing username and password")
            else:
                self.warnlab.config(text="Error: passwords dont match")
        else:
            self.warnlab.config(text="Error: one or more entries empty")

    
        

    def Clear(self):
        """for clearing the entries"""
        self.user.set("")
        self.passw.set("")
        self.label.config(text="")

    def Close(self):
        msg=askyesno(title="EXIT?",message="Are you sure you want to exit this app ?")
        if msg:
            app.destroy()

    def Login(self):
        """Login in to page"""
        conn=lite.connect("cbtapp.db")
        cursor=conn.cursor()
        cursor.execute("""select * from admindetails""")
        b=cursor.fetchall()
        #checking if the entry value are in the database
        #using regular expression to validate
        space=compile(r'^[ ]*$')
        #checking if it is empty
        empty1=space.match(self.user.get())
        empty2=space.match(self.passw.get())
    
        for i in b:
            if (self.user.get() == i[1]) and (self.passw.get() == i[2]):

                self.AdminLoginPage.pack_forget()
                self.PageAdmin.pack(side='top',expand='yes',fill='both')
                
                self.label.config(text="")
            elif not(self.user.get() == i[1]) or not(self.passw.get() ==i[2]):
                try:
                    empty1.group()
                    empty2.group()
                    self.label.config(text="Error: one of the entries contains spaces or empty")
                except:
                    self.label.config(text="Error: wrong username or password")
        conn.close()

    def AdminPage(self):
        """this designs the admin page"""
        self.PageAdmin=Frame(self.master,style="TFrame")

        #header for the admin change page
        headerLabel=Label(self.PageAdmin,style='header.TLabel',text='\t\t\t\t\tAdmin Page',justify='center')
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        #frames for the radiobuttons and entries
        self.choice=IntVar()#the variable for the radiobuttons
        radioFrame=frames(self.PageAdmin,"left",anchor='n')
        entryFrame=frames(self.PageAdmin,"left",anchor='ne',expand="yes")

        #creating the label
        labelRadio=Label(radioFrame,style="TLabel",text="what would you want to do with the database?",width=50)
        labelRadio.pack(side="top")
        radlist=["Nothing","Update the questions","Add new subjects","Clean database"]

        #images for the radiobuttons
        radioImages=[nothingimg,updateimg,addimg,deleteimg]

        value=0

        for i in radlist:
            rad=Radiobutton(radioFrame,text=i,value=value,variable=self.choice,style='TRadiobutton',image=radioImages[value],compound="left")
            rad.pack(side='top',padx=2,pady=20,anchor='w')
            value+=1
        self.choice.set(0)

        #designing the entry widget
        labelRadio=Label(entryFrame,style="TLabel",text="Enter the following ",width=20)
        labelRadio.pack(side="top")

        self.subjectvar=StringVar()
        entframe=frames(entryFrame,'top')
        label=Label(entframe,text="Subject Name :",style="TLabel",width=20)
        label.pack(side='left',padx=5,pady=15)
        self.ent=Entry(entframe,textvariable=self.subjectvar,style="TEntry",width=20)
        self.ent.pack(side="left",padx=5,pady=15)

        entframe=frames(entryFrame,"top")
        label=Label(entframe,style="TLabel",width=10,text="Status :")
        label.pack(side='left',anchor='e')
        self.statlabel=Label(entframe,style="warn.TLabel",width=20,text="")
        self.statlabel.pack(side='left')
        #functions for the page admin
        def Prev():
            app.title("Admin Login")
            self.PageAdmin.pack_forget()
            self.AdminLoginPage.pack(side='top',expand='yes',fill='both')
        def Clear():
            self.subjectvar.set("")
            self.statlabel.config(text="")
        

        #button list
        butlist=["Prev","Clear","Next","Close"]
        butcommand=[Prev,self.Clear,self.Next,self.Close]
        butimages=[previousimg,refreshimg,forwardimg,logoutimg]

        index=0
        

        #creating the buttons
        butframe=frames(radioFrame,'right',anchor="sw",hei=20)#frame for the button
        for i in butlist:
            i=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound="left")
            i.pack(side='left',padx=5,pady=10)
            index+=1

        #creating the database edit frame
        self.DatabaseFrame=frames(self.master,'top')
        self.DatabaseFrame.pack_forget()
        
    
    def Next(self):
        """database operation"""
        value=self.subjectvar.get()
        if value!="":
            conn=lite.connect("cbtapp.db")
            cur=conn.cursor()
            if self.choice.get()==0:
                self.statlabel.config(text="you chose nothing")
                
            elif self.choice.get()==1:
                try:
                    b=cur.execute("""select * from %s"""%(value))
                    self.DatabaseFrame.pack(side='top',expand='yes',fill='both')
                    self.PageAdmin.pack_forget()
                    
                except:
                    self.statlabel.config(text="subject not in database")
                
                
                
                
            elif self.choice.get()==2:
                
                try:#adding subject to the database and verifying they've been there before
                    conn.execute("""create table %s (id INTEGER primary key autoincrement,question TEXT UNIQUE,A TEXT,B TEXT,C TEXT,D TEXT,Answer char(1))"""%(value))
                    self.statlabel.config(text="subject created successfully")
                    #adding the subject name i.e the name of the table to subjecttab table
                    conn.execute("""insert into subjecttab values(null,?)""",(value,))
                    conn.commit()
                except ImportError:
                    self.statlabel.config(text="subject already in the\n database")
                
            elif self.choice.get()==3: 
                try:#deleting subjects and verifying if they are in the database or not
                    conn.execute("""drop table %s"""%(value))

                    #removing the subject name i.e the name of the table to subjecttab table
                    conn.execute("""delete from subjecttab where subject=(?)""",(value,))
                    self.statlabel.config(text="subject successfully\n removed")
                    conn.commit()
                except lite.OperationalError:
                    self.statlabel.config(text="subject to be removed\n not in database",)
        
        else:
            self.statlabel.config(text="subject entry is empty")

    def Database(self):
        #designing the databaseframe
        #header for the admin change page
        app.title("updating questions")
        headerLabel=Label(self.DatabaseFrame,style='header.TLabel',text='\t\t\t\t\tUpdating Questions',justify='center',width=100)
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        #list for the labels and entries
        labelist=[["Questions :","questions"],["Option A :","Option A"],["Option B :","Option B"],["Option C :","Option C"],\
                  ["Option D :","Option D"],["Answer :","Answer"]]
        #initialisin the variables for the entries
        self.questVar=StringVar()
        self.aVar=StringVar()
        self.bVar=StringVar()
        self.cVar=StringVar()
        self.dVar=StringVar()
        self.ansVar=StringVar()
        varlist=[self.questVar,self.aVar,self.bVar,self.cVar,self.dVar,self.ansVar]
        index=0
        #creating the labels and entries
        for i in labelist:
            label,entry=i
            framentry=frames(self.DatabaseFrame,'top')
            lab=Label(framentry,style="TLabel",text=label,width=10)
            lab.pack(side="left",pady=20)
            ent=Entry(framentry,style="TEntry",textvariable=varlist[index],width=70)
            ent.pack(side="left",pady=20)
            index+=1
        lab=Label(self.DatabaseFrame,style="warn.TLabel",width=20)
        lab.pack(side="top",pady=20)

        #functions for the buttons
        def Prev():
            self.DatabaseFrame.pack_forget()
            self.PageAdmin.pack(side='top',expand='yes',fill='both')

        def Clear():
            self.questVar.set("")
            self.aVar.set("")
            self.bVar.set("")
            self.cVar.set("")
            self.dVar.set("")
            self.ansVar.set("")
            lab.config(text="")

        def Update():
            """adding to the database"""
            conn=lite.connect("cbtapp.db")
            cur=conn.cursor()
            a=self.questVar.get()
            b=self.aVar.get()
            c=self.bVar.get()
            d=self.cVar.get()
            e=self.dVar.get()
            f=self.ansVar.get()
            value=self.subjectvar.get()
            if a!="" and b!="" and c!="" and d!="" and e!="" and f!="":
                try:#adding question to the database and also verifying if it is already in the database
                    cur.execute("""insert into %s (question,a,b,c,d,answer) values(?,?,?,?,?,?)"""%(value),(a,b,c,d,e,f))
                    lab.config(text="question added")
                    conn.commit()
                    #clearing the values of the entries
                    Clear()
    
                except:
                    lab.config(text="the question is already\n in the database")
            else:
                lab.config(text="one or more entry empty")
            
                  
            
        

        #creating the buttons
        
        buttext=["Prev","Clear","Update",'Close']
        butcommand=[Prev,Clear,Update,self.Close]
        #images for the buttons
        butimages=[previousimg,refreshimg,updateimg,logoutimg]
        index=0
        #frame for the buttons
        butframe=frames(self.DatabaseFrame,'top')

        for i in buttext:
            but=Button(butframe,style="TButton",width=7,text=i,command=butcommand[index],image=butimages[index],compound="left")
            but.pack(side="left",padx=5,pady=10)
            index+=1
    def CreateMenu(self):
        """method that creates all the menus"""
        mainmenu=Menu(self.master,)
        save=Menu(self.master,tearoff=0)
        opens=Menu(self.master,tearoff=0)
        mainmenu.add_cascade(label="save",menu=save)
        mainmenu.add_cascade(label="open",menu=opens)
        app.config(menu=mainmenu)
                
            
        
        
        
        
        
        

#calling the class object
p=admin(app)
app.mainloop()
