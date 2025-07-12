import requests 
import pandas as pd 
import datetime
import psycopg2
from sqlalchemy import create_engine

StartDate = datetime.datetime(2025, 1, 1)
StopDate = datetime.datetime(2025, 7, 1)

#Create a function to store the API Call 
def get_uk_historical():
    url = "https://disease.sh/v3/covid-19/historical/UK?lastdays=10"
    response = requests.get(url)

#Check if the Response was successful
    if response.status_code == 200:
        result = response.json()
        #Process the result
         #Extract part of the JSON
        timeline = result['timeline']
        #Convert to dataFrames
        cases_df = pd.DataFrame(timeline['cases'].items(), columns=['date', 'cases'])
        deaths_df = pd.DataFrame(timeline['deaths'].items(), columns=['date', 'deaths'])
        recovered_df = pd.DataFrame(timeline['recovered'].items(), columns=['date', 'recovered'])
        df = cases_df.merge(deaths_df, on='date').merge(recovered_df, on='date')

        return df
    else:
        ##Error message
        print('Failed')
        raise Exception(f"Failed to fetch data: {response.status_code}")

resultlist = get_uk_historical()

print(resultlist)

##### Connect to Neon or any other database ######

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
    print(" Successfully connected to Neon PostgreSQL!")
    connection.close()

except Exception as e:
    print(" Connection failed:", e)


##### pass the data into the Neno #####


## Connection string 
connection_string = "postgresql+psycopg2://neondb_owner:npg_0aLTWcGqE1AJ@ep-lively-term-abff86z3-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# Create engine and write data
engine = create_engine(connection_string)
resultlist.to_sql("covid_test", engine, schema="raw", if_exists="replace", index=False)

print(" Data written to Neon!")