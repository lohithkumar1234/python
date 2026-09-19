number = int(input("enter a number: "))
if number% 5 == 0:
    print("dividible by 5")



    # temperatue 
    temperature = float(input("enter temperature:"))
    if temperature> 40:
     print("high temperature")

# marks
marks = int(input("enter marks:"))

if marks >= 40:
   print("pass")
else:
   print("fail")

number = int (input("enter a number:"))
if number >=0:
   print("positive")
else:
   print("negative")


   number = int(input("enter a number:"))

if number > 100:
      
      print("number is greater than 100")

else:

   print(" number is not greater than 100")
   # atm amount withdrawal

balance = float(input("enter balance:"))
amount = float(input("enter withdrawal amount:"))
if amount >0:
    if amount<=balance:
       balance= balance-amount
       print("withdawal sucessfully")
       print("remaining balance:", balance) 
    else:
        print("insufficient balance")   
else:
      print("invalid amount")   

           # login moment
username = input("enter username:")
password = input("enter password:")
if username == "admin":
    if password == "12345":
        print("login sucessful")
    else:
        print("wrong password")    
else:
    print("wrong username")      
   
