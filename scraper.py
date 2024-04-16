import requests 

response = requests.get (
    url = ""
)

print(response.status.code)

