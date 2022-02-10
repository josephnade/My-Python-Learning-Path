import requests
import json

to_currency = input("What currency do you want to exchange: ")
budget = int(input("How much money do you want to exchange: "))

re = json.loads(requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=1a94ca9cae749dce4c2a54be1641c04b").text)
result =  re["rates"][to_currency] * budget
print(f"EUR to {to_currency} = {result}")

