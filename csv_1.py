# CSV file - Comma Separated Value
# CSV module: It is python inbuilt module that helps to interact with csv file
# It allows: read data, write data, add data
# csv.reader() = It helps to read/retrive data from csv file
# csv.writer() = It helps to write data in a csv file
# writerow() = it helps to write single row at a time
# writerows() = It helps to write multiple rows at a time

# mode of file operation
# read = "r"
# write = "w"
# append = "a"

# First step is to import
# import csv

# f=open("students.csv","r")

# xyz = csv.reader(f)

# # print(datas)
# for data in xyz:
#     print(data)
#     # print(type(data))

# f.close()


# import csv

# with open("students.csv","r") as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)



# print(list(range(5)))

# for i in range(5):

import csv
with open("students.csv","a", newline="") as f:
    data = csv.writer(f)

    rows=[
        ["Ram","Tertayug"],
        ["Sita","Teretayug"],
        ["Krishna","Dwaparyug"],
        ["Radha","Dwaparyug"]
    ]
    data.writerows(rows)

    # data.writerow(["Name", "Address"])
    # data.writerow(["Bijay", "Manjhariya"])



    # Write a program to store name, salary and position of a employee in a school.