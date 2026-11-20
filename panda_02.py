# import pandas

# data = pandas.Series(["Ram", "shyam"])
# print(data)

# details = {
#     "name":"Bijay",
#     "age":22
# }

# df = pandas.DataFrame(details, index=[10])
# print(df)

# import pandas as pd

# data = pd.read_csv("students.csv")

# print(data.to_string(index=False))

import pandas as pd

student_details = {
    "name":["Bijay","Ram"],
    "age":[2,3]
}

df = pd.DataFrame(student_details)

data = df.to_csv("students.csv", index=False, mode="a", sep="-")

print("Data added successfully")