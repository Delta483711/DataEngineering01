## Import Librairies 
import pandas as pd
import requests
from io import StringIO
from init import ConnectionToDatabase
from sqlalchemy import create_engine

## Read the csv file 
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(StringIO(requests.get(url).text))

## Minor transform the csv file ##

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter: Get rows after a specific date (e.g., after 2022-01-01)
filtered_df = df[df['date'] > '2024-01-10']

## Limit the number of rows returned
trimdata = filtered_df.head(50)

print(trimdata)

## store columns in var Test 
date = trimdata["date"]

##### Connect to Neon or any other database ######

## Declare Connection variables 
username = 'neondb_owner'
password = 'npg_0aLTWcGqE1AJ'
host = 'ep-lively-term-abff86z3-pooler.eu-west-2.aws.neon.tech'
port = '5432'
database = 'neondb'
sslmode = 'require'  # Neon requires SSL

## run the connection function 
ConnectionToDatabase(username,password,host,port,database,sslmode)

## Save to database 
##connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}?sslmode={sslmode}"
##engine = create_engine(connection_string)

##trimdata.to_sql("CovidCSVTest", engine, schema="raw", if_exists="replace", index=False)

##print(" Data written to Neon!")











                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        