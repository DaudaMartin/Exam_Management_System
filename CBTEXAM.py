from distutils.command.check import check
from operator import index
from optparse import Option
from sqlite3 import DataError, DatabaseError, IntegrityError
import sys
import time
import subprocess
import datetime as dt
from traceback import print_tb
tm = dt.datetime.now()

#---------------------------------------------------VERSION 1 CBT PROGRAMM 
# student_details = {"WALE":"345","TOHEEB" : "123"}
# def questions():
#     global score
#     score = 0
#     print("If You are done type S to submmit")
#     questions = {
#         1 :{'D': ''' 
#         1. what is the maximum length of a python identifier \n (a) 32 \n (b) 16 \n(c) 128\n
#         (d) no fixed lenght is specified
#         '''},
#         2:{'A': ''' 
#         2. what will be the output of the following code snippet? (2**3 + (5+6)**(1+1)) \n (a) 129 \n (b)8 \n(c)121 (d)none of the above
#         '''},
#         3 :{'D': ''' 
#         3. what will be the datatype of var in the below code snippet? \n var = 10 \n print(type(var)) \n var = "Hello" \n print(type(var)) \n (a) str and int \n (b)int and int \n (c)str and str (d)int and str
#         '''},
#         4: {'S':'Type S to submit'}
#     }
#     for q in questions.values():
#         for y,z in q.items():
#             time.sleep(2)
#             print(z)
#             user = input("input your answer")
#             if user.strip().capitalize()==y:
#                 score += 5
#     if user. strip().capitalize()=='S':
#                 result()                  
# def exam_():
#     print("""
    
#             ________________WAIT WHILE QUESTION IS LOADING__________________
    
    
#     """)
#     time.sleep(4)
#     print(student_Name + " Your Exam Start Now")
#     print("""
#       Instruction: \n          YOU HAVE 10min to complete all questions, click submit once you are done
#     """)
#     questions()          
# def result():
#         print(student_Name + ' your Score is '+str(score))
#         login()
                
# def quit():
#     print("""
#      Are you sure you want to close the program

#      If yes Type Q to Quit
#      """)
#     studentExit = input("TYPE Q TO EXIT")
#     if studentExit == "Q":
#         sys.exit()
# def login():
#     print("""


#                  ...............Wait while Page is Loading
          

#            Computer Based Test Program                          
#            Copy Right TMR 2022 
#        """)
#     time.sleep(2)
#     user_student = input("To Quit type Q or click Return to Continue").upper()
#     if user_student == "Q":
#         quit()
#     else:
#         user_Input = input("Enter E to take Exam : ").upper()
#         if user_Input == "E": 
#             global student_Name 
#             student_Name = str(input("Enter Your Name"))
#             matricNo     = str(input("Enter your matricNumber"))
#             sign_In      = str(input("Type to sign in")).lower

#             if matricNo in student_details.values() and student_Name in student_details.keys():
#                 print("Successfully log in")
#                 exam_()
#             else:
#                 print("invalid Login")
#                 login()
# login()
#--------------------------------------------------------------------------------------|
# print(f"HELLO WORD {}")
import math
# a = []
# b= math.cos(20)*math.sin(20)
# a.append(b)
# print(a)
#---------------------------------------------------VERSION 2 CBT PROGRAMM 
import mysql.connector as sql
data_base = sql.connect(host='127.0.0.1', user='root', password = '', database= 'EXAM_MANAGEMENT_SYS')
cursor = data_base.cursor()
# cursor.execute("CREATE DATABASE EXAM_MANAGEMENT_SYS")
# cursor.execute("CREATE TABLE STUDENT_RECORDS (STUDENT_ID INT(5) PRIMARY KEY AUTO_INCREMENT,STUDENT_NAME VARCHAR(40), STUDENT_MATRIC INT(5) UNIQUE, STUDENT_SCORE INT(3))")
# cursor.execute("SHOW DATABASE")
# cursor.execute("ALTER STUDENT_ IN EXAM_MANAGEMENT_SYS ADD STUDENT_INFO")
# cursor.execute("CREATE TABLE QUESTION_BANK(TEACHER VARCHAR(15), SUBJECT VARCHAR(20), QUESTION VARCHAR(200) UNIQUE, ANSWER VARCHAR(4)) ")
checksubject = input("Enter Subject of the exam You want to sit for : ").upper()
query1 = "SELECT SUBJECT FROM RESULT_COLLATION WHERE MATRIC_NO = %s"
supply1 = (12323,)
cursor.execute(query1,supply1)
check1 = cursor.fetchall()
for run in check1:
    if checksubject in run:
        print("Hi")
class CBT:
    def _init_(self):
        self.name = input("Input preffered Name ")
        self.login()
    def login(self):
        print("""


                ...............Wait while Page is Loading
          

          Computer Based Test Program
          Copy Right TMR 2022 
        """)
        user_ = input("To Quit type Q or click Return to Continue : ").upper()
        if user_ == "Q":
            self.quit()
        else:
            print("""
            Are You a staff or a Student  

            Type S if You are a Student
            Type T if You are a Staff 

            Press Q to quit
            """)
            user_Input = input("Enter S or T / Q : ").upper()
        try:
            if user_Input == "S": 
                global student_Name 
                global matricNo
                student_Name = str(input("Enter Your Name : "))
                matricNo     = int(input("Enter your matricNumber : "))
                query2 = "SELECT STUDENT_ID, STUDENT_NAME, STUDENT_MATRIC,SUBJECT FROM STUDENT_RECORDS WHERE STUDENT_NAME = %s AND STUDENT_MATRIC = %s"
                value_2 = (student_Name,matricNo)
                cursor.execute(query2, value_2)
                details = cursor.fetchone()
                name = details[1]
                self.mat_number = details[2]
                student_score = details[2]
                self.subject = details[3]
                data_base.commit()
                if details:
                         print("Successfully log in")
                         self.exam_()
                else:
                   print("invalid Login")
                   self.login() 
            elif user_Input == "T" :
                 self.register()
            elif user_Input == "Q":
                sys.exit()
            else :
                print("Invalid Input")
                self.login()
        except IntegrityError:
            print("Please Check Your Details and enter Correct Information")
            self.login()
        except ValueError:
            print("Please Insert Correct Value")
            self.login()
        except DataError:
            print("Please Check Your Details and enter Correct Information")
            self.login()
        except DatabaseError:
            print("Invalid User Registration")
            self.login()
        except TypeError:
            print("Please Check Your Details and enter Correct Information")
            self.login()
        except AttributeError:
            print("Please Check Your Details and enter Correct Information")
            self.login()
        finally:
            pass
    # def check_details(slelf):
    #     print(""" 
    #                  NOTE THIS FEATURE IS FOR STAFF
    #         """)
    #     print("Kindly Log in your details")
    #     log1 = input("Enter User ID ")
    #     logpass = input("Enter Password") 
    #     for x in teacherdeatinl.items():
    #         for z,y in x[1]:
    #             if x == log1 and z == logpass:
    #                     print(".................Loading Page")
    #                     for x in teacherdeatinl.items():
    #                         for y in studentdetails.items:
    #                          print(x[0])
    #                          print(y)
                             
    def register(self):
        print("""

                          HARVARD EXAM MANAGEMENT  SYSTEM

            """)
        print(""" 
                     NOTE THIS FEATURE IS FOR STAFFS

                     Press Q to Quit
            """)
        opt = input("Enter C to create your staff account or L if You Already Have an account : ").upper()
        if opt == "C":
            ("""
                    Please Note Password and ID(Your Name) will be require for Login into your Staff Account
            """)

            self.teacher_name = input("Enter Your Full name : ")
            self.teacher_subject = input("Enter Your Subject : ")
            self.teacher_pin = input("Input Pin : ") 
            reg_teacher = "INSERT INTO TEACHERS_DETAILS (NAME,SUBJECT,PIN) VALUES(%s,%s,%s)"
            value = (self.teacher_name,self.teacher_subject,self.teacher_pin)
            cursor.execute(reg_teacher,value)
            data_base.commit()
            print("Your Registration is Successfull")
            user = input("Enter Q to Quit or Click Return To Continue").upper()
            if user == "Q":
                self.login()
            else:
                self.teacher_login()
        elif opt == "L":
             self.teacher_login()
        elif opt == "Q":
            sys.exit()
        else: 
            self.staff()
    def choices(self):
        choice_ = input("Enter R to Register Student or S to set questions or V to view Questions : ").upper()
        try:
            if choice_ == "R":
                self.register_student()
            elif choice_ == "V" :
                self.view() 
            elif choice_ == "S":
                self.set_exam()
            else:
                print("invalid input")
                self.choices()
        except:
                self.choices()
    def teacher_login(self):
                print("""

                          HARVARD EXAM MANAGEMENT  SYSTEM
                              for Academic Staff Only
                                   Staff Login
                          
            """)
                try:
                    global name
                    global sub
                    print("Log In To Your Staff Account")
                    log_1 = input("Enter ID(Your Name) : ")
                    log_2 = input("Enter Your Password : ")
                    log = "SELECT NAME, SUBJECT, PIN FROM TEACHERS_DETAILS WHERE NAME=%s AND PIN=%s"
                    val = (log_1,log_2)
                    cursor.execute(log,val)
                    details = cursor.fetchone()
                    data_base.commit()
                    name = details[0]
                    sub = details[1]
                    if details:
                        print("""
                        Login Successful
                        """)
                        print("NAME : "+name +"\n"+"\n"+"SUBJECT : "+sub)
                        self.choices()
                        pass
                    else:
                        print("Invalid Login")
                        self.teacher_login()
                except:
                    self.teacher_login()
    def register_student(self):
            print("""

                          HARVARD EXAM MANAGEMENT  SYSTEM
                              for Academic Staff Only
                            student Registration Portal
                          
            """)
            self.number_ofstud = input("Enter Number Of Student You Want to register : ")
            x = int(self.number_ofstud)
            while x > 0:
                    # try:
                        global student_Name_reg
                        global student_Matric_reg
                        student_Name_reg = input("Enter Student Full Name :")
                        student_Matric_reg = int(input("Matric Number :"))
                        examQuery = "INSERT INTO STUDENT_RECORDS (STUDENT_NAME,STUDENT_MATRIC,TEACHER,SUBJECT) VALUES(%s,%s,%s,%s)"
                        value_1 = (student_Name_reg,student_Matric_reg,name,sub)
                        cursor.execute(examQuery,value_1)
                        data_base.commit()
                        # studentdetails.update(student)
                        if x == 0:
                            cursor.execute("SHOW DATABASE")
                            break
                        x -= 1
                        continue
                    # except IntegrityError:
                    #  print("Please Check Your Details and enter Correct Information")
                    #  self.register_student()
                    # except ValueError:
                    #  print("Please Insert Correct Value")
                    #  self.register_student()
                    # except DataError:
                    #  print("Please Check Your Details and enter Correct Information")
                    #  self.register_student()
                    # except DatabaseError:
                    #  print("Invalid User Registration")
                    #  self.register_student()
                    # except TypeError:
                    #  print("Please Check Your Details and enter Correct Information")
                    #  self.register_student()
            print("""

                            Student Registration Succesfull

                    """)
            user_input= input("Enter P to proceed to Staff Login  : or Q to Quit").upper()
            if user_input == "P": 
                     self.staff()       
            elif user_input == "Q":
                self.login()
            else:
                self.login()
    def staff(self):
            data_base.commit()
            print("""

                          HARVARD EXAM MANAGEMENT  SYSTEM
                              for Academic Staff Only
                                   Staff Portal
                          
            """)
            global name
            global sub
            teacher_id = input(" Enter ID (Your Full Name) : ")
            pin = int(input("Enter Pin : "))
            query = "SELECT ID, NAME, SUBJECT, PIN FROM TEACHERS_DETAILS WHERE NAME=%s AND TEACHER_PIN=%s"
            values = (teacher_id,pin)
            cursor.execute(query,values)
            detail = cursor.fetchone()
            data_base.commit()
            name = (detail[0])
            sub = (detail[1])
            print(name + " " + sub)
            data_base.close()
            print("""
            TO CHECK STUDENTS AND SUBJECT RECORDS TYPE C / TO SET EXAM TYPE S / TO VIEW EXAMS TYPE E  or Q TO QUIT APP 
             """)
            cheCk = input("Enter Text : ").upper()
            if cheCk == "C":
                query1 = "SELECT MATRIC,RECORD,SUBJECT,TIME FROM RESULT_COLLATION WHERE SUBJECT=%s"
                valcheck = (sub,)
                cursor.execute(query1,valcheck)
                detail1 = cursor.fetchall()
                data_base.commit()
                print(detail1)
            elif cheCk == "Q":
                sys.exit()
            elif cheCk == "S":
                self.set_exam()
            elif  cheCk == "E":
                    self.view()
            else:
                print("Invalid Input")
                self.staff() 
    def set_exam(self):
                data_base.commit()
                print("""

                          HARVARD EXAM MANAGEMENT  SYSTEM
                              for Academic Staff Only
                          
            """)
                # try:
                teacher_s = input("Enter Subject You Want To register")
                teacher = input(" Enter Number of Questions ")
                x = int(teacher)
                while x >0:
                       question = input("Enter Your Question")
                       option = input("Enter Option")
                       answer = input("Enter Answer")
                       setquery = "INSERT INTO QUESTION_BANK (TEACHER,SUBJECT,QUESTION,OPTION,ANSWER) VALUES(%s,%s,%s,%s,%s)"
                       supply = (name,sub,question,option,answer)
                       cursor.execute(setquery,supply)
                       data_base.commit()
                       x -= 1
                       if x == 0:
                        data_base.close()
                        print("Exam Completely Uploaded")
                        exa_m = input("Type V To View question or Q to Quit").upper()
                        if exa_m == "V":
                            self.view()
                        elif exa_m == "Q":
                            sys.exit()
                # except:
                #   self.set_exam()
    def view(self):
            teacher_name = name
            subject = sub
            query_ = "SELECT TEACHER, SUBJECT,QUESTION, OPTION,ANSWER FROM QUESTION_BANK WHERE TEACHER =%s AND SUBJECT=%s "
            supply = (teacher_name,subject)
            cursor.execute(query_,supply)
            dtabase = cursor.fetchall()
            data_base.commit()
            data_base.close()              
            print(str(dtabase))
            time.sleep(20)
            print("Do you want to quit Type Q to Quit or M to go to main menu")
            user = input("Enter Text : ")
            if user == "Q":
                sys.exit()
            elif user == "M":
                sys.exit()
            else:
                self.staff()
    def exam_(self):
            try:
                checksubject = input("Enter Subject of the exam You want to sit for : ").upper()
                query1 = "SELECT SUBJECT FROM RESULT_COLLATION WHERE MATRIC_NO = %s"
                supply1 = (self.mat_number,)
                cursor.execute(query1,supply1)
                check1 = cursor.fetchall()
                for run in check1:
                    if checksubject in run:
                        print("You have Already Taken this Exam")
                        self.exam_()
                else:
                    query2 = "SELECT SUBJECT FROM STUDENT_RECORDS WHERE STUDENT_MATRIC = %s"
                    supply2 = (self.mat_number,)
                    cursor.execute(query2,supply2)
                    review = cursor.fetchall()
                    data_base.commit()
                    for runcheck in review:
                        if checksubject in runcheck:
                            print("HELLO")
                            query = "SELECT QUESTION,OPTION,ANSWER,SUBJECT FROM QUESTION_BANK WHERE SUBJECT=%s"
                            supply = (checksubject,)
                            cursor.execute(query,supply)
                            exam = cursor.fetchall()
                            trythis = exam[0]
                            self.thesubject = trythis[3]
                            print("""
                                                               Your Exam is Loading
                                """)
                            print("SUBJECT : "+self.thesubject)
                            print("""
                                """)
                            print(student_Name + " Your Exam Start Now")
                            print("""
                                  Instruction: \n          YOU HAVE 10min to complete all questions, click submit once you are done
                                """)
                            index = 0
                            self.score = 0
                            for x in exam:
                                x = exam[index]
                                question = x[0]
                                option = x[1]
                                answer = x[2]
                                print (answer)
                                print("1. " + str(question) )
                                print(option)
                                user = input("input your answer").upper()
                                if user == answer:
                                    self.score += 5
                                index +=1
                                continue
                            print("Exam Completed")
                            print(student_Name +"Your Exam Score is "+str(self.score))
                            self.result()
                        else:
                            print("You Are Not Registered for this Exam")
                            self.exam_()
            except:
                print("Enter Valid Information")
                self.exam_()
    def result(self):
        # student_Score = self.score
        now_time = str(tm.time())
        now_date = str(tm.date())
        current_date = (now_time+" "+now_date)
        student_collation = (student_Name +" Score "+str(self.score)+" #"+self.thesubject)
        query =("INSERT INTO RESULT_COLLATION (MATRIC_NO,RECORD,SUBJECT,TIME) VALUES(%s,%s,%s,%s)")
        score_value = (self.mat_number,student_collation,self.thesubject,current_date)
        cursor.execute(query,score_value)
        data_base.commit()
        self.login()     
    def quit(self):
        data_base.close()              
        print("""
         Are you sure you want to close the program

         If yes Type Q to Quit
         """)
        studentExit = input("TYPE Q TO EXIT")
        if studentExit == "Q":
          sys.exit()          
haVARD = CBT()       
haVARD.login()
#--------------------------------------------------------------------------------------|
            

            
            
            


