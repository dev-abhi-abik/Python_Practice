import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com','https://api.github.com/invalid']:
    try:
        r = requests.get(url)
        r.raise_for_status() # Invoke to HTTP error will be raised for certain status codes
        # print('Printing contents')
        # print(r.content) #.content gives raw byte of response payload

        # print('Printing JSON')
        # print(r.json())

        print('Printing HEaders')
        print(r.headers)
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured:{err}')
    else:
        print('success')