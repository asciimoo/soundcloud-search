from json import loads
from requests import get

guest_client_id = 'b45b1aa10f1ac2941910a7f0d10f8e28'



def search(query):
    global guest_client_id

    search_url = 'https://api.soundcloud.com/search?q=%s&facet=model&limit=10&offset=0&linked_partitioning=1&client_id='+guest_client_id

    url = search_url % query

    while url:
        doc = loads(get(url).text)
        for entity in doc['collection']:
            if entity['kind'] == 'track':
                yield entity['permalink_url']

        url = doc.get('next_href')

def main():
    global search_url
    from sys import argv
    if len(argv) < 2:
        print '[!] missing search terms'
        from sys import exit
        exit(1)
    query = ' '.join(argv[1:])
    for song_url in search(query):
        print song_url

if __name__ == '__main__':
    main()
