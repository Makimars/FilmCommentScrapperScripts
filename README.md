# Film Comments Scrappers

- works mainly for čsfd and letterbox

# How to use

## ČSFD

```
python csfd.py <file_name> <last_page_number> <film_url>
```

- last_page_number = number of the last pageof comments so the scripts knows to stop
- film_url on čsfd, eg. https://www.csfd.cz/film/6170-star-wars-epizoda-i-skryta-hrozba/

## Letterbox

```
python letterbox.py <file_name> <_lastpage_number> <film_url>
```

- url example: https://letterboxd.com/film/star-wars-episode-i-the-phantom-menace/reviews/by/activity/
  - url does not have to be "by/activity" but that page has to display the reviews and reviews only
