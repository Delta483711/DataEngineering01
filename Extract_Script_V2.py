## New Extract Covid Data File ##

import pandas as pd
import requests
from io import StringIO


## Read the csv file 
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(StringIO(requests.get(url).text))


## transform the csv file 



##Get number of rows
rownum = df.head(1)


## store columns in vars 
date = df["date"]

print(rownum)



# Save locally
#df.to_csv("data/raw/owid_covid_data.csv", index=False)


## Save to database 