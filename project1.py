import os
import platform
import mysql.connector
import pandas as pd
import datetime
global z
mydb = mysql.connector.connect(user='root', password='1234',
 host='localhost',
 database='event')
mycursor=mydb.cursor()


print("+----------------------------------------------+")
print("|   WELCOME  TO   El Festejo! EVENT PLANNING   | ")
print("+----------------------------------------------+")
print("| Please select an option!                     |")
print("|                                              |")
print("| 1.Instructions                               |")
print("| 2.Quit                                       |")
print("+----------------------------------------------+\n")


choice=int(input("enter your selection :"))

if choice==2:
    print("+----------------------------------------------+")
    print("| Thank You For Visiting! :)                   |")
    print("+----------------------------------------------+\n")
    quit()

else:
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|     INSTRUCTIONS                                                                                                                    | ")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                     |")
    print("| 1.The user is required to fill in his/her personal details.                                                                         |")
    print("| 2.A menuset will be displayed to the user.                                                                                          |")
    print("| 3.The user needs to choose from the menuset as per his/her requirement.                                                             |")
    print("| 4.At the end , a complete bill will be generated to the user.                                                                       |")
    print("|                                                                                                                                     |")
    print("| We hope you enjoy our services!                                                                                                     |")
    print("|                                                                                                                                     |")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+\n")



def register():
    mycursor.execute("CREATE TABLE customer(name varchar(20),address varchar(30),phone int,date varchar(20));")
    global name
    global address
    global phone
    global date
    name=input("enter your name :")
    address=input("enter your address :")
    phone=int(input("enter your phone no. :"))
    date=input("enter your date :")
    sql="insert into customer(name,address,phone,date)values(name,address,phone,date)"
    mycursor.execute(sql)
    mydb.commit()

def eventtype():
 print("Do you want to see event types available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
     
  mycursor.execute("select*from decoration")
  myresult=mycursor.fetchall()
  for x in myresult:
   print(x)

def eventbill():
 global e
 x=int(input("Enter your type of event please"))
 if(x==1):
  print ("you have opted for Birthdays and small parties")   
  e=100000
 elif (x==2):
  print ("you have opted for Weddings and Receptions")   
  e=300000
 elif (x==3):
  print ("you have opted for Formal meetings and conferences")   
  e=300000
 elif (x==4):
  print ("you have opted for Fundraising Events")   
  e=100000
 else:
  print ("please choose an event")
 print ("your event bill including GST is =",e)
 return e


def venue():
   print("Do you want to see location with areas available : Enter 1 for yes :")
   ch=int(input("enter your choice:"))
   if ch==1:
     sql="select * from venue"
     mycursor.execute(sql)
     rows=mycursor.fetchall()
     for x in rows:
      print(x)

def venuebill():
 global s
 print ("We have the following venues for you:-")
 sql="select *from venue"
 x=int(input("Enter Your Choice Please->"))
 n=int(input("For How many days do you want to book:"))
 if(x==1):
  print ("you have opted Lake Land Country Club,KOLKATA")
  s=10000*n
 elif (x==2):
  print ("you have opted Royal Orchid Beach Resort,GOA")
  s=20000*n
 elif (x==3):
  print ("you have opted Radisson Blu Hotel,NEW DELHI")
  s=30000*n
 elif (x==4):
  print ("you have opted The Oberoi Udayvillas,UDAIPUR")
  s=40000*n
 elif (x==5):
  print ("you have opted JW Marriott Juhu,MUMBAI")
  s=50000*n
 else:
  print ("please choose a venue")
 print ("your total venue rent is =",s)
 return s
 runagain()

     
 
def starter():
 print("Do you want to see starter items available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from starter"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
   print(x)


def starterbill():
 global t
 print("Do yoy want to see the starter menu available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from starter"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
   print(x)

 print("do you want to purchase from above list:enter your choice:")
 d=int(input("enter your choice:"))
 a=int(input("Please enter no of heads: "))
 if(d==1):
  print("you have ordered veg salad")
  t=350*a
  print("your amount for veg salad is :",t,"\n")
 elif (d==2):
  print("you have ordered cheese corn salad")
  t=400*a
  print("your amount for cheese corn salad is :",t,"\n")
 elif(d==3):
  print("you have ordered chicken pasta salad")
  t=450*a
  print("your amount for chicken pasta salad is :",t,"\n")
 elif(d==4):
  print("you have ordered crispy babycorn")
  t=335*a
  print("your amount for crispy babycorn is :",t,"\n")
 elif(d==5):
  print("you have ordered mushroom soup")
  t=250*a
  print("your amount for mushroom soup is :",t,"\n")
 elif(d==6):
  print("you have ordered ginger garlic soup")
  t=300*a
  print("your amount for ginger garlic soup is :",t,"\n")
 elif(d==7):
  print("you have ordered chicken sweet corn soup")
  t=300*a
  print("your amount for chicken sweet corn soup is :",t,"\n")
 else:
   Print("please enter your choice from the menu")
 return t


def maincourseveg():
   print("Do you want to see maincourse veg items available : Enter 1 for yes :")
   ch=int(input("enter your choice:"))
   if ch==1:
     sql="select * from maincourse_veg"
     mycursor.execute(sql)
     rows=mycursor.fetchall()
     for x in rows:
        print(x)

def maincoursevegbill():
 global l
 print("Do yoy want to see the main course (veg) menu available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from maincourse_veg"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
   print(x)

 print("do you want to purchase from above list:enter your choice:")
 d=int(input("enter your choice:"))
 n=int(input("enter no of heads:"))
 if(d==1):
  print("you have ordered butter naan")
  l=100*n
  print("your amount for butter naan is :",l,"\n")
 elif (d==2):
  print("you have ordered peas kachori")
  l=60*n
  print("your amount for peas kachori is :",l,"\n")
 elif(d==3):
  print("you have ordered achari-alur dum")
  l=200*n
  print("your amount for achari-alur dum is :",l,"\n")
 elif(d==4):
  print("you have ordered paneer butter masala")
  l=230*n
  print("your amount for paneer butter masala is :",l,"\n")
 elif(d==5):
  print("you have ordered veg fried rice")
  l=330*n
  print("your amount for veg fried rice is :",l,"\n")
 elif(d==6):
  print("you have ordered veg hakka noodles")
  l=350*n
  print("your amount for veg hakka noodles is :",l,"\n")
 elif(d==7):
  print("you have ordered veg manchurian")
  l=300*n
  print("your amount for veg manchurian is :",l,"\n")
 else:
   Print("please enter your choice from the menu")
 return l


def maincoursenonveg():
 print("Do you want to see maincourse non veg items available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from maincourse_non_veg"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
   print(x)


def maincoursenonvegbill():
 global k
 print("Do you want to see the maincourse non-veg menu available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from maincourse_non_veg"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
    print(x)

 print("do you want to purchase from above list:enter your choice:")
 d=int(input("enter your choice:"))
 n=int(input("enter no of heads:"))
 if(d==1):
  print("you have ordered masala kulcha")
  k=150*n
  print("your amount for masala kulcha is :",k,"\n")
 elif (d==2):
  print("you have ordered mutton biriyani")
  k=450*n
  print("your amount for mutton biriyani:",k,"\n")
 elif(d==3):
  print("you have ordered chicken chaap")
  k=400*n
  print("your amount for chicken chaap is :",k,"\n")
 elif(d==4):
  print("you have ordered chicken bharta")
  k=500*n
  print("your amount fopr chicken bharta is :",k,"\n")
 elif(d==5):
  print("you have ordered chicken rezala")
  k=550*n
  print("your amount for chicken rezala is :",k,"\n")
 elif(d==6):
  print("you have ordered mixed fried rice")
  k=450*n
  print("your amount for mixed fried rice is :",k,"\n")
 elif(d==7):
  print("you have ordered chilli chicken")
  k=400*n
  print("your amount for chilli chicken is :",k,"\n")
 else:
   Print("please enter your choice from the menu")
 return k


def dessert():
 print("Do you want to see dessert items available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from dessert"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
   print(x)
       

def dessertbill():
  global q
  print("Do yoy want to see menu available : Enter 1 for yes :")
  ch=int(input("enter your choice:"))
  if ch==1:
   sql="select * from dessert"
   mycursor.execute(sql)
   rows=mycursor.fetchall()
   for x in rows:
    print(x)

  print("do you want to purchase from the dessert list:enter your choice:")
  d=int(input("Please enter your choice:"))
  n=int(input("Please enter the no of heads for the event: "))
  if(d==1):
    print("you have ordered ice-cream")
    q=250*n
    print("your amount for ice-cream is :",q,"\n")
  elif (d==2):
   print("you have ordered baked roshogolla")
   q=150*n
   print("your amount for baked roshogolla is :",q,"\n")
  elif(d==3):
   print("you have ordered gulab jamun")
   q=150*n
   print("your amount for gulab jamun is :",q,"\n")
  elif(d==4):
   print("you have ordered phirni")
   q=200*n
   print("your amount for phirni is :",q,"\n")
  else:
   print("please enter your choice from the menu")
  return q



def activities():
 print("Do yoy want to see the add-on activities available : Enter 1 for yes :")
 ch=int(input("enter your choice:"))
 if ch==1:
  sql="select * from activities"
  mycursor.execute(sql)
  rows=mycursor.fetchall()
  for x in rows:
   print(x)

def activitiesbill():
  global g
  print("do you want to purchase from the add-on list:enter your choice:")
  d=int(input("Please enter your choice:"))
  if(d==1):
    print("you have opted for music")
    g=40000
    print("your amount for music is :",g,"\n")
  elif (d==2):
   print("you have opted for DJ")
   g=120000
   print("your amount for DJ is :",g,"\n")
  elif (d==3):
   print("you have opted for Live Counter-Kebabs ")
   g=70000
   print("your amount for Live Counter-kebabs is :",g,"\n")
  elif (d==4):
   print("you have opted for Live Counter-Mocktails ")
   g=100000
   print("your amount for Live Counter-Mocktails is :",g,"\n")
  elif (d==5):
   print("you have opted for Dance Ball ")
   g=50000
   print("your amount for Live Counter-Mocktails is :",g,"\n")
  elif (d==6):
   print("you have opted for Magic Show ")
   g=150000
   print("your amount for Magic Show is :",g,"\n")
  elif (d==7):
   print("you have opted for Aesthetic Bokeh Lighting ")
   g=100000
   print("your amount for Aesthetic Bokeh Lighting is :",g,"\n")
  else:
   print("please enter your choice from the add-ons list")
  return g


def completebill():
    
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("| NAME :"+name+"                                                                                                                      | ")
    print("| ADDRESS :"+address+"                                                                                                                | ")
    print("| PHONE :"+str(phone)+"                                                                                                               |")
    print("| DATE :" +date+"                                                                                                                     |")
    print("|                                                                                                                                     |")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                     |")
    print("| Event bill:", e,"                                                                                                                   | ")
    print("| Venue bill:",s,"                                                                                                                    | ")
    print("| Starter bill:",t,"                                                                                                                  | ")
    print("| Main course veg bill:",l,"                                                                                                          | ")
    print("| Main course non veg bill:",k,"                                                                                                      | ")
    print("| Dessert bill",q,"                                                                                                                   | ")
    print("| Add-on activities bill:",g,"                                                                                                        | ")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Total bill:",e+s+t+l+k+q+g,"                                                                                                        | ")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
   
           

def menuset():
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|     MENUSET                                                                                                                         | ")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                     |")
    print("| 1. To enter customer data                                                                                                           |")
    print("| 2. To display event type                                                                                                            |")
    print("| 3. To calculate event bill                                                                                                          |")
    print("| 4. To view venue                                                                                                                    |")
    print("| 5. To calculate venue bill                                                                                                          |")
    print("| 6. To view starter menu                                                                                                             |")
    print("| 7. To calculate starter bill                                                                                                        |")
    print("| 8. To view Main course (veg) menu                                                                                                   |")
    print("| 9. To calculate Main course (veg) bill                                                                                              |")
    print("| 10. To view Main course (non-veg) menu                                                                                              |")
    print("| 11. To calculate Main course (non-veg) bill                                                                                         |")
    print("| 12. To view dessert menu                                                                                                            |")
    print("| 13. To calculate dessert bill                                                                                                       |")
    print("| 14. To view add-on activities                                                                                                       |")
    print("| 15. To calculate add-on activities bill                                                                                             |")
    print("| 16. For complete bill                                                                                                               |")
    print("| 17. To exit                                                                                                                         |")
    print("|                                                                                                                                     |")
    print("+-------------------------------------------------------------------------------------------------------------------------------------+\n")

    try:
     userinput=int(input("Please select an above option:"))
    except ValueError:
      exit("\n Please enter a number")


    userinput=int(input("Please enter your choice"))
    if(userinput==1):
     register()
    elif(userinput==2):
     eventtype()
    elif(userinput==3):
     eventbill()
    elif(userinput==4):
     venue()
    elif(userinput==5):
     venuebill()
    elif(userinput==6):
     starter()
    elif(userinput==7):
     starterbill()
    elif(userinput==8):
     maincourseveg()
    elif(userinput==9):
     maincoursevegbill()
    elif(userinput==10):
     maincoursenonveg()
    elif(userinput==11):
     maincoursenonvegbill()
    elif(userinput==12):
     dessert()
    elif(userinput==13):
     dessertbill()
    elif(userinput==14):
     activities()
    elif(userinput==15):
     activitiesbill()
    elif(userinput==16):
     completebill()
    elif(userinput==17):
     quit()
    else:
     print("enter correct choice")

menuset()
def runAgain():
 runAgn = input("\nwant To Run Again Y/n: ")
 while(runAgn.lower() == 'y'):
  if(platform.system() == "Windows"):
    print(os.system('cls'))
  else:
    print(os.system('clear'))
  menuset()
  runAgn = input("\nwant To Run Again Y/n: ")
runAgain()
   



