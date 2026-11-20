# Two 1.series 2.dataframe

# import pandas as bijay

# data = [1,2,3,"ram"]

# data_series = bijay.Series(data, index=["hello","world","jahdj","khaj"])

# print(data_series)

# import pandas as pd

# data ={
#     "name":"Bijay",
#     "salary":10
# }

# df=pd.DataFrame(data, index=[10])
# print(df)

# import csv

# with open("students.csv", mode="r") as f:
#     data = csv.reader(f)

#     for row in data:
#         print(row)



# import pandas

# data = pandas.read_csv("students.csv")

# print(data)

# write dataframe into csv file

import pandas

employee_details = {
    "name":["Jhon","Doe","Smith"],
    "salary":[200,400,500],
    "address":["UK","USA","AUS"]
}

details_dataframe=pandas.DataFrame(employee_details)

details_dataframe.to_csv("employee.csv", mode="a", index=False)

print("Successfully changed ")