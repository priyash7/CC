import os
import platform
import mysql.connector 
import pandas as pd 
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="root",\
                             database="COURSE_MATCH")
mycursor=mydb.cursor()

def course_Insert():
 L=[] 
 c_id=int(input("Enter the course id : "))
 L.append(c_id)
 stream=input("Enter The Stream Name:")
 L.append(stream)
 c_name=input("Enter available opportunities or courses  in this stream : ") 
 L.append(c_name)
 course=(L) 
 sql="insert into course_details (c_id, stream, c_name) values (%s,%s,%s)" 
 mycursor.execute(sql,course) 
 mydb.commit()
 
def cView(): 
 print("Select the search criteria : ") 
 print("1. c_id") 
 print("2. Stream") 
 print("3. All") 
 ch=int(input("Enter the choice : ")) 
 if ch==1:
     s=int(input("c_id : "))
     c=(s,)
     sql="select * from course_details where c_id=%s"
     mycursor.execute(sql,c)
 elif ch==2:
     s=input("Enter stream Name : ")
     n=(s,)
     sql="select * from course_details where stream=%s"
     mycursor.execute(sql,n) 
 elif ch==3:
     sql="select * from course_details"
     mycursor.execute(sql)
 res=mycursor.fetchall()
 print("The course details are as follows : ")
 print("course_id, Stream_Name,Course_opportunities")
 for x in res:
    print(x)
    
def removecourse():
    c_id=int(input("Enter the course_id of the course to be deleted : "))
    ci=(c_id,)
    sql="Delete from course_details where c_id=%s"
    mycursor.execute(sql,ci)
    sql="Delete from course_details where c_id=%s"
    mycursor.execute(sql,ci)
    mydb.commit()
def MenuSet(): #Function For The course match
    print("Enter 1 : To Add course")
    print("Enter 2 : To View course ")
    print("Enter 3 : To Remove course")
    try: #Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
        exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n") #Print New Line
        if(userInput == 1):
            course_Insert()
        elif (userInput==2):
            cView()
        elif (userInput==3):
            removecourse()
        else: print("Enter correct choice. . . ")
    
MenuSet()
def runAgain():
 runAgn = input("\nwant To Run Again Y/n: ")
 while(runAgn.lower() == 'y'):
     if(platform.system() == "Windows"):
         print(os.system('cls'))
     else:
         print(os.system('clear'))
     MenuSet()
     runAgn = input("\nwant To Run Again Y/n: ")
runAgain() 
