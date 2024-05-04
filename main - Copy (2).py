import pickle
import os
import pathlib
class Account :
    acc_no = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(main):
        main.acc_no= int(input("Enter the account no : "))
        main.name = input("Enter the account holder name : ")
        main.type = input("Ente the type of account [C/S] : ")
        main.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")
    
    def showAccount(main):
        print("Account Number : ",main.acc_no)
        print("Account Holder Name : ", main.name)
        print("Type of Account",main.type)
        print("Balance : ",main.deposit)
    
    def modifyAccount(main):
        print("Account Number : ",main.acc_no)
        main.name = input("Modify Account Holder Name :")
        main.type = input("Modify type of Account :")
        main.deposit = int(input("Modify Balance :"))
        
    def depositAmount(main,amount):
        main.deposit += amount
    
    def withdrawAmount(main,amount):
        main.deposit -= amount
    
    def report(main):
        print(main.acc_no, " ",main.name ," ",main.type," ", main.deposit)
    
    def getAccountNo(main):
        return main.acc_no
    def getAcccountHolderName(main):
        return main.name
    def getAccountType(main):
        return main.type
    def getDeposit(main):
        return main.deposit
    

def intro():
    print('''Welcome to JV
Presented by-
Vijeta Priya
Jaya Ambastha
Co-presented by-
Shipra Mam''')


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.acc_no," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No records to display")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.acc_no == num :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.acc_no == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.acc_no != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.acc_no == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
ch=''
num=0
intro()

while ch != 8:
    print('''\tMAIN MENU
         \t1. NEW ACCOUNT
         \t2. DEPOSIT AMOUNT
         \t3. WITHDRAW AMOUNT
         \t4. BALANCE ENQUIRY
         \t5. ALL ACCOUNT HOLDER LIST
         \t6. CLOSE AN ACCOUNT
         \t7. MODIFY AN ACCOUNT
         \t8. EXIT
         \tSelect Your Option (1-8) ''')
    ch = input()

    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank management system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    


    
    
    
    
    
    
    
    
    
    
