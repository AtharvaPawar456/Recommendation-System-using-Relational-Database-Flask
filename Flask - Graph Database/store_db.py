import json
from rdflib import Graph, Namespace, RDF, RDFS, Literal, URIRef

# Load JSON data from file
with open('clients_data.json', 'r') as json_file:
    data = json.load(json_file)

# Define namespaces
ns = Namespace("http://recomend.org/people/")
product_ns = Namespace("http://recomend.org/products/")

# Create a new RDF graph
clients_db = Graph()

# Add triples for users
for user in data:
    user_uri = ns[user["id"]]
    clients_db.add((user_uri, RDF.type, ns.Person))
    clients_db.add((user_uri, ns.name, Literal(user["name"])))
    clients_db.add((user_uri, ns.age, Literal(user["age"])))
    clients_db.add((user_uri, ns.city, Literal(user["city"])))

    # Add triples for friendships
    for friend_id in user.get("friend_of", []):
        friend_uri = ns[friend_id]
        clients_db.add((user_uri, ns.friendOf, friend_uri))

    # Add triples for purchases
    for purchase in user.get("purchases_list", []):
        product_uri = product_ns[purchase["item"].replace(" ", "_").lower()]
        clients_db.add((user_uri, product_ns.purchased, product_uri))
        clients_db.add((product_uri, RDF.type, product_ns.Product))
        clients_db.add((product_uri, RDFS.label, Literal(purchase["item"])))
        clients_db.add((product_uri, product_ns.quantity, Literal(purchase["qty"])))

# Save the RDF graph to a file
clients_db.serialize(destination='clientsdb.rdf', format='xml')
