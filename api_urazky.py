import requests

parameters = {
    "lang": "cs",
    "type": "json"
}
response = requests.get("https://evilinsult.com/generate_insult.php", params= parameters)
response.raise_for_status()
data = response.json()

print(data["insult"])