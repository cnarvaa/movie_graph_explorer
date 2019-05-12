from neo4j import GraphDatabase
from json import dumps
import time
from pandas import DataFrame


class KnowledgeRecommendation(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self.session = self._driver.session()

    def close(self):
        self._driver.close()

#     @staticmethod
#     def _epoch_to_date(epoch):
#         try:
#             s, ms = divmod(int(epoch), 1000)  # (1236472051, 807)
#         except Exception as e:
#             raise e

#         return '{}.{:03d}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s)), ms)

    def serialize_movie(self, movie):
        return {
            'id': movie['id'],
            'title': movie['title'],
            'summary': movie['description'],
            'released': movie.get('releaseDate'),
            'duration': movie['runtime'],
            'rated': movie['rated'],
            'imdbId': movie['imdbId'],
            'genre': movie['genre']
        }

    def movie(self, title):
        query = ('MATCH (movie:Movie) ' +
                 f'WHERE movie.title =~ "{title}" ' +
                 'RETURN movie')
        results = self.session.run(query)
        return [self.serialize_movie(record['movie']) for record in results.data()]

    def same_genre_movies(self, title):
        query = ('MATCH (movie:Movie) ' +
                 f'WHERE movie.title = "{title}" ' +
                 'WITH movie.genre as genre ' +
                 'MATCH (movies:Movie) ' +
                 'WHERE movies.genre = genre ' +
                 'RETURN movies.title, movies.releaseDate, movies.genre, movies.imdbId ' +
                 'LIMIT 100')
        results = self.session.run(query)
#         return [self.serialize_movie(record['movies']) for record in results.data()] # you should only return movies
        return results.data()

    def movies_by_movie_director(self, title):
        query = ('MATCH (movie:Movie)<-[:DIRECTED]-(director:Director) ' +
                 f'WHERE movie.title = "{title}" ' +
                 'MATCH (movies:Movie)<-[:DIRECTED]-(director) ' +
                 'RETURN movies.title, movies.releaseDate, movies.genre, movies.imdbId ' +
                 'LIMIT 100')
        results = self.session.run(query)
        return results.data()

    def movies_by_actor(self, actor):
        query = ('MATCH (movies:Movie)<-[:ACTS_IN]-(actor:Actor) ' +
                 f'WHERE actor.name = "{actor}" ' +
                 'RETURN movies.title, movies.releaseDate, movies.genre, movies.imdbId ')
        results = self.session.run(query)
        return results.data()

    def movies_by_actor_and_genre(self, actor, genre):
        query = ('MATCH (movies:Movie)<-[:ACTS_IN]-(actor:Actor) ' +
                 f'WHERE actor.name = "{actor}" and movies.genre="{genre}" ' +
                 'RETURN movies.title, movies.releaseDate, movies.genre, movies.imdbId ')
        results = self.session.run(query)
        return results.data()

    def movies_shared_actors_with_genre(self, actor, genre):
        query = ('MATCH (actor:Actor)-[:ACTS_IN]->(movie:Movie)<-[:ACTS_IN]-(actors:Actor) ' +
                 f'WHERE actor.name = "{actor}" ' +
                 'WITH actors ' +
                 'MATCH (actors)-[:ACTS_IN]->(movies:Movie) ' +
                 f'WHERE movies.genre="{genre}" ' +
                 'RETURN movies.title, movies.releaseDate, movies.genre, movies.imdbId ' +
                 'LIMIT 100 ')
        print(query)
        results = self.session.run(query)
        return results.data()


graph = KnowledgeRecommendation("bolt://localhost:11004", "neo4j", "123456")
