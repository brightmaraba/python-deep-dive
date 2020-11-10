import requests

ngrok_url = 'https://863c190c3642.ngrok.io'

endpoint = f'{ngrok_url}/box-ofice-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.text)