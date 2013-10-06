from sys import argv
from json import loads
from requests import get

guest_client_id = 'b45b1aa10f1ac2941910a7f0d10f8e28'

search_url = 'https://api.soundcloud.com/search?q=%s&facet=model&limit=10&offset=0&linked_partitioning=1&client_id='+guest_client_id

query = argv[1]

url = search_url % query

while url:
    doc = loads(get(url).text)
    for entity in doc['collection']:
        if entity['kind'] == 'track':
            print entity['permalink_url']

    url = doc.get('next_href')
