import pandas as pd


df=pd.read_csv('student_sample_data.csv')
#print(df)

#student result

total=df.groupby("Name")["Marks"].sum()
average=df.groupby("Name")["Marks"].mean()

result=pd.DataFrame({"Total":total,"Average":average})
#print(result)

#find topper

#topper=df.groupby("Name")["Marks"].sum().sort_values(ascending=False)

#print(topper.nlargest(1))

#print(topper.head(1))


#subjectwise analysis

# subject=df.groupby("Subject")["Marks"].mean()
# result=pd.DataFrame({"Subject":subject})
# print(result)

#result

df["Result"]=df["Marks"].apply(
    lambda x: "Pass" if x>=40 else "Fail"
)
print(df)

pivot=pd.pivot_table(values="Marks",index="Name",columns="Subject",data=df)
print(pivot)

