import requests

url = "https://quotel-quotes.p.rapidapi.com/quotes/random"

payload = {}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "8eab0d1d70mshc50857f18e3f763p1256cajsnd8f01ee1a4a6",
	"X-RapidAPI-Host": "quotel-quotes.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())