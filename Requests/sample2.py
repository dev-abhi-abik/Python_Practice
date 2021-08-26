import requests
from requests.exceptions import HTTPError

BASE_URL = 'https://dev-api.partrunner.com/'

def checkBaseURL():
    try:
        r = requests.get(BASE_URL)
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured:{err}')
    else:
        print('Success')
        print(r.json())

checkBaseURL()