import pandas as pd
df = pd.read_excel("E:\งานทุกอย่างภีม\Coding\Python\Pandas1\Data Example\Excel\Stock.xlsx",index_col="Name")
df["delivery"] = 100
df["total"] = df["delivery"]+df["Price"]
cols = {"Category":"Group", "Amount":"Quantity", "total":"Summation"} #{new:old}
df.rename(columns=cols, inplace=True)#.rename(columns))
df.drop("delivery",axis=1,inplace=True) #.drop(col,axis=0(row)//1(column)
print(df)