import requests

url = 'https://query.wikidata.org/sparql'


def get_data(query):
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    return data


def get_movie_info(id):
    query = f"""SELECT ?movie ?movieLabel ?main_subjectLabel ?genreLabel ?box WHERE {{
        ?movie wdt:P345 "{id}".
        OPTIONAL {{ ?movie wdt:P921 ?main_subject. }}
        OPTIONAL {{ ?movie wdt:P136 ?genre. }}
        OPTIONAL {{
            ?movie p:P2142 ?statement.
            ?statement ps:P2142 ?box
        }}
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        }}"""
    data = get_data(query)
    return data


def get_more_movies_by_production_company(id):
    query = f"""SELECT DISTINCT ?new_movies ?new_moviesLabel ?production_companyLabel WHERE {{
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
            ?movie wdt:P345 "{id}".
            OPTIONAL {{
                ?movie wdt:P272 ?production_company.
                ?new_movies wdt:P31 wd:Q11424;
                wdt:P272 ?production_company.
            }}
            }}
            ORDER BY (?production_companyLabel)
        """

    data = get_data(query)
    return data
