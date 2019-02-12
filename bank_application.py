import re
import sys
import datetime 
class Sitanshu_Bank:
    
    ''''Customer class with bank related operations'''
    no=1000
    cbank="Sitanshu_Bank"
    
    def __init__(self):
        
        ''''Constructor to initialize instance variable and take user input'''
        
        self.accno = "sitanshu_bank0" + str(Sitanshu_Bank.no)
        self.name=input("Enter Name:")
        while True:
            self.mob=input("Enter Phone no")
            m=re.fullmatch('[6-9]\d{9}',self.mob)
            if m==None:
                print("Please Number Valid Mobile Number")
            else:
                break
        while True:
            self.dob=input("Enter date of birth in format 'dd/mm/yy'")
            day,month,year=self.dob.split('/')
            isvaliddate=True
            try:
                datetime.datetime(int(year),int(month),int(day))
            except ValueError:
                print("Enter validate Number")
                isvaliddate=False
            if(isvaliddate):
                break
            else:
                print("Input Dob is not valid")
        
        Sitanshu_Bank.no=Sitanshu_Bank.no + 1
        self.amount=int(input("Enter mimimum amount"))
    def display(self):
        
        ''' Method to display the user information'''
        
        print(self.accno, " ", self.name, " ",self.dob, " ", self.mob," ", self.amount)
    @staticmethod
    def deposit():
        
        ''' method to deposit amount to the bank'''
        
        acc_match=input("Enter the account number")
        for item in store:
            if item.accno == acc_match:
                add=eval(input(("enter the amount to be added")))
                item.amount+=add
                print("Now,balance in your account after credited  is",item.amount)
        else:
            print("Please provide correct user account number")
    @staticmethod
    def withdrawl():
        
        ''' method to withdrawl amount from the bank'''
        
        acc_match=input("Enter the account number")
        for item in store:
            if item.accno == acc_match:
                withdrawl=eval(input(("enter the amount to be debited")))
                if(item.amount-withdrawl<500):
                    print("XXXXX Low balance XXXX")
                else:
                    print("Now,balance in your account after debited",(item.amount-withdrawl))
                
            else:
                print("Please provide correct user account number")
    
    
store=[]

while True:
    print(""".........................................................................
             .                                                                       .
             .                      Welcome to the Sitanshu Bank                     .
             .                                                                       .
             .........................................................................""")
    print("Press The Following Keys To Perform the Required Options")
    print("1. Crete Account")
    print("2. Display All Account")
    print("3. Display Account by account number")
    print("4. Deposit your money")
    print("5. Withdraw your money")
    print("7. Exit")
    ch= int(input("Enter choice : "))
    if ch==1:
        nw = Sitanshu_Bank()
        store.append(nw)
    elif ch == 2:
        for a in store:
            a.display()
    elif ch == 3:
        acno = input("Enter account number : ")
        for a in store:
            if a.accno == acno:
                a.display()
    elif ch == 4:
        Sitanshu_Bank.deposit()
    elif ch == 5:
        Sitanshu_Bank.withdrawl()
    elif ch==7:
        break
        
        
        
