from flask import Blueprint, render_template
import jmespath
from models.sparkl_query import get_movie_info
from models.neo4j_query import KnowledgeRecommendation

neo4j_graph = KnowledgeRecommendation("bolt://localhost:11004", "neo4j", "123456")

# Instance your controller with Blueprint
graph_controller = Blueprint('graph_controller', __name__,
                             template_folder='templates')


@graph_controller.route('/movie/<title>/', defaults={'augmented': "True"})
@graph_controller.route('/movie/<title>/<augmented>')
def main_info(title, augmented):
    data = neo4j_graph.movie("Jurassic Park")[0]
    augmented_data = None
    imdb_id = data["imdbId"]
    if augmented == "True":
        try:
            augmented_data = get_movie_info(imdb_id)
        except Exception as e:
            print("something happened trying to get info from SPARKL", e)
        else:
            augmented_data = augmented_data["results"]["bindings"]
            genres = jmespath.search("join(',',[*].genreLabel.value)", augmented_data)
            augmented_data = augmented_data[0]
            augmented_data.update({"genreLabel": {"value": genres}})
    return render_template('movie.html', movie_data=data, augmented_data=augmented_data)
