# A python code to design an ATM machine
import sys
import csv
from unit_test import substract, add
# start by defining some functions to make our code stress free
def substract(a, b):
    return a - b

def add(a, b):
    return a + b

def withdraw(accBalance, amount):
     
    newBalance = substract(accBalance, amount)
    return newBalance

def deposit(accBalance, amount):
    newBalance = add(accBalance, amount)
    return newBalance

def thanks():
     print("Thank you for banking with CHIBANKS")

#welcoming the user and assigning values to some variables
def main():
    print("WELCOME TO CHIBANK")
    
    balance= 0
    user_index= 0
    students= []
    login_successful= False
    counter= 0
    with open("student.csv") as file:
        for line in file:
            try:
                name, password, mybalance= line.rstrip().split(",")
                student= {"name": name, "password": password, "balance": int(mybalance)}
                students.append(student)
            except ValueError:
                pass   
           
#           if len(sys.argv)== 3:
            if sys.argv[1]== name and sys.argv[2]== password:
               
                login_successful= True
                balance= int(mybalance)
                user_index= counter
                print(user_index)
            counter += 1
#                user_data=[name, password, balance]
    if not login_successful:
        print("wrong username or password entered")     
#    print(students[5])
#inputs your pin and checks if its correctso as to display your available balance
     

    #if balance is displayed, it prompts the user to select between 1,2 or 3 for the next line of action that would be performed
    #if the user selects "1", it askes "how much" and then shows available balance by deducting the amount withdrawn from the initial balance
            #money = input("1: withdraw or 2: deposit or 3: exit: ")
    while login_successful:
        money = input("1: withdraw or 2: deposit or 3: transfer or 4: exit:")  
        match money:              
            case "1":
                user_withdraw= int(input("how much: "))
                print( "you have withdrawn #",user_withdraw, "from your account")
                if user_withdraw > balance:
                    print("you don't have sufficient funds")
                    thanks()
                else:
                    balance= withdraw(balance, user_withdraw)
                    print("your balance after withdrawal is: ",balance)
                    thanks()
                    

# else if the user selects "2", it shows "how much" and then shows the total balance                
            case "2":
                user_deposit= int( input("how much: "))
                print( "you have deposited #",user_deposit, "to your account")                        
                print("oshey plenty money to spend!")
                balance= deposit(balance, user_deposit)
                print ("your balance after deposit is: ", balance)
                thanks()
                
            case "3":
                user_name= input("pls what is your name? ")
                for student in students:
                    if student["name"]== user_name:
                        amount = int(input("how much to transfer: "))
                        student ["balance"]+= amount
                        balance= balance - amount
                        if amount> balance:
                            print("sorry, your available balance is low")
                            thanks()
                        else:
                            print("your balance after transfer to ", student["name"], "is ", balance )
                            print("transfer successful")
                            thanks()   

# if user selects "3", thank you for banking with us!                 
            case "4":
                thanks()
#                print(students[user_index])
                try:
                    students[user_index]["balance"]= balance
                    print(students[user_index]["balance"])
                except IndexError:
                    pass
                with open("student.csv", "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["name", "password", "balance"])
                    for student in students:
                        writer.writerow({"name": student["name"],"password": student["password"], "balance": student["balance"]})
                break
            
                                          
                    # else:
                    #     print("username not found")
                    #     thanks()
                            
                # with open("student.csv", "w") as file:
                #     writer = csv.DictWriter(file, fieldnames=["name", "password", "balance"])
                #     for student in students:
                #         writer.writerow({"name": student["name"],"password": student["password"], "balance": student["balance"]})
                
                
            case _:
                print("please call the security")
                continue



        
                    
    
                 
        



if __name__ == "__main__":
    main()       


