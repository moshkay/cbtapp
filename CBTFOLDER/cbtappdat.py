#this applet is for the admin to add data into the database
#####################################################about the app##############################################################################################
__author__="DaVinci kay"
__authoremail__="kayzeebiz@gmail.com"
__project__="A Computer base application Admin"
__description__="""this application is a computer base test application"""
__date__="11-03-2013"
__version__="version 1.0"

#################################################################################################################################################################

from tkinter import *
import sqlite3 as lite

app=Tk()
app.title("DaVINCICBT ADMIN PORTAL")
app.config(bg="steelblue")
app.geometry("600x500+320+100")
app.resizable(False,False)



#creating the object
class CbtApp(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        self.create_header()
        self.create_button()


    def create_header(self):
        """creating tjhe labels and the entries"""
        #creating the header label
        header=Label(self.master,text="DaVinciCBT Admin portal",bg="steelblue",fg="#bbdefb",height=1,width=20,font=("verdana",15,"bold"))
        header.grid(row=0,column=0,columnspan=10,padx=2,pady=2)
        #vreating the warning label
        self.label=Label(self.master,bg="steelblue",fg="#ff0000",font=("verdana",10,"bold"),height=1,width=30,padx=2,pady=2)
        self.label.grid(row=7,column=1,columnspan=3)
        #creating the list for the labels
        labellist=["Question:","option A:","option B:","option C:","option D:","ANSWER:"]
        row=1

        #initialisin the variables for the entries
        self.questVar=StringVar()
        self.aVar=StringVar()
        self.bVar=StringVar()
        self.cVar=StringVar()
        self.dVar=StringVar()
        self.ansVar=StringVar()
        varlist=[self.questVar,self.aVar,self.bVar,self.cVar,self.dVar,self.ansVar]

        #creating the questiion entry using the text widget
        self.quest=Entry(self.master,bg="#bbdefb",fg="steelblue",font=("verdana",10),width=50,textvariable=self.questVar)
        self.quest.grid(row=1,column=1,padx=2,pady=2)

        #creating the labels using the items in the labellist
        for i in labellist:
            lab=Label(self.master,text=i,bg="steelblue",fg="#bbdefb",height=2,width=10,font=("verdana",10,"bold"))
            lab.grid(row=row,column=0,padx=2,pady=2)
            
            if row>=2:
                #creating entries excluding the question label
                ent=Entry(self.master,font=("verdana",10,"bold"),width=40,bg="#bbdefb",fg="steelblue",justify=CENTER,relief=SUNKEN,textvariable=varlist[row-1])
                ent.grid(row=row,column=1,padx=2,pady=2)
            row+=1
    def create_button(self):
        """creating the update button"""
        but=Button(self.master,text="Update",bg="#bbdefb",fg="steelblue",activebackground="#bbdefb",height=1,width=7,relief=FLAT,padx=2,pady=2,font=("verdana",10),command=self.update)
        but.grid(row=7,column=0,padx=2,pady=2)
        
    def update(self):
        """creating the update"""
        if self.questVar.get()!="" and self.aVar.get()!="" and self.bVar.get()!="" and self.cVar.get()!="" and self.dVar.get()!="" and self.ansVar.get()!="":
            #connecting to the database
            conn=lite.connect("cbtapp.db")
            with conn:
                cursor=conn.cursor()
                cursor.execute("""INSERT INTO cbtdat VALUES(null,?,?,?,?,?,?)""",(self.questVar.get(),self.aVar.get(),self.bVar.get(),self.cVar.get(),self.dVar.get(),self.ansVar.get()))
                conn.commit()
                self.label.config(text="")
        else:
            self.label.config(text="Error: one or more entry is empty")
    
            
            
        



CbtApp(app)
app.mainloop()



