from tkinter import * #tkinter module
from tkinter.ttk import Combobox #for comobox
import tkinter as ttk  #using as ttk
import random  #import random
from abc import ABC,abstractmethod #abstract base class

# DESTROYER

class destroyer:
        # This file is used as composition in "MIDDLE" when timer become equal to zero then create an object and then this function has been called and it destryos all label and display score and writes indivisual score of every player
        def destroying_scoreshowing(self):
            f=open('myfile','a')
            f.write(" "+"Score: "+str(middle.score)) 
            f.close()
            
            middle.fontLabel3.destroy()# Destroyes Difficulty Level
            middle.entry2.destroy() # Destroy Combobox
            middle.button2.destroy() # Destroy Set button
            middle.fontLabel4a.destroy() # Destroyes Score
            middle.fontLabel5.destroy() # Destroy Time Left
            middle.fontLabel5a.destroy()

            
            middle.fontLabel6.config(text=middle.score)
            middle.fontLabel6.place(x=270,y=300)
            middle.fontLabel4.config(text="score",font=("Times", "40", "bold italic"),bg= 'black',fg='white',width=10)
            middle.fontLabel4.place(x=250,y=200)
            
            middle.entry3.destroy()





# MIDDLE

class middle(ABC):

    score=0
    timer1=60 # for difficulty level Basic
    timer2=45 # for difficulty level Normal
    timer3=20 # for difficulty level Hard

   


    def timer(*args):  # STATIC METHOD
        middle.entry3.focus_set() # Set focus to the entry from where we take input
        middle.fontLabel7.destroy() # Destroyes Tab
        
        if middle.entry2.get()=="Basic":# Check if time is equal 0 then it call the destroyer previous function.
             if middle.timer1==0:
                 r=destroyer()
                 r.destroying_scoreshowing() 
                 

             else:
        # Else call this function again to minimize time and update label of time.
                middle.timer1-=1
                middle.fontLabel5a.config(text=middle.timer1)
                middle.fontLabel5a.after(1000,middle.timer) #1000 for 1 Seconds

        elif middle.entry2.get()=="Normal":
        # Check if time is equal 0 then it call the destroyer previous function.
            if middle.timer2==0:
                r=destroyer()
                r.destroying_scoreshowing()

                

            else:
        # Else call this function again to minimize time and update label of time.
                middle.timer2-=1
                middle.fontLabel5a.config(text=middle.timer2)
                middle.fontLabel5a.after(1000,middle.timer)

        elif middle.entry2.get()=="Hard":
        # Check if time is equal 0 then it call the destroyer previous function.
            if middle.timer3==0:
                r=destroyer()
                r.destroying_scoreshowing()
               

            else:
        # Else call this function again to minimize time and update label of time.
                middle.timer3-=1
                middle.fontLabel5a.config(text=middle.timer3)
                middle.fontLabel5a.after(1000,middle.timer)


    def update_label(*args):
            # When we set our difficulty level then this method has been called and sets time according to user difficulty level and disabled the combobox
            if middle.entry2.get()=="Basic":
                middle.fontLabel5a.config(text=middle.timer1)
                middle.entry2.config(state=DISABLED)

            if middle.entry2.get()=="Normal":

                middle.fontLabel5a.config(text=middle.timer2)
                middle.entry2.config(state=DISABLED)

            if middle.entry2.get()=="Hard":
                middle.fontLabel5a.config(text=middle.timer3)
                middle.entry2.config(state=DISABLED)
                    
          
            
    
    def get_input(*args):
        # This method binds with Enter Key and matches our typed word with above word if that word found to be equal then it adds score and shuffle the word again to display new word
        
        if middle.entry3.get()==middle.word[0]:
            middle.score+=1
            middle.fontLabel4a.config(text=middle.score)   
        else:
            pass

        random.shuffle(middle.word)
        middle.entry3.delete(0,END)
        middle.fontLabel6.config(text=middle.word[0])




# NEW BASE

    @abstractmethod
    def new_base(self):
    # This is abstract method and we call it through method overrinding in start Class
    # Sets Timer label, Entry box , Set combobox for difficulty , Score Label , Words appear
        middle.word=['abandoned' , 'abc', 'aberdeen', 'abilities', 'ability', 'able', 'aboriginal', 'abortion', 'about', 'above', 'abraham', 'abroad',  'absence', 'absent', 'absolute', 'absolutely', 'absorption', 'abstract', 'abstracts',  'abuse', ' academic', 'academics', 'academy' , 'accent', 'accept', 'acceptable', 'acceptance', 'accepted', 'accepting','accepts', 'access', 'accessed', 'accessibility', 'accessible', 'accessing', 'accessories', 'accessory', 'accident', 'accidents', 'accommodate', 'accommodation', 'accommodations', 'accompanied' ,'accompanying', 'accomplish', 'accomplished', 'accordance', 'according', 'accordingly', 'account']

        middle.fontLabel3=Label(self.root,text="Difficulty Level",font=("Times", "22", "bold italic"),bg= 'black',fg='white')
        middle.fontLabel3.place(x=30,y=430)

        middle.entry2=Combobox(self.root,values=['Basic','Normal','Hard'])
        middle.entry2.place(x=30,y=470)
        middle.entry2.focus_set()

        middle.button2=Button(self.root,text="Set",bd=5,fg="white",bg="black",padx=1,pady=2,font=("Times", "15", "bold italic"),width=5,command=middle.update_label)
        middle.button2.pack()
        middle.button2.place(x=250,y=460)
        

        
        
        middle.fontLabel4=Label(self.root,text="Points",font=("Times", "25", "bold italic"),bg= 'black',fg='white')
        middle.fontLabel4.place(x=90,y=110)
        
        middle.fontLabel4a=Label(self.root,text=middle.score,font=("Times", "25", "bold italic"),bg= 'black',fg='white')
        middle.fontLabel4a.place(x=120,y=160)

        middle.fontLabel5=Label(self.root,text="Time Left",font=("Times", "25", "bold italic"),bg= 'black',fg='white')
        middle.fontLabel5.place(x=580,y=110)


        middle.fontLabel5a=Label(self.root,text=0,font=("Times", "25", "bold italic"),bg= 'black',fg='white')
        middle.fontLabel5a.place(x=620,y=160)


        middle.fontLabel6=Label(self.root,text=middle.word[0],font=("Times", "30", "bold italic"),bg= 'black',fg='white',width=13)
        middle.fontLabel6.place(x=250,y=210)

        middle.fontLabel7=Label(self.root,text="TAB to start timer",font=("Times", "15", "bold italic"),bg= 'black',fg='white')
        middle.fontLabel7.place(x=560,y=505)

        middle.entry3=Entry(self.root,font=("Times", "18", "bold italic"),bd=3,bg='white',fg='black',width=15)
        #it calls get input method and timer function it binds with two keys
        self.root.bind('<Return>',self.get_input) and self.root.bind('<Tab>',self.timer)

        
        
        middle.entry3.place(x=300,y=270)

        
        
        

   

        

# START        
        
class start(middle):
    
    def __init__(self):
        start.f=open('myfile','a') #Opens file
        self.root=Tk()  #tkinter root
 
#Destroy Labels
        
    def new_base(self): #Calling middle class abstract method New_base()
            super().new_base() 
            
    def destroy(self): #Destroying labels for Name,title,Entry box and Start button when Start button pressed
        self.fontLabel.destroy()
        self.fontLabel2.destroy()
        self.entry1.destroy()
        self.button.destroy()

        self.new_base()  #calling new_base fucntion of start class
        
# ENTER DATA IN LIST

    def data(self):  #writes the name of user in file and if user dont enter name it sets it to UNKNOWN by default using exception handling
            try:
                    a=self.entry1.get()
                    if a=="":
                            a="unknown"
                            

                    else:
                            pass
            except:
                    start.f.write("\n"+"Name: "+self.entry1.get())
                    start.f.close()
                    self.destroy() #Calling destroying function to destroy labels

            else:
                   start.f.write("\n"+"Name: "+a)
                   start.f.close()
                   self.destroy() #Calling destroying function to destroy labels
# CREATING THINGS
                   
    def base(self):
        self.root.geometry('800x533+290+150') #root.geometry("resolution+x-axis+y-axis")
        self.root.title('Speed Typing Game') #root.title("any text")
    
        frame=Frame(self.root,bg='red') 
        frame.pack(fill=BOTH,expand=True)
        image=PhotoImage(file='pic.gif') #setting image
        label=ttk.Label(frame,image=image)
        label.pack(fill=BOTH,expand=TRUE)

        self.fontLabel=Label(self.root,text="Welcome Speed Typing Master...",font=("Times", "22", "bold italic"),bg= 'black',fg='white') #Label(root,text="any text",font=(),bg="")
        self.fontLabel.place(x=180,y=90) #x and y cordinates where we want to place
 
        self.fontLabel2=Label(self.root,text="Name",font=("Times", "22", "bold italic"),bg= 'black',fg='white')
        self.fontLabel2.place(x=180,y=150)

        self.entry1=Entry(self.root,font=("Times", "15", "bold italic"),bd=0,bg='white',fg='black',width=12)
        self.entry1.place(x=270,y=156)
        self.entry1.focus_set() #automatically set the cursor to typing box ,This takes name as input

        self.button=Button(self.root,text="Start",bd=5,fg="white",bg="black",padx=1,pady=2,font=("Times", "22", "bold italic"),command=self.data) #calling data Function.
        self.button.pack()
        self.button.place(x=350,y=210)

     
        self.root.mainloop()


        

#MAIN PROGRAM
        
s=start() #object of class start
s.base() #calling base fucntion of start class
