import requests
import pandas as pd

# Extract data from API

def extract_data_by_api(api_url):
    response = requests.get(api_url)
    data = response.json()
    return pd.DataFrame(data)


