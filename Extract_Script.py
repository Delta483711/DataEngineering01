

import requests
import pandas as pd

BASE_URL = 'https://api.covid19api.com'

def get_covid19_data(country=None):
    if country:
        endpoint = f"{BASE_URL}/dayone/country/{country}"
    else:
        endpoint = f"{BASE_URL}/summary"
        
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

# Fetch global COVID-19 summary
global_data = get_covid19_data()
print("Global Summary:")
print(global_data['Global'])

# Fetch country-specific COVID-19 data
country_data = get_covid19_data(country="united-kingdom")
print("\nUK Day One Data:")
print(pd.DataFrame(country_data).head())




##https://www.omi.me/blogs/api-guides/how-to-fetch-covid-19-data-using-covid-19-api-in-python?srsltid=AfmBOoqV0tCWposskBXLRBZjlL6n3DwPz6Xhs1VWfeElHwXnqslh4dza

##https://api.covidtracking.com
