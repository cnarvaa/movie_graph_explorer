from flask import Blueprint, render_template
import jmespath
from models.sparql_query import get_movie_info
from models.sparql_query import get_more_movies_by_production_company
from models.neo4j_query import KnowledgeRecommendation
from utils.dict import group_by_key

import json

neo4j_graph = KnowledgeRecommendation("bolt://localhost:11004", "neo4j", "123456")

# Instance your controller with Blueprint
graph_controller = Blueprint('graph_controller', __name__,
                             template_folder='templates')


@graph_controller.route('/movie/<title>/', defaults={'augmented': "True"})
@graph_controller.route('/movie/<title>/<augmented>')
def main_info(title, augmented):
    try:
        data = neo4j_graph.movie(title)[0]
    except IndexError:
        return render_template('responses/not_found.html', title=title)
    else:
        augmented_data = None
        related_movies = None
        imdb_id = data["imdbId"]
        if augmented == "True":
            try:
                augmented_data = get_movie_info(imdb_id)
                related_movies = get_more_movies_by_production_company(imdb_id)
            except Exception as e:
                print("something happened trying to get info from SPARQL", e)
            else:
                augmented_data = augmented_data["results"]["bindings"]
                genres = jmespath.search("join(',',[*].genreLabel.value)", augmented_data)
                if augmented_data:
                    augmented_data = augmented_data[0]
                    augmented_data.update({"genreLabel": {"value": genres}})
                if related_movies:
                    related_movies = jmespath.search(
                        "results.bindings[*].{internal_source: null, external_source:new_movies.value, name:new_moviesLabel.value, production_company:production_companyLabel.value}", related_movies)
                    for movie in related_movies:
                        movie["internal_source"] = f"http://127.0.0.1:5000/movie/{movie.get('name')}"

                    related_movies = group_by_key(related_movies, "production_company")
        print(json.dumps(related_movies))
        return render_template('movie.html', movie_data=data, augmented_data=augmented_data,
                               related_movies=related_movies)
