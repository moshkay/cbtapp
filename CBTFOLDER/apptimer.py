#the timer for my cbt app
mins=29;sec=59

def timer(lab1,submit=None):
    def count():
        global mins,sec
        sec-=1
        if sec==0:
            mins-=1
            sec=59
        if mins==0 and sec==0:
            app.destroy()
        else:
            lab1.config(text="%2d : %2d"%(mins,sec))
            lab1.after(1000,count)
    count()
        
       
