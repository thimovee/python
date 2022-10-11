import pandas as pd
file_loc = "datavis\sales_data.xlsx"
df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols=['_SalesTeamID'])
x = 1
z = 0
while x < 29:
    print("\nSales team " + str(x))
    print("Total sales " + str(len(df[df['_SalesTeamID'] == (x)])))
    z = z + len(df[df['_SalesTeamID'] == (x)])
    x = x+1
average = z/29
print("\nAverage sales per team: " + str(average) + "\n")
d = 1
while d < 29:
    d = d+1
    t = len(df[df['_SalesTeamID'] == (d)])
    if t < average:
        print("Sales team " + str(d) + " has below average sales")