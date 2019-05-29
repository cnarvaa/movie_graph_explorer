# Movie GraphExplorer
The purpose of this project is to explore semantic technologies such as Neo4j's cypher and Sparql.

# Knowledge Graphs Introduction.

The [slides from NEO4j](https://www.slideshare.net/neo4j/knowledge-graphs-the-power-of-graphbased-search?from_action=save) are a good point to start.
I strongly recommend you to explore these slides:
* 3-7
* 23-25
* 32-34

This [slides from Microsoft](https://kdd2018tutorialt39.azurewebsites.net/KDD%20Tutorial%20T39.pdf) are more academic but they pinpoint the actual research topics on the field.

You can find the slides in the slides folder.

## Requirements
* neo4j
* jmespath
* Flask

# Recommender system with semantic knowledge

## Steps:
1) Install neo4j desktop
2) download the database from http://example-data.neo4j.org/3.3-datasets/cineasts.tgz
3) Create a new graph from neo4j desktop (remember pass)
4) go to the new graph settings and open graph folder
5) extract the database and put as data/database/graph.db folder
6) set the allow upgrade flag in your neo4j.conf
7) Copy the Bolt port, you can find it in the graph configs.

## Some links
https://neo4j.com/developer/python/
https://github.com/neo4j/neo4j-python-driver
https://neo4j.com/docs/cypher-refcard/current/
