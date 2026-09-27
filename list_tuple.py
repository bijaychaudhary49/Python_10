name1 = "Abha"
name2 = "Ankit"
name3 = "Alisha"


list = ["Abha", "Ankit", "Alisha", "Akriti", "Aman","Bijay","Ram","Bijay"] #lsit = [1,2,3,4,]
# list[0]="Jyoti"
# print(list)
# str = "Bijay"
# print(str.lower())
# print(str)
# print(str[0])
# () = tuple
# {} = set/dict
# collection of item/element that can be of different datatype or similar also
# It is squence/ order sequence. so they have their own position which is called index
# and index always starts from 0 and goes on.
# Elements of list can be accessed by using their index and syntax list_name[index]
# List are mutable variable
# Mutable means: the value can be changed. new value can be added, remove, modify
# immutable: that cannot be changed (value)
# print(list.append("Bibek"))
# list.insert(2,"Bibek")
# print(list)
# list.sort(reverse=True)
# print(list.count("Bijay"))
# print(list.index("Bijay"))
# list.remove(1)
# list.pop()
# print(list)
# print(list)


# tup = ("Bijay","Prabin","Amrit","Arun","Sunil") #Immutable variable () parenthesis eg:tup=(1m2,2,3,3)
# print(tup[1])

# set = unorder collection. element cannot be accessed using the index. defined using {}.set contains only unique element

# set1 = {1,4,2,3,"Bijay"}
# set2 = {"ram","shyam","Bijay"}
# # # print(set.add(10))

# print(set1.difference(set2))

# dictionery: data structure which store data in key-value pair
# can be defined using curly bracket {}
employee_details = {
    "name": "Bijay",
    "age":23,
    "contact_number": 980000,
    "address":"Ramgra,-10",
}

employee_details.update({"23":"45"})
# employee_details.pop("age")
# employee_details.clear()
print(employee_details)

# A = {1,2,3,4}
# B={3,4,5,6}
# print(A.union(B))