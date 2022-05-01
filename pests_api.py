import config
import requests

url = "https://texaspanhandlevectors.com"

headers_dictionary = {
    "authorization": "bearer " + config.api_key
}

params_dictionary = {
    "term": "west nile virus",
    "location": "amarillo, tx"
}
response = requests.get(url, headers=headers_dictionary,
                        params=params_dictionary)
result = response.json()
