## Import Librairies 
import pandas as pd
import requests
from io import StringIO
from init import ConnectionToDatabase
import os 

## Read the csv file 
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(StringIO(requests.get(url).text))

## Minor transform the csv file ##

## Limit the number of rows returned
trimdata = df.head(50)
print(trimdata)

## store columns in var Test 
date = trimdata["date"]
print(date)

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

