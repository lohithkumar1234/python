# student mark claculate
name = input("Enter student name" )
m1 = int(input("enter python mark:"))
m2 = int(input("Enter java mark:"))
m3 = int(input("enter sql marks:"))

total =m1+m2+m3
average =total/3

print("\n---------student report---------")
print("name:", name)
print("total:", total)

#students scholarship eligibility checker
mark = float(input("enter marks:"))

attendance = float(input("enter attendance:"))

eligible = mark>=85 and attendance >=75
print ( "scholarship eligible:", eligible)
