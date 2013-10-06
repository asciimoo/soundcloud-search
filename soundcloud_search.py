#!/usr/bin/env python

'''
soundcloud_search is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

soundcloud_search is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with soundcloud_search. If not, see < http://www.gnu.org/licenses/ >.

(C) 2013- by Adam Tauber, <asciimoo@gmail.com>
'''

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
