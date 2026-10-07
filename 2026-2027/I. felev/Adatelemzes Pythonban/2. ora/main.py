import pandas as pd

wine_rev = pd.read_csv("./winemag.csv")

wine_rev.loc[wine_rev.country == "Italy"]