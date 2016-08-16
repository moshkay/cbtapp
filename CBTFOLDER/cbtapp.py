#A CBT application using python
#####################################################about the app##############################################################################################
__author__="DaVinci kay"
__authoremail__="kayzeebiz@gmail.com"
__project__="A Computer base application"
__description__="""this application is a computer base test application"""
__date__="11-03-2013"
__version__="version 1.0"

#################################################################################################################################################################
#import external modules
from tkinter import *

#these are functions for the widgets for calling in the main prog.


def label(mas,text,bgcol,fgcol,hei,wid,ro,col,fontsize,colspan,img=None,com=None):
    """Function for the Label widget"""
    lab=Label(mas,text=text,height=hei,width=wid,bg=bgcol,fg=fgcol,padx=10,pady=10,font=("Verdana",fontsize,"bold"),image=img,compound=com)
    lab.grid(row=ro,column=col,sticky=N,columnspan=colspan,padx=4,pady=4)
def button(mas,text,bgcol,fgcol,hei,wid,ro,col,x,y,command=None):
    """Function for the Button widget"""
    but=Button(mas,text=text,bg=bgcol,fg=fgcol,height=hei,width=wid,font=("Arial black",10,"bold"),relief=FLAT,bd=4,pady=2,padx=2,command=command)
    but.grid(row=ro,column=col,padx=x,pady=y)
#end global functions def

app=Tk()
app.title("DaVinci CBT app")
app.geometry('600x600+300+70')
app.config(bg="steelblue")
app.resizable(False,False)
#starting the object
class CbtApp(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        self.create_header()
        self.create_checkboxes()
        self.create_button()
        


    def create_header(self):
        text="""1. What is the largest inland lake in South America?\n."""
        label(self.master,"DAVCOMTEST CBT SOFTWARE","steelblue","#bbdefb",5,40,0,0,15,10)
        questbox=Label(self.master,bg="#bbdefb",fg="steelblue",font=("Verdana",10),text=text,height=10,width=60,padx=2,pady=2)
        questbox.grid(row=1,column=0,columnspan=10,rowspan=5)

    def create_checkboxes(self):
        #creating a frame inside the interface
        self.mid=Frame(self.master,height=10,width=60,padx=2,pady=2,bg="steelblue")
        self.mid.grid(row=6,column=0,columnspan=10,rowspan=4,pady=5)

        #initialising the values of the radiobuttons
        options="ABCD"
        opt=["A. the answer here is Ontario","B. oHn uhs","C. Titicaca","D  Amazon",]
        c=0;r=0
        val=StringVar()

        for i in options:#creating the radiobuttons
            check=Radiobutton(self.mid,height=2,width=60,fg="#bbdefb",font=("verdana",10,"bold")\
                              ,bg="steelblue",text=opt[r],variable=val,value=i,indicatoron=1,activebackground="#bbdefb",activeforeground="steelblue")
            check.grid(row=r,column=c,pady=1)
            r+=1

    def create_button(self):
        buts=["Previous","Next","Submit"]
        r=11;c=0

        for i in buts:
            button(self.master,i,"#bbdefb","steelblue",1,6,r,c,2,2)
            c+=1
            if i=="Next":
                c+=5
    def Next(self):
        pass
    def Previous(self):
        pass
    def submit(self):
        pass
            
        
        
        
            






        
CbtApp(app) 
app.mainloop() 
