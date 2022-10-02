#------------BANK TRANSACTION AUTOMATION
from secrets import choice
from sqlite3 import Cursor, DataError, DatabaseError, IntegrityError, OperationalError, ProgrammingError
import sys
import os
from threading import activeCount
import time
import mysql.connector as sql
import random
import datetime as dt
tm = dt.datetime.now()
bank_database = sql.connect(host="127.0.0.1", user="root", password ='', database="_ACCOUNT_DATABASE")
cursor = bank_database.cursor()
# cursor.execute("CREATE DATABASE _ACCOUNT_DATABASE")
#cursor.execute("CREATE TABLE USER_LOG (USER_ID INT(255) PRIMARY KEY AUTO_INCREMENT, USER_NAME VARCHAR(30) UNIQUE, USER_PASSWORD INT(11))")
# cursor.execute("CREATE TABLE USER_ACCOUNT(ACCOUNT_NUMBER INT(10) UNIQUE, ACCOUNT_NAME VARCHAR(20), ACCOUNT_BALANCE INT(20))")
#DELETE FROM `USER_LOG` WHERE `USER_LOG`.`USER_ID` = 2;
# cursor.execute("DELETE FROM _ACCOUNT_DATABASE TABLE USE_LOG")
# cursor.execute("DELETE FROM USER_LOG")
# cursor.execute("DROP TABLE ACCOUNT_REGISTRATION")
# cursor.execute("CREATE TABLE ACCOUNT_REGISTRATION(FIRSTNAME VARCHAR(20), LAST_NAME VARCHAR(20), OTHER_NAME VARCHAR(10), EMAIL_ VARCHAR(30) UNIQUE, PHONE_NUMBER INT(15) UNIQUE, BVN INT(15) PRIMARY KEY, NIN INT(11))")
# mycursor.execute("ALTER TABLE customers_table CHANGE ctm_id customer_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# cursor.execute("ALTER TABLE `ACCOUNT_REGISTRATION` CHANGE `ACCOUNT_NUMBER` `ACCOUNT_NUMBER` INT(15) NULL DEFAULT NULL;")
# ALTER TABLE `ACCOUNT_REGISTRATION` CHANGE `PHONE_NUMBER` `PHONE_NUMBER` INT(20) NULL DEFAULT NULL, CHANGE `BVN` `BVN` INT(20) NOT NULL, CHANGE `NIN` `NIN` INT(20) NULL DEFAULT NULL;
# cursor.execute("ALTER TABLE ACCOUNT_REGISTRATION CHANGE PHONE_NUMBER PHONE_NUMBER INT(20) UNIQUE")
# cursor.execute("ALTER TABLE USER_ACCOUNT CHANGE ACCOUNT_NAME ACCOUNT_NAME VARCHAR(30)")
# cursor.execute("CREATE TABLE TRANSACTION_HISTORY(ACCOUNT_NAME VARCHAR(50), ACCOUNT_NUMBER INT(20) PRIMARY KEY, TRANSACTION VARCHAR(50))")
# ALTER TABLE `TRANSACTION_HISTORY` ADD `TRANSACT_TIME` VARCHAR(100) NOT NULL AFTER `TRANSACTION`;
class Bankapp:
    def __init__(self):
         pass
    def landing_page(self):
        print("""
            FIRST BANK PLC
        """)
        print("Type R to create account of L to log in or Q to Quit")
        user_ = input("TYPE OPTION :").upper()
        if user_ == "L":
                print(".....Loading Page")
                self.login()
        elif user_ == "R":
            self.registration()
        elif user_ == "Q":
            sys.exit
        else:
            print("Invalid Input")
            self.landing_page()
    def registration(self):
        print("""
                    FIRST BANK PLC
                       Sign Up
        """)
        self.user_ = input("Enter Username")
        self.password = input("Enter Password of Atleat 5 digit ")
        verify = input("Confirm password")
        if self.password == verify:
            bankquery = "INSERT INTO USER_LOG(USER_NAME,USER_PASSWORD) VALUES(%s,%s)"
            reg_values = (self.user_,self.password)
            cursor.execute(bankquery,reg_values)
            bank_database.commit()
            print("Registration Succesfull")
            self.login()
        else:
            print("Password does not match")
            print("Do you want to quit Click Return to Retry Sign Up ")
            user = input("Type Q to quit : ")
            if user == "Q":
                sys.exit()
            else:
              self.registration()
    def login(self):
        print("""
                    FIRST BANK PLC
                       login
        """)
        try :
            global user_
            user_ = input("Enter Your User Name : ")
            user_password = int(input("Enter Password : "))
            log = input("Enter P to Proceed or Q to Quit App : ").upper()
            bankquery = "SELECT USER_NAME, USER_PASSWORD FROM USER_LOG WHERE USER_NAME = %s AND USER_PASSWORD = %s"
            log_val = (user_, user_password)
            cursor.execute(bankquery,log_val)
            log__ = cursor.fetchone()
            bank_database.commit()
            if log == "P":
                if log__:
                         print("Succesfull Login")
                         self.application()
                else:
                 print("Invalid User Log In")
                 self.login()
            elif log == "Q":
                sys.exit()
            else:
                print("Invalid Input")
                self.login()
        except ValueError:
            print("Invalid Log In ")
            self.login()
    def application(self):
            print("""
                    FIRST BANK PLC
              """)
            print("""
             1. Create FirstBank Account              

             2. Go To My Account 

             3. Register As a First Bank Agent

             4. Log Out 
            """)
            user_app = input("Select Option :")
            if user_app == "1":
                    self.register()
            elif user_app == "2":
                    self.myaccount()
            elif user_app == "3":
                    self.agent()
            elif user_app == "4":
                    self.login()    
            else:
                self.application()
    def agent(self):
        print("""
                    FIRST BANK PLC
                     first Agent
              """)
        print("""
            Service Currently Unavailable Visit Nearby First Bank Branch for Enquiries About Service
        """)
        print("""
              Enter G to Go back to Menu
        """)
        user = input("Enter Option : ").upper()
        if user == "G":
            self.registered()
    def myaccount(self):
        print("""
                    FIRST BANK PLC
                   First Mobile App
              """)
        self.time = (tm.time())
        self.date = (tm.date())
        self.current = (str(self.time)+str(self.date))
        try:
            self.acccount_number = input("Enter Account Number")
            self.pin = input("Enter your 5 digit pin")
            query = "SELECT ACCOUNT_NAME, ACCOUNT_NUMBER, USER_PIN, ACCOUNT_BALANCE FROM USER_ACCOUNT WHERE ACCOUNT_NUMBER=%s AND USER_PIN=%s"
            values = (self.acccount_number,self.pin)
            cursor.execute(query,values)
            values = cursor.fetchone()
            bank_database.commit()
            if values:
                self.registered()
            else:
                print("Invalid Account Details")
                self.myaccount()
        except IntegrityError:
            print("Please Check Your Details and enter Correct Information")
            self.myaccount()
        except ValueError:
            print("Please Insert Correct Value")
            self.myaccount()
        except DataError:
            print("Please Check Your Details and enter Correct Information")
            self.myaccount()
        except DatabaseError:
            print("Invalid User Registration")
            self.myaccount()
        except TypeError:
            print("Please Check Your Details and enter Correct Information")
            self.myaccount()
    def registered(self):
        global account_name
        print("""
                    FIRST BANK PLC
                   First Mobile App
              """)
        query = "SELECT ACCOUNT_NAME, ACCOUNT_NUMBER, USER_PIN, ACCOUNT_BALANCE FROM USER_ACCOUNT WHERE ACCOUNT_NUMBER=%s AND USER_PIN=%s"
        values = (self.acccount_number,self.pin)
        cursor.execute(query,values)
        values = cursor.fetchone()
        self.account_balance = (values[3])
        self.account_name = (values[0])
        bank_database.commit()
        print("  WELCOME"+" "+ self.account_name)
        print("""

        """)
        print("  Account Balance : "+"#"+str(self.account_balance))
        print("""

            Type Q to log Out / H to Check Transaction History

            1. Transfer  

            2. Quick Airtime     

            3. Firstmonie

            4. E-naira  

            5. Log Out  
        """)
        try:
             user_ = input("Enter Selection : ").upper()
             if user_ == "1":
                 self.transfer()
             elif user_ == "2":
                self.quickairtime()
             elif user_ == "3":
                self.firstmonie()
             elif user_ == "5":
                self.login()
             elif user_ == "Q":
                self.login()
             elif  user_ == "H":
                self.history()
        except ValueError:
                 print("Invalid Input")
                 self.registered()
    def quickairtime(self):
        print("""
                          FIRST BANK PLC
                         First Mobile App
              """)
        print("""
                Select Biller Below i.e 1 for MTN
                   Enter M to Go to Main Menu
            
            1. MTN 

            2. AIRTEL

            3. GLO

            4. 9mobile
        """)
        try:
             recharge = input("Enter Option : ").upper()
             if recharge == "1":
                recharge_no= input("Enter Phone Number : ")
                if len(recharge_no)<11 or len(recharge_no)>11:
                    print("Invalid Number")
                    self.quickairtime()
                else:
                    amount = int(input("Enter Amount"))
                    balance = self.account_balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    _time = str(tm.time())
                    _date = str(tm.date())
                    transact_time = (_date +" "+_time)
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.acccount_number)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "UPDATE TRANSACTION_HISTORY SET ACCOUNT_NAME=%s,ACCOUNT_NUMBER=%s,TRANSACTION=%s,TRANSACT_TIME=%s)"
                    updates = (self.account_name,self.acccount_number,to_transaction,transact_time)
                    cursor.execute(query2,updates)
                    bank_database.commit()
                    print("""
                    Processing Request
                    """)
                    time.sleep(5)
                    print("""
                    Recharge Succesfull
                    """)
                    self.quickairtime()
             elif recharge == "2":
                recharge_no= input("Enter Phone Number : ")
                if len(recharge_no)<11 or len(recharge_no)>11:
                    print("Invalid Number")
                    self.quickairtime()
                else:
                    amount = int(input("Enter Amount"))
                    balance = self.account_balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.acccount_number)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION) VALUES(%s,%s,%s)"
                    updates = (self.account_name,self.acccount_number,to_transaction)
                    cursor.execute(query2,updates)
                    bank_database.commit()
                    print("""
                    Processing Request
                    """)
                    time.sleep(5)
                    print("""
                    Recharge Succesfull
                    """)
                    self.quickairtime()
             elif recharge == "3":
                recharge_no= input("Enter Phone Number : ")
                if len(recharge_no)<11 or len(recharge_no)>11:
                    print("Invalid Number")
                    self.quickairtime()
                else:
                    amount = int(input("Enter Amount"))
                    balance = self.account_balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.acccount_number)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION) VALUES(%s,%s,%s)"
                    updates = (self.account_name,self.acccount_number,to_transaction)
                    cursor.execute(query2,updates)
                    bank_database.commit()
                    print("""
                    Processing Request
                    """)
                    time.sleep(5)
                    print("""
                    Recharge Succesfull
                    """)
                    self.quickairtime()
             elif recharge == "4":
                recharge_no= input("Enter Phone Number : ")
                if len(recharge_no)<11 or len(recharge_no)>11:
                    print("Invalid Number")
                    self.quickairtime()
                else:
                    amount = int(input("Enter Amount : "))
                    balance = self.account_balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.acccount_number)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION) VALUES(%s,%s,%s)"
                    updates = (self.account_name,self.acccount_number,to_transaction)
                    cursor.execute(query2,updates)
                    bank_database.commit()
                    print("""
                    Processing Request
                    """)
                    time.sleep(5)
                    print("""
                    Recharge Succesfull
                    """)
                    self.quickairtime()
             elif recharge == "M":
                    self.registered()
        except IntegrityError:
            print("Please Check Your Details and enter Correct Information")
            self.myaccount()
        except ValueError:
            print("Please Insert Correct Value")
            self.myaccount()
        except DataError:
            print("Please Check Your Details and enter Correct Information")
            self.myaccount()
        except DatabaseError:
            print("Invalid User Registration")
            self.myaccount()
        except TypeError:
            print("Please Check Your Details and enter Correct Information")
            self.myaccount()

    def firstmonie(self):
        print("""
                    FIRST BANK PLC
                  First Monie Wallet
                    
              """)
        print("""
               Service Currently Unavailable
        """)
        print("""
              Enter G to Go back to Menu
        """)
        user = input("Enter Option : ").upper()
        if user == "G":
            self.registered()
    def transfer(self):
             try:  
                print("""
                           FIRST BANK PLC
                          First Mobile App
                           Safe Transfer 
                           
                     """)
                print("""
                
                Enter Destination Account Number
                """)
                account = input("Enter Account Number : ")
                print("""
                
                Enter Amount To Transfer
                """)
                amount = int(input("Enter Amount To Transfer : "))
                if self.account_balance < amount:
                    print("Insufficient Balance")
                    self.transfer()
                else:
                    query = ("SELECT ACCOUNT_NUMBER,ACCOUNT_NAME,ACCOUNT_BALANCE FROM USER_ACCOUNT WHERE ACCOUNT_NUMBER = %s")
                    supplyvalue = (account,)
                    cursor.execute(query,supplyvalue)
                    verify = cursor.fetchone()
                    if verify:
                       destination = (verify)
                       print("Send "+ "#"+str(amount)+ "to "+ destination[1])
                       time.sleep(2)
                       enter_transactpin = input("Enter Transaction Pin")
                       if enter_transactpin == self.pin:
                            supplydestination = amount+destination[2]
                            query3 = "UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER =%s"
                            supval = (supplydestination,destination[0])
                            cursor.execute(query3,supval)
                            bank_database.commit()
                            balance = self.account_balance-amount
                            to_transaction = ("#"+str(amount)+" to "+str(account)+" "+str(destination[1]))
                            query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                            val = (balance,self.acccount_number)
                            cursor.execute(query,val)
                            bank_database.commit()
                            query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION,TRANSACT_TIME) VALUES(%s,%s,%s,%s)"
                            updates = (account_name,self.acccount_number,to_transaction,self.current)
                            cursor.execute(query2,updates)
                            bank_database.commit()
                            print("""
    
                             Verifying Transaction
                            """)
                            time.sleep(3)
                            print("Transaction Succesfull")
                            self.registered()
                       else:
                            print("Invalid Pin")
                            self.transfer()
                    else:
                       print("Invalid Account Number")
                       self.transfer()
             except:
                self.transfer()
    def register(self):
        print("""
                    FIRST BANK PLC
                   Account Creation
              """)
        try:
            self.form1 = input("ENTER FIRST NAME : ")
            self.form2 = input("ENTER LAST NAME : ")
            self.form3 = input("ENTER OTHER NAME : ")
            self.form4 = input("ENTER EMAIL ADDRESS : ")
            self.form5 = input("ENTER PHONE NUMBER : ")
            self.form6 = input("ENTER BVN : ")
            self.form7 = input("ENTER NIN : ")
            bankAccountquery = "INSERT INTO ACCOUNT_REGISTRATION(FIRSTNAME,LAST_NAME,OTHER_NAME,EMAIL_,PHONE_NUMBER,BVN,NIN) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            accoutnval = (self.form1,self.form2,self.form3,self.form4,self.form5,self.form6,self.form7)
            if len(self.form5)<11 or len(self.form5)>11:
                print("Invalid Number")
                self.register()
            elif len(self.form6)<12 or len(self.form6)>12:
                print("Invalid BVN")
                self.register()
            elif len(self.form7)<11 or len(self.form7)>11:
                print("Invalid NIN")
                self.register()
            else:
                cursor.execute(bankAccountquery,accoutnval)
                print("""
                    Processing Your Request, This May Take Few Minutes Please Wail
                """)
                time.sleep(3)
                print("""
                       Verifying Data.......
                """)
                time.sleep(2)
                bank_database.commit()
                print("registration Succesfull")
                self.accountsetup()
        except:
             print("Please Check Your Details and enter Correct Information")
             self.register()
        # except IntegrityError:
        #     print("Please Check Your Details and enter Correct Information")
        #     self.application()
        # except ValueError:
        #     print("Please Insert Correct Value")
        #     self.accountsetup()
        # except DataError:
        #     print("Please Check Your Details and enter Correct Information")
        #     self.application()
        # except DatabaseError:
        #     print("Invalid User Registration")
        #     self.application()
        # except OperationalError:
        #     print("Please Check Your Details and enter Correct Information")
        #     self.application()
        # except ProgrammingError:
        #     print("Please Wait awhile and, Try Again.")
        #     self.accountsetup()
    def history(self):
        query = "select transaction from transaction_history where account_number=%s"
        supply = (self.acccount_number,)
        cursor.execute(query,supply)
        history = cursor.fetchall()
        printh = (history)
        print("TRANSACTION HISTORY "+ self.account_name+" "+ self.acccount_number)
        index = 0
        for i in printh:
            view = i[index]
            print(view)
        index += 1
        time.sleep(10)
        self.registered()
    def accountsetup(self):
            try:
                account_Name   = (self.form1+" "+self.form2+" "+self.form3)
                # lst = range(10000,1000000000)
                # self.account_num = (random.choices(lst, k=1))
                # self.account_number = (self.account_num[0])
                self.accountbalance = 100000
                print("""
                                Set Transaction Pin
                You Can Only Enter A five Digit Transaction Pin

                """)
                self.pin = input("Enter Your Five Digit pin : ")
                if len(self.pin)>5 or len(self.pin)<5:
                    print("You Can Only Enter A five Digit Transaction Pin")
                    self.accountsetup()
                else :
                    try:
                        query = "INSERT INTO USER_ACCOUNT(ACCOUNT_NAME,USER_PIN,ACCOUNT_BALANCE,BVN) VALUES(%s,%s,%s,%s)"
                        val = (account_Name,self.pin,self.accountbalance,self.form6)
                        cursor.execute(query,val)
                        query2 = "SELECT ACCOUNT_NUMBER FROM USER_ACCOUNT WHERE BVN = %s"
                        supply =(self.form6,)
                        cursor.execute(query2,supply)
                        fetch = cursor.fetchone()
                        for i in fetch:
                             accountnumber = (fetch[0])
                        bank_database.commit()
                        print(account_Name +" "+"Your Account number is " + str(accountnumber) +" Thank You For Choosing First Bank")
                        self.customer()
                    except IntegrityError:
                        print("Please Wait awhile and, Try Again.")
                        self.accountsetup()
                    except ValueError:
                        print("Please Insert Correct Value")
                        self.accountsetup()
                    except ProgrammingError:
                        print("Please Wait awhile and, Try Again.")
                        self.accountsetup()
                    except DatabaseError:
                        print("Please Wait awhile and, Try Again.")
                        self.accountsetup()
            except:
                self.accountsetup()
    def customer(self):
                    print("Continue At login with A or Quit with Q")
                    user = input("Type Selection : ").upper()
                    if user == "A":
                        self.login()
                    elif user == "Q":
                        sys.exit()
                    else:
                        print("Invalid Input")
                        self.customer()
firstbank = Bankapp()     
firstbank.landing_page()
#------------------------------------------------------------------------|


      