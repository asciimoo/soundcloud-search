soundcloud-search
=================

soundcloud search script


### Command line usage

```bash
$ python soundcloud_search.py <search terms>
```

### python usage

```python
>>> import soundcloud_search
>>> track_urls = soundcloud_search.search('chiptune')
>>> for track_url in track_urls:
...     print track_url

```


### License

```
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
```
