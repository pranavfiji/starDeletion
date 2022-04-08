import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)
del df["hyperlink"]

print(df.shape)

del df["temp_star_data"]
del df["temp_star_mass"]
del["star_letter"]
del["star_name"]
del df["star_controvflag"]
del df["star_pnum"]
del df["star_orbper"]
del df["star_orbpererr1"]
del df["star_orbpererr2"]
del df["star_orbperlim"]
del df["star_orbsmaxerr1"]
del df["star_orbsmaxerr2"]
del df["star_orbsmaxlim"]
del df["star_orbeccen"]
del df["star_orbeccenerr1"]
del df["star_orbeccenerr2"]
del df["star_orbeccenlim"]
del df["star_orbinclerr1"]
del df["star_orbinclerr2"]
del df["star_orbincllim"]


print(df.shape)
df.to_csv("main.csv")
