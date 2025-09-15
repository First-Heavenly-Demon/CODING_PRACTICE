import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()

# Extract the Bitcoin price in USD
usd_price = data["bpi"]["USD"]["rate"]
time_updated = data["time"]["updated"]

print("As of", time_updated, "Bitcoin price is USD", usd_price)
