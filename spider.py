import requests
import json
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from decrypter import decrypt
import gender_guesser.detector as gender

URL = "https://directory.ubc.ca/"
POST = "index.cfm?d=-39Z4V%3F%2A%3DH%3CJIFX-%3B%3E%40%20%20"

NAMES = [
    "Rensink Ronald",
    "Yoon Dongwook",
    "Yim Annie",
    "Wilson Eric",
    "Wolfman Steven Andrew",
    "Munzner Tamara",
    "Traviss Karol",
    "Thorogood Miles",
    "Shriver Chelsea G",
    "Raussendorf Robert"
]

form_data = {
    'keywords': '',
    'andorexactkeywords': 'start',
    'submitAnd': 'search using exact fields'
}

RESULTS = {}

def get_request(url):
    
    response = requests.get(url)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)

    # Must have been a 200 status code
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def post_request(url, data):

    response = requests.post(url, data=data)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)

    # Must have been a 200 status code
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def retrieve_data(name, form_data, index):

    print("-------------")
    print("Searching for: ", name)

    # Get div w/ URL to person's page
    doc = post_request(URL + POST, form_data)
    try: 
        target_row = doc.find("div", {"class": "results"}).find("table").find("tbody").find_all("tr")[1]
        target_td = target_row.find_all('td')[1]
        js = target_td.find_all("script")

        decrypted = []

        for script in js:
            text = script.get_text()
            params = text[12:] # Remove function() name

            params = params.split(');', 1)[0] # Take only stuff before );

            params = params.split('",', 1) # Split by ", (for first param and second)

            res = str(decrypt(params[0], params[1]))
            res = res.replace('"', '') # Remove quotes
            res = res.replace('\'', '')

            decrypted.append(res)

        result = {}
        d = gender.Detector()
        firstName = name.split()[1]

        result['position'] = decrypted[0]
        result['department'] = decrypted[len(decrypted)-1]
        result['gender'] = d.get_gender(firstName)

        if ',' in result['department']:
            temp = result['department'].split(',')
            result['department'] = str(temp[1][1:] + " " + temp[0])

        RESULTS[name] = result

        print("Successfully added: ", name, " ", RESULTS[name])

    except Exception as e:
        print("No result for search: ", name)
        print("====> Error: ", e)


# SCRIPT

index = 0

for name in NAMES:

    # Check if have middle name
    # If longer than 2, only use first 2 
    strings = name.split()

    if len(strings) > 2:
        name = strings[0] + " " + strings[1]

    form_data['keywords'] = name
    retrieve_data(name, form_data, index)
    index += 1

print("\n")
print("===========================")
print(RESULTS)