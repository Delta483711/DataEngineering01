## New Extract Covid Data File ##

import pandas as pd
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(StringIO(requests.get(url).text))

# Save locally
df.to_csv("data/raw/owid_covid_data.csv", index=False)