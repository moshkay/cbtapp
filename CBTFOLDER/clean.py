 ####creating the Database clean frame and designing the widgets on the page#####
        self.cleandatabaseFrame=frames(self.master,'top')
        self.cleandatabaseFrame.pack_forget()#removing the clean database out of the
        #the header label for the cleandata page
        headerLabel=Label(self.cleandatabaseFrame,style='header.TLabel',width=100,text='\t\t\t\t\tDatabase Cleanup',justify='center')
        headerLabel.pack(side='top',padx=2,pady=5,fill='x')

        label=Label(self.cleandatabaseFrame,style='TLabel',text="How many Subjects do you want to clean?",width=50)
        label.pack(side="top")
        #entry variable
        self.subjectvar=StringVar()

        #entry on clean database
        entframe=frames(self.cleandatabaseFrame,"top",)
        entry=Entry(entframe,width=20,style="TEntry",textvariable=self.subjectvar)
        entry.pack(side='left')
        

        label=Label(self.cleandatabaseFrame,style='TLabel',text="Enter the Subjects below:",width=50)
        label.pack(side="top")

        entframe=frames(self.cleandatabaseFrame,"top",)
        entframe.pack(side='top')

       


        def entrycreate(event):
            """creating the entries"""
            try:
                val=int(self.subjectvar.get())
                
                entframe=frames(self.cleandatabaseFrame,"top",)
                entframe.pack(side='top')
                if val<=5:
                    for i in range(val):
                       
                        entry=Entry(entframe,width=20,style="TEntry")
                        entry.pack(side='top',pady=10)
                    
                        
            except:
                pass
        
        #binding the function to the above entry
        entry.bind("<Any-KeyRelease>",entrycreate)
