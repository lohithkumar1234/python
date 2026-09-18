#set i python 
# set is order and multiple

#set is a collection of unique value that is unordered and mutable


number = {10,20,30,20,10}
print(number)

# why use set ?
#suppose students have selected subject.

#add values to set 
subjects = {"python","java"}
subjects.add("SQL")
print( subjects)

#remove values froma set 
subjects.remove("java")
print(subjects)




#sets  do not allow duplicate values.
number = {1,2,2,3,3,4}
print(number)
#dictionary in python 
#dictionary is acollection  of key -value pairs that is unordewred and 

student = {
    "name": "lohith",
    "age": 18,
    "cource": "python"
}

print(student)

#access element in dic
print(student["name"])
print(student["age"])
print(student["cource"])
#add new data to a dictionary
student["city"] = "vijayawada"

print(student)


print(student.keys())

# key () returns all the keys in the dicitionary 
print(student.values())

#values () returns all the value in the dicitionary
print(student.items())

#items () returns all key -value pair 
print(student.get("name"))
# get() returns all key-value pairs 

student.update({"age": 22}) 
# update() update the value of the specified key
print(student)
student.pop("age")

# pop() remove the specified and irs value
print(student)
#popitem() remove the  last instered key-values pair
student ={
    "name":"lohith",
    "age":18,
    "course":"python"
}
student.popitem()
print()

student = {
    "name": "lohith",
}
student.setdefault("age",21)

print(student)




