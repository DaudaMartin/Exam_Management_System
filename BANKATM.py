from cProfile import run
from sqlite3 import connect
import mysql.connector as sql
import pyttsx3 
import sys
import time 
import os
import datetime as dt
machine = pyttsx3.init()
bank_database = sql.connect(host="127.0.0.1", user="root", password="", database="_ACCOUNT_DATABASE")
cursor =bank_database.cursor()
tm = dt.datetime.now()
robot_voice = machine.getProperty('voices')
machine.setProperty('voice',robot_voice[38].id)
rate = machine.getProperty('rate')
machine.setProperty('rate',180)
machine.say("Hello ........... Welcome to First Bank")
machine.runAndWait()
class ATM:
    def __init__(self):
        pass
    def welcomepage(self):
        try:
            machine.say("Enter Your Transaction Details")
            machine.runAndWait()
            print("""
                    Welcome to First Bank

                Please Enter Your Transaction Details
            """)
            self.accountnumber = input("Enter Your Account Number : ") 
            self.user = input("XXXXX : ")
            query = "SELECT USER_PIN, ACCOUNT_BALANCE,ACCOUNT_NUMBER, ACCOUNT_NAME FROM USER_ACCOUNT WHERE ACCOUNT_NUMBER = %s"
            supply = (self.accountnumber,)
            cursor.execute(query,supply)
            fromaccnt = cursor.fetchone()
            pin = fromaccnt[0]
            self.balance = fromaccnt[1]
            self.account_name = fromaccnt[3]
            if fromaccnt:
                self.transaction()
                # self.transaction()
            else:
                print("Invalid Input Take Your Card")
        except:
            self.welcomepage()
    def transaction(self):
             try:
                 print(""""
                    1: Withdrawal                     2: Transfer 

                    3: Register Account               4: TOP-up Airtime

                    5: Check Account Balance          6: Register First Bank Account

                 """)
                 selectinput = input("Enter Option")
                 if selectinput == "1":
                     self.withdrawal()
                 elif selectinput == "2":
                     self.Transfer()
                 elif selectinput == "3":
                     self.register()
                 elif selectinput == "4":
                     self.quickairtime()  
                 elif selectinput == "5":
                     self.CheckBalance()     
                 elif selectinput == "6":
                     print("Service Unavailable")
                     self.welcomepage()
             except:
                self.welcomepage()
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
                        Processing Your Request, This May Take Few Minutes Please Wait
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
                        self.welcomepage()

            except:
                self.accountsetup()
    def CheckBalance(self):
         print("Your Account Balance #"+str(self.balance))
    def withdrawal(self):
            print("""
                   FIRST BANK ATM 
            """)
            transaction = {1:1000,2:20000,3:5000,4:10000,5:15000,6:20000}
            for key, value in transaction:
                print(key,value)
            user = ("Enter Option")
            if user == key:
               balance = 1000000-value
               print(balance)
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
                    balance = self.accountbalance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    _time = str(tm.time())
                    _date = str(tm.date())
                    transact_time = (_date +" "+_time)
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.accountnumber)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "UPDATE TRANSACTION_HISTORY SET ACCOUNT_NAME=%s,ACCOUNT_NUMBER=%s,TRANSACTION=%s,TRANSACT_TIME=%s)"
                    updates = (self.account_name,self.accountnumber,to_transaction,transact_time)
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
                    balance = self.balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.accountnumber)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION) VALUES(%s,%s,%s)"
                    updates = (self.account_name,self.accountnumber,to_transaction)
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
                    balance = self.balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.accountnumber)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION) VALUES(%s,%s,%s)"
                    updates = (self.account_name,self.accountnumber,to_transaction)
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
                    balance = self.balance-amount
                    to_transaction = ("#"+str(amount)+" to "+str(recharge_no))
                    query = ("UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE = %s WHERE ACCOUNT_NUMBER = %s")
                    val = (balance,self.accountnumber)
                    cursor.execute(query,val)
                    bank_database.commit()
                    query2 = "INSERT INTO TRANSACTION_HISTORY(ACCOUNT_NAME,ACCOUNT_NUMBER,TRANSACTION) VALUES(%s,%s,%s)"
                    updates = (self.account_name,self.accountnumber,to_transaction)
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
                    self.transaction()
        except:
            print("Please Check Your Details and enter Correct Information")
            self.welcomepage()

    def Transfer(self):
        print("""
                FIRST TRANSFER
               Safe Transaction
        """)
        destination = input("Enter Destination Account Number")
        query = "SELECT ACCOUNT_NUMBER,ACCOUNT_BALANCE,ACCOUNT_NAME FROM USER_ACCOUNT WHERE ACCOUNT_NUMBER=%s"
        supply=(destination,)
        cursor.execute(query,supply)
        details=cursor.fetchone()
        accnum = (details[0])
        balance = (details[1])
        name = (details[2])
        if details:
            user_ = int(input("Enter Amount To Transfer"))
            print("You want to Transfer #"+str(user_)+" To "+str(accnum) +"\n"+name)
            for i in range(0,5):
                machine.say("Please Wait Your Transaction Is Processing")
                machine.runAndWait()
            transaction = int(self.balance) - int(user_)
            beneficiary = balance + user_
            query = "UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE=%s WHERE ACCOUNT_NUMBER=%s"
            supply = (transaction,self.accountnumber)
            cursor.execute(query,supply)
            query_ = "UPDATE USER_ACCOUNT SET ACCOUNT_BALANCE=%s WHERE ACCOUNT_NUMBER=%s"
            supply_ = (beneficiary,destination)
            cursor.execute(query_,supply_)
            bank_database.commit()
            bank_database.close()
        else:
            print("Invalid Account Details")
            self.Transfer()
firstbankATM = ATM()
firstbankATM.welcomepage()
