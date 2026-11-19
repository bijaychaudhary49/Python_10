# import panda as pd
# import pandas
# data=[1,2,3]
# data_series = pandas.Series(data, index=["Bijay","ahj","kjad"])
# print(data_series)

# using dictionary
# import pandas

# data = {
#     "name": ["Bijay", "Ram", "Ram"],
#     "age":[24,23,11],
#     "address":["Ramgram-10",3,4]
# }
# df = pandas.DataFrame(data)
# print(df)

# using list
import pandas 

ram = [
    ("ram","1"),
    ("shyam",2),
]

df = pandas.DataFrame(ram,columns=["name","age"])
print(df)