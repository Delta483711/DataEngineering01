## New Extract Covid Data File ##

import pandas as pd
import requests
from io import StringIO
import psycopg2
import os


## Read the csv file 
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(StringIO(requests.get(url).text))


## transform the csv file ##



##Get number of rows
trimdata = df.head(50)
print(trimdata)



## store columns in var Test 
date = trimdata["date"]
print(date)


  ##### Connect to Neon or any other database ######

def ConnectionToDatabase():
## Declare variables 
    username = 'neondb_owner'
    password = 'npg_0aLTWcGqE1AJ'
    host = 'ep-lively-term-abff86z3-pooler.eu-west-2.aws.neon.tech'
    port = '5432'
    database = 'neondb'
    sslmode = 'require'  # Neon requires SSL

## Test connection  
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password,
            port=port,
            sslmode=sslmode
        )
        print("Successfully connected to Neon PostgreSQL!")
        connection.close()
    except Exception as e:
        print(" Connection failed:", e)

## Save to database 

ConnectionToDatabase()