# Film Comments Scrappers

- works for čsfd and letterbox

# How to use

## ČSFD

```
python csfd.py <file_name> <last_page_number> <film_url>

# example:
python csfd.py comments.txt 65 https://www.csfd.cz/film/6170-star-wars-epizoda-i-skryta-hrozba/
```

- last_page_number = number of the last page of comments for that film so that the scripts knows when to stop

- film_url on čsfd, eg. https://www.csfd.cz/film/6170-star-wars-epizoda-i-skryta-hrozba/

## Letterbox

```
python letterbox.py <file_name> <_lastpage_number> <film_url>

# example:
python letterbox.py comments.txt 250 
```

- url example: https://letterboxd.com/film/star-wars-episode-i-the-phantom-menace/reviews/by/activity/
  - url does not have to be "/by/activity" but that page has to display the reviews and reviews only
  - url can be ordered differently and it should still work
