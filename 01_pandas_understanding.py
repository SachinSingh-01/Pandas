# import numpy as np
# import pandas as pd
# labels=['a','b','c']
# my_list=[10,20,30]
# arr=np.array([10,20,30])
# d={1:10,2:20,3:30}
# l=pd.Series(my_list)
# list_index=pd.Series(my_list,index=labels)
# s=pd.Series(arr)
# print(s)
# print(list_index)


# import numpy as np
# import pandas as pd
# data={
#     'Name':["John","Anna","Sachin","Boss"],
#     'Age':[20,56,75,34],
#     'city':['newyork','paris','london','brazil'],
#     'salary':[65000,70000,90000,50000]
# }
# df=pd.DataFrame(data)
# print(df)


# import numpy as np
# import pandas  as pd
# data_list=[
#     ['John',28,'New York',65000],
#     ['Anna',34,'Paris',70000],
#     ['Peter',29,'Berlin',62000],
#     ['Sachin',42,'America',85000]
# ]
# df2=pd.DataFrame(data_list)
# print(df2)
# columns=["Name","Age","City","Salary"]
# df2=pd.DataFrame(data_list,columns=columns)
# print(df2)

# print("Particular column")
# particular_column=df2["Name"]
# print(particular_column)

# print("Particular two column")

# particular_column1=df2[["Name","City"]]
# print(particular_column1)

# print("Creating new column")
# new_column=df2["Designation"]=["Doctor","Eng.","Cricketer","AI/ML Eng."]
# # print(new_column)
# print(df2)

# print("To remove column")
# remove=df2.drop("Designation",axis=1)
# print(remove)

# permanent_remove=df2.drop("Designation",axis=1,inplace=True)
# print(df2)

# print("Selecting Rows")
# rows=df2.loc[[3,1]]
# print(rows)

# rows=df2.iloc[3]
# print(rows)

# print("Selecting subset of rows and columns")
# subset=df2.loc[[0,1], ["City","Salary"]]
# print(subset)

# print("Conditional Selection")
# greater_age=df2[df2["Age"]>30]
# print(greater_age)

# print("Age greater than 30 and city must be paris")
# both=df2[(df2["Age"]>30)&(df2["City"]=="Paris")]
# print(both)

# import numpy as np
# import pandas as pd
# data={
#     'A':[1,2,np.nan,4,5],
#     'B':[np.nan,2,3,4,5],
#     'C':[1,np.nan,np.nan,np.nan,5],
#     'D':[1,np.nan,np.nan,np.nan,5]
# }
# df=pd.DataFrame(data)
# print(df)
# print("Check null")
# null_check=df.isna()
# print(null_check)

# print("Check number of null value in each row")
# count_null=df.isna().sum()
# print(count_null)

# print("Check kya haar column mai null value present hai ki nahi")
# column_null=df.isna().any()
# print(column_null)

# print("Remove entire data")
# remove=df.dropna()
# print(remove)
# print("Remove only row where 3 null value present")
# null_3_remove=df.dropna(thresh=3)
# print(null_3_remove)

# print("Filling 0 in place of null")
# filling=df.fillna(0)
# print(filling)
# values={"A":0,"B":100,"C":300,"D":400}
# put_values=df.fillna(value=values)
# print(put_values)

# print("Fill mean value in place of null")
# mean=df.fillna(df.mean())
# print(mean)

import numpy as np
import pandas as pd
employees={
    "employee_id":[1,2,3,4,5],
    "name":["John","Anna","peter","linda","Bob"],
    "department":["HR","IT","Finance","IT","HR"]
}
salaries={
    "employee_id":[1,2,3,4,5,6,7],
    "salary":[60000,65000,70000,90000],
    "bonus":[5000,10000,7000,8000,12000]
}
d1=pd.DataFrame(employees)
d2=pd.DataFrame(salaries)
print(d1)
print(d2)

pd.merge(employees,salaries,on="employee_id",how="inner")
pd.merge(employees,salaries,on="employee_id",how="outer")

import numpy as np
import pandas as pd
df1=pd.DataFrame({
    "A":["A0","A1","A2"],
    "B":["B0","B1","B2"],
    "C":["C0","C1","C2"]
})
df2=pd.DataFrame