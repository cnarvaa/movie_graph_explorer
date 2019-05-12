import requests


def get_movie_info(id):
    url = 'https://query.wikidata.org/sparql'
    query = f"""SELECT ?movie ?movieLabel ?main_subjectLabel ?genreLabel ?box WHERE {{
        ?movie wdt:P345 "{id}";
            wdt:P921 ?main_subject;
            wdt:P136 ?genre.
        ?movie p:P2142 ?statement.
        ?statement ps:P2142 ?box
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        }}"""
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    return data
