import requests 
import pandas as pd 
import datetime

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


##### Connect to Neon 



        



