import requests
import pandas as pd





##https://www.omi.me/blogs/api-guides/how-to-fetch-covid-19-data-using-covid-19-api-in-python?srsltid=AfmBOoqV0tCWposskBXLRBZjlL6n3DwPz6Xhs1VWfeElHwXnqslh4dza

##https://api.covidtracking.com

BASE_URL = 'https://api.covidtracking.com'

def get_covid19_data(country=None):
    endpoint = f"{BASE_URL}summary"
    if country:
        endpoint = f"{BASE_URL}dayone/country/{country}"
        
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Fetch global COVID-19 summary
global_data = get_covid19_data()
print(global_data)

# Fetch country-specific COVID-19 data
country_data = get_covid19_data(country="us")
print(country_data)