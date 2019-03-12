
## CLASS 1##
import msvcrt
import time
import pickle
import os
import random
import sys
from Tkinter import*
import Tkinter as tk
lst_code=[1.1,1.2,1.2,1.3,1.4,1.5,2.1,2.2,2.3,2.4,3.1,3.2,3.3,3.4,4.1,4.2,4.3,4.4]

def counter():
    ctr=1
    f=open("\\details.dat",'rb')
    try:
        while True:
            obj=pickle.load(f)
            if obj:
                ctr+=1
            else:
                break
    except EOFError:
        pass

    f.close()

    reg=100+(ctr+1)
    return reg

    
class custdetails:

    def __init__(self):
        self.cname=" "
        self.cage=None
        self.cID=None
        self.caddress=" "
        self.cphno=None
    def enter_details(self):
        print
        print
        wel= "Please,let us know your details"
        print (wel)
        time.sleep(0.7)
        print
        self.cname=raw_input("What's your good name? : ")
        time.sleep(0.7)
        self.cage=input("how old are you? : ")
        time.sleep(0.7)
        self.caddress=raw_input("Where do you live? : ")
        time.sleep(0.7)
        self.cphno=input("Your phone number? : ")
        time.sleep(1)

        x= '''Thank You for your personal details!'''
        for i in range (0,len(x)):
            time.sleep(.01)
            print (x[i]),
            time.sleep(.01)
        print
        print
        
        time.sleep(1.5)
        wel='''  Don't worry, your details are in safe hands :-)'''
        for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
               
        time.sleep(.01)
        print
        print
        
        time.sleep(1.5)
        self.cID=counter()
        print ("Your unique customer ID is : ",self.cID)
        time.sleep(0.7)
        print
        print
        wel= "Remember it for next time whenever you visit us"
        print (wel)
        time.sleep(1.5)
        print
        print

        time.sleep(0.7)
        wel= "You are now one of our registered customers!"
        print (wel)
        
        time.sleep(1.5)
        print
        print
        time.sleep(0.7)  

    def showcustomer(self):
        s1=(15-len(str(self.cname)))*" "
        s2=(15-len(str(self.cage)))*" "
        s3=(20-len(str(self.caddress)))*" "
        s4=(10-len(str(self.cphno)))*" "
        print (self.cname,s1,self.cage,s2,self.caddress,s3,self.cphno,s4,self.cID)


###CLASS 2###
class bill:
    netbal=0
    def __init___(self):
        self.code=None
        self.name=" "
        self.cost=0
        self.price=0
        self.qnty=0
    def get(self):
        self.code=float(input("Enter the item code which you desire to buy : "))
        time.sleep(0.5)
        self.qnty=input("how much quantity of this item do you want to buy? : ")
        time.sleep(0.5)
        if self.code in lst_code:
            f1=open("F:\\PARUL\\PYTHON PROJECT\\price database.txt")
            f2=open("F:\\PARUL\\PYTHON PROJECT\\sales made.txt","a")
            list1=f1.readlines()
            for rec in list1:
                l2=rec.split('-')
                l=l2[0:3]
                if float(l[0])==self.code:
                    f2.write(rec)
                    self.name=l[1]
                    self.cost=int(l[2])
                    self.price=self.cost*self.qnty
                    bill.netbal+=self.price
            f1.close()
            f2.close()
               
        else:
            print "We are sorry ,but you made a wrong choice, :-("
    def display(self):
        s1=(24-len(str(self.name)))*" "
        s2=(14-len(str(self.cost)))*" "
        s3=(9-len(str(self.qnty)))*" "
        s4=(6-len(str(self.price)))*" "

        print"  ",  self.code,"       ",self.name,s1,self.cost,s2,self.qnty,s3,self.price,"   2%"

        
    @staticmethod
    def net():
        print "Your net payable amount INCLUDING GST is",((bill.netbal)*0.02)+bill.netbal,"Rs."





    
##FUNCTIONS FOR BINARY FILE##

                        #for dumping..... 
def dumping():
    c1=custdetails()
    c1.enter_details()
    f1=open("F:\\PARUL\\PYTHON PROJECT\\details.dat","ab")
    pickle.dump(c1,f1)
    f1.close()
       
                       #for modification....

def modification():
    c1=custdetails()
    
    ID=input("Enter your unique customer id for verification")
    f1=open("\\details.dat","rb")
    t1=open("temp.dat","ab")
    c1=pickle.load(f1)
    if c1.cID!=ID:
        print "sorry, but no such record is found in our database"
    else:
        try:
            while True:
                c1=pickle.load(f1)
                if not c1:
                    break
                else:
                    if c1.cID!=ID:
                        pickle.dump(c1,t1)
                        
                    else:
                        print " Please enter your new details"
                        
                        c1.enter_details()
                        pickle.dump(c1,t1)
                        print " Thank you, your new details has been successfully saved, :-)"
                
        except EOFError:
            pass
    f1.close()
    t1.close()
    os.remove("\\details.dat")
    os.rename("temp.dat","\\details.dat")





##FOR DISPLAYING THE PRODUCTS##
def dis_pro(ID,name):
    time.sleep(1.5)
    for i in range(0,35):
              print "=",
              time.sleep(0.005)    

    print
    print 
                         


    wel= '''     We have a lot of varities to make your l'll masters more happier'''
    print (wel)
        
    time.sleep(0.5)
    wel= '''It's all grouped into four categories made in accordance to age groups'''
    print (wel)
    time.sleep(0.5)

    wel='''             Category #1   0-3 yrs
                
            Category #2   3-6 yrs

            Category #3   6-9 yrs

            Category #4   9-12 yrs
'''
    for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
        
    for i in range(0,30):
              print "*",
              time.sleep(0.005)
                         
      
    for i in range(0,5):
              time.sleep(0.01)
              print '.',

    print
    print
    wel= '''So, for how much old child are you looking for?
'''
    print (wel)    
    ch="y"
    while ch=="y":
        cat=input("Please enter the category number : ")
        print
        print
        print
        print '''NOW, LOOK A BUTTON HAS APPEARED IN A NEW WINDOW NAMED tk
CHECK IT OUT TO VIEW THE IMAGE OF THIS CATEGORY PRODUCT'''
        time.sleep(1)
        print
        print
        

        wel= '''Don't forget to notice the product code'''
        for i in range(0,len(wel)):
            print (wel[i]),
        print
        print
        print

        if cat==1:
            #for pic 1
            a=tk.Tk()
            def pic1():
            
                photo=tk.PhotoImage(file="F:\\PARUL\\PYTHON PROJECT\\P.gif")
                cv=tk.Canvas()
                cv.pack(side='top', expand='yes')
                cv.create_image(1,1, image=photo,anchor='nw')
                tk.mainloop()



            a=Button(text='Click to view category 1', command=pic1).place(x=100,y=100)
            mainloop()
            
        elif cat==2:
            #for pic 2
            def pic2():
                
                photo=tk.PhotoImage(file="F:\\PARUL\\PYTHON PROJECT\\P2.gif")
                cv=tk.Canvas()
                cv.pack(side='top', expand='yes')
                cv.create_image(1,1, image=photo,anchor='nw')
                tk.mainloop()


            a=Button(text='Click to view category 2', command=pic2).place(x=100,y=100)
            mainloop()
        elif cat==3:
            #for pic 3
            def pic3():
                
                photo=tk.PhotoImage(file="F:\\PARUL\\PYTHON PROJECT\\P3.gif")
                cv=tk.Canvas()
                cv.pack(side='top', expand='yes')
                cv.create_image(1,1, image=photo,anchor='nw')
                tk.mainloop()


            
            a=Button(text='Click to view category 3', command=pic3).place(x=100,y=100)
            mainloop()
        elif cat==4:
            #for pic 4
            def pic4():
                
                photo=tk.PhotoImage(file="F:\\PARUL\\PYTHON PROJECT\\P4.gif")
                cv=tk.Canvas()
                cv.pack(side='top', expand='yes')
                cv.create_image(1,1, image=photo,anchor='nw')
                tk.mainloop()


            
            a=Button(text='Click to view category 4', command=pic4).place(x=100,y=100)
            mainloop()
            
        else:
            print "It's a wrong choice"
        ch=raw_input("want to review the categories? y/n : ")
        if ch=="n":
            c=input("press 1 to go back and 2 to exit : ")
            if c==1:
                choice2(ID,name)
            elif c==2:
                sys.exit()
##FOR BILL GENERATION
def billing(ID,name):
    

    n=input("So, how many orders would u like to give us? : ")
    cust=list()
    for i in range(n):
        c=bill()
        c.get()
        cust.append(c)
    print
    print


    x="......Generating your bill......"
    print
    print 
    for i in range(0,len(x)):
        time.sleep(0.1)
        print x[i],
            
    time.sleep(2)
    print 
    print
    print
    for i in range(0,35):
        time.sleep(0.1)
        print "*",
    print
    print
    print
    
    print '''                        ||THE KID'S CRADLE||'''
    time.sleep(1.5)
    print'''                               CASH MEMO'''
    print "Today's date "  + time.strftime("%x")
    time.sleep(1.5)
    print
    print "Current time " + time.strftime("%X")
    time.sleep(1.5)
    print
    print "Customer's Name : ",name
    time.sleep(1.5)

    print
    print '''ITEM CODE         ITEM NAME         COST PER UNIT     QNTY    COST   TAX PER UNIT'''


    for j in range(n):
        cust[j].display()
        time.sleep(1.3)
    time.sleep(2)

    print
    print
    print

    bill.net()
    time.sleep(2)
    print
    print
    print
    time.sleep(2)

    wel= "Thank You for choosing us!"
    print
    print

    for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
    time.sleep(2)
    wel= "Your requirements will reach you soon  :-)"
    for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
    print
    print
    for i in range(0,20):
        time.sleep(0.1)
        print "*",
    print
    print
    print

## FOR PLACING ORDER##
def place_order(ID,name):
    wel= '''
As you might have noticed that a number, name and value is alloted to each product....
'''
    for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
    
    time.sleep(1.5)
    wel= '''

So, would you like to place the order?
'''

    for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)

    ch=raw_input("Say yes or no : ")

    for i in range(0,5):
              time.sleep(0.3)
              print '.',   
    while ch=='yes' or 'YES':
        
                #....................................................bill generation#
        billing(ID,name)
        ch=raw_input("Want to continue (yes or no) : ")
        if ch=="no":
            choice2(ID,name)

##FOR ADMINISTRATOR


def Administrator():
          wel='You will get 3 chances to Login!!'
          print
          for i in range (0,len(wel)):
                                        time.sleep(.01)
                                        print (wel[i]),
                                        time.sleep(.01)
          a=1
          while a<4:
                    print
                    user=raw_input('User Id:')
                    if user=='Parul Garg':
                        pas=raw_input("What is the password? : ")
                        if pas=='cs@python':
                            for i in range(0,5):
                                time.sleep(0.1)
                                print '.',
                            wel= 'Login successful'
                            for i in range(0, len(wel)):
                                    print (wel[i]),
                            print
                            a=5
                        else:
                            print 'Wrong password  :-('
                            a+=1
                            print 'You need to enter it again!!'            

                    else:
                              print 'Wrong user id   :-('
                              a+=1
                            
          if a==4:
              print"You entered wrong id and password 3 times."
              print
              print "Sorry, your access is denied  :-("
              print

              choice()
              

          if a==5:
                    while True:                           
                                time.sleep(1.5)
                                print
                                
    
                                wel='''What would you like to do?.....'''


                                
                                for i in range (0,len(wel)):
                                    time.sleep(.01)
                                    print (wel[i]),
                                    time.sleep(.01)
                                print
                                print

                                print "1.)See List of Registered Customers"
                                print
                                time.sleep(0.5)
                                print "2.)Log Out"
                                print
                                time.sleep(0.5)

                             
                                print
                                ch=input('So, what have you decided? : ')
                              
                                if ch==1:
                                      SeeListofRegisteredCustomers()
                                elif ch==2:
                                    choice()
                                else:
                                    print "Wrong choice"
                                    break

                                   #..............for the administrator##
        
def SeeListofRegisteredCustomers():
                                
                for i in range(0,5):
                          time.sleep(0.3)
                          print '.',

                print
                s1=10*" "
                s2=15*" "
                s3=20*" "
                s4=10*" "
                print 'Name',s1,"     ",'Age',s2,'Address',s3,'Phone No',s4,'Customer ID'
                files=open('details.dat','rb')  
                try :
                                
                    d=pickle.load(files)
                    while d:
                                        
                              d.showcustomer()
                                        
                              d=pickle.load(files)
                              print
                                        
                              
                except EOFError:
                    pass
                files.close()

##FOR AN EXISTING CUSTOMER

def oCustomer():
    
    ID=input('Enter your unique Id: ')
    files=open('details.dat','rb')
    
    try :
        
            
            while True:
                d=pickle.load(files)
                
                if ID==d.cID:
                    
                    name=d.cname
                    global name
                    
                    time.sleep(1)
                
                    wel= '''
        Hello! and Welcome to the world of toys!! :-)'''
                    for i in range (0,len(wel)):
                     time.sleep(.01)
                     print (wel[i]),
                     time.sleep(.01)
    
                    files.close()
                    
                    choice2(ID,name)
                    
                if not d:
                    print"this ID does not exist"

            
    except EOFError:
        
                        pass
    files.close()
def choice2(ID,name):
    print
    time.sleep(1.5)
    cho=0
    while cho>=0:
        print
        time.sleep(1)
        for i in range(0,35):
            print "=",
        print
        print

        wel='''
        So, how can we help you?.....'''


                                    
        for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
        print
        print

        print "                      1. Have a look at our products "
        time.sleep(0.5)
        print
        print "                      2. Place an order for your kiddie"
        time.sleep(0.5)
        print
        print "                      3. Look your details"
        time.sleep(0.5)
        print
        print "                      4. Modify your details"
        time.sleep(0.5)
        print
        print "                      5. Exit to previous menu"
        time.sleep(0.5)
        print
        print "                      6. Exit"
        time.sleep(0.5)

        ch=input("What's your choice? : ")
        if ch==1:
            dis_pro(ID,name)
        elif ch==2:
            place_order(ID,name)
        elif ch==4:
            editinfo(ID,name)
        elif ch==3:
            seeinfo(ID,name)
        elif ch==6:
            sys.exit()
        elif ch==5:
            choice()
        else:
            print 'Sorry, but you made a wrong choice'
            choice2(ID,name)

    
        

##FOR DETAILS OF OLD CUSTOMER

def seeinfo(ID,name):
          print
          
          print 'Name         Age           Address                  Phone No        Customer ID '
          
          a=custdetails()
          
          files=open('details.dat','rb')
          try :
                    while True:
                              d=pickle.load(files)
                              if not d:
                                        break
                              elif d.cID ==ID:
                                        d.showcustomer()                                                                      
                                        print
          except EOFError:
                    pass
          files.close()
          choice2(ID,name)

def editname(ID):
          
          sal=raw_input('Enter Correct Name here-')
          file2=open('sample1.txt','ab')
          files=open('details.dat','rb')
          try:
                    while True:
                              r=pickle.load(files)
                              if r.cID !=ID:
                                        pickle.dump(r,file2)
                              else:
                                        r.cname=sal 
                                        pickle.dump(r,file2)
                                                  
          except EOFError:
                    pass
          files.close()          
          file2.close()
          os.remove('details.dat')
          os.rename('sample1.txt','details.dat')
          
def editage(ID):
        sal=raw_input('Enter your correct age: ')
        file2=open('sample1.txt','ab')
        files=open('details.dat','rb')
        try:
                  while True:
                            r=pickle.load(files)
                            if r.cID!=ID:
                                      pickle.dump(r,file2)
                            else:
                                      r.cage=sal 
                                      pickle.dump(r,file2)
                                                
        except EOFError:
                  pass
        files.close()          
        file2.close()
        os.remove('details.dat')
        os.rename('sample1.txt','details.dat')
def editaddress(ID):
          
        sal=raw_input('Enter your correct address: ')
        file2=open('sample1.txt','ab')
        files=open('details.dat','rb')
        try:
                  while True:
                            r=pickle.load(files)
                            if r.cID!=ID:
                                      pickle.dump(r,file2)
                            else:
                                      r.caddress=sal 
                                      pickle.dump(r,file2)
                                                
        except EOFError:
                  pass
        files.close()          
        file2.close()
        os.remove('details.dat')
        os.rename('sample1.txt','details.dat')
def editphonenumber(ID):
    
          sal=raw_input('Enter Correct Phone Number here-')
          file2=open('sample1.txt','ab')
          files=open('details.dat','rb')
          try:
                    while True:
                              r=pickle.load(files)
                              if r.cID!=ID:
                                        pickle.dump(r,file2)
                              else:
                                        r.cphno=sal 
                                        pickle.dump(r,file2)
                                                  
          except EOFError:
                    pass
          files.close()          
          file2.close()
          os.remove('details.dat')
          files.close()          
          file2.close()
          os.rename('sample1.txt','details.dat')




def editinfo(ID,name):
          
          print
          print 'Name           Age              Address          Phone No     Customer ID'
          files=open('details.dat','rb')  
          try :
                    while True:
                        d=pickle.load(files)
                        if d.cID ==ID:
                                d.showcustomer()                                                                      
                                print  
                                                                              
                    
                    print
          except EOFError:
                              pass
          files.close()
          wel=''' 
                       What Do You Want To Edit..??

                                1.)Name

                                2.)Age

                                3.)Address

                                4.)Phone Number

                                5.)Back'''

          for i in range (0,len(wel)):
                    time.sleep(.01)
                    print (wel[i]),
                    time.sleep(.01)
          while True:
                    time.sleep(1.5)
                    print
                    print
                    ch='Enter Your choice here-'
                    for i in range (0,len(ch)):
                              time.sleep(.01)
                              print ch[i],
                              time.sleep(.01)
                    ch=input('')
                    if ch==1:
                              editname(ID)
                              time.sleep(0.5)
                              wel= "Your details has been sucessfully saved"
                              for i in range (0,len(wel)):
                                  time.sleep(.01)
                                  print (wel[i]),
                                  time.sleep(.01)
                              choice2(ID,name)
                    elif ch==2:
                              editage(ID)
                              time.sleep(0.5)
                              wel= "Your details has been sucessfully saved"
                              for i in range (0,len(wel)):
                                  time.sleep(.01)
                                  print (wel[i]),
                                  time.sleep(.01)
                              choice2(ID,name)
                    elif ch==3:
                              editaddress(ID)
                              time.sleep(0.5)
                              wel= "Your detail's has been sucessfully saved"
                              for i in range (0,len(wel)):
                                  time.sleep(.01)
                                  print (wel[i]),
                                  time.sleep(.01)
                              choice2(ID,name)
                    elif ch==4:
                              editphonenumber(ID)
                              time.sleep(0.5)
                              wel= "Your detail's has been sucessfully saved"
                              print (wel)
                              choice2(ID,name)
                    elif ch==5:
                        choice2(ID,name)
                    else:
                              print 'Wrong Choice'
                              break


##FOR A NEW CUSTOMER

def nCustomer():
          
          a=custdetails()
          a.enter_details()
          files=open('details.dat','ab+')
          pickle.dump(a,files)
          files.close()
          time.sleep(1.5)
          print
          print
          
          wel= 'Thank You For Joining us...   :-)'
          time.sleep(0.5)
          print (wel)
          print
          print
          
          choice()                                


def choice():
        print
        time.sleep(1.5)
           
        for i in range (0,35):
            time.sleep(.01)
            print "=",
            time.sleep(.01)
        print
        print

        wel=''' 
How Do You Want To Login?'''


        
        for i in range (0,len(wel)):
            time.sleep(.01)
            print (wel[i]),
            time.sleep(.01)
        print
        print

        print "                            1.)Administrator"
        time.sleep(0.5)
        print
        print "                            2.)Registered Customer"
        time.sleep(0.5)
        print
        print "                            3.)New Customer"
        time.sleep(0.5)
        print
        print "                            4.)Exit"
        time.sleep(0.5)
        print
          
        while True:
            ch=input("So, what did you chose? : ")
            if ch==1:
                Administrator()
                                
            elif ch==2:
                oCustomer()
                                
            elif ch==3:
                nCustomer()
                                
            elif ch==4:
                return

            else:
                print 'Sorry, but you made a wrong choice'
                                

#.........................................THE MAIN MENU
            


WEL= '''    WELCOME TO THE COMPANY MANAGEMENT PROJECT'''
                         
for i in range(0,len(WEL)):
    time.sleep(0.02)
    print (wel[i]),
print

WEL='''                         MADE BY PARUL GARG'''
for i in range(0,len(WEL)):
    time.sleep(0.02)
    print (wel[i]),

print
print
print
for i in range(0,35):
    print "=",
    time.sleep(0.05)

print
print
print
time.sleep(1)
print '''                            ||THE KID'S CRADLE||'''
time.sleep(1)     
print '''                                              - bringing smile on every face  '''                          



print        

#......Displaying current date and time
print "Today's date "  + time.strftime("%x")




for i in range(0,5):
          time.sleep(0.3)
          print '.',
print
print
print
## Time representation
print "Current time " + time.strftime("%X")

for i in range(0,5):
          time.sleep(0.2)
          print '.',
print
print
print

   
choice()
