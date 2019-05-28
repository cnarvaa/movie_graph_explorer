# Flask MVC Template

Template for using MVC pattern with Flask and Peewee

## Requisites:
* Flask
* Peewee

# Usage:
* Clonate the repo
* Use the example model, controller and templates to create your own
* Register the models/controllers in the app.py file
* Run app.py
# Recommender system with semantic knowledge

## Requirements
neo4j
jmespath

##Steps:
1) Install neo4j desktop
2) download the database from http://example-data.neo4j.org/3.3-datasets/cineasts.tgz
3) Create a new graph from neo4j desktop (remember pass)
4) go to the new graph settings and open graph folder
5) extract the database and put as data/database/graph.db folder
6) set the allow upgrade flag in your neo4j.conf
7) Copy the Bolt port, you can find it in the graph configs.

##Some links
https://neo4j.com/developer/python/
https://github.com/neo4j/neo4j-python-driver
https://neo4j.com/docs/cypher-refcard/current/
