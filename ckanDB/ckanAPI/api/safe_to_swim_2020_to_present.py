import json
import urllib.request
import pprint
""" - used Odata API link from data.ca.gov, modified link added '?$format=json' at end
    - changed key 'records' to 'value' for response_dict
"""

url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=1987c159-ce07-47c6-8d4f-4483db6e6460&limit=5'


fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())
# query_dict = response_dict['value']
pprint.pprint(response_dict)
