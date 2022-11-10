import pandas as pd


df1 = pd.DataFrame([["1", "2", "4"], ["2", "3", "4"]], columns=["A", "B", "C"])
df2 = pd.DataFrame([["1", "2", "4"], ["3", "4", "5"]], columns=["A", "B", "C"])

df = pd.concat([df1, df2])
print(df)

df_groupby = df.groupby(['A', 'C'])

df_groupby = df_groupby['B'].apply(lambda x: "&&".join(x)).reset_index()
print(df_groupby)

