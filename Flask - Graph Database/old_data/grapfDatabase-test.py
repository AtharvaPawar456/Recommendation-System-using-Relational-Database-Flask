from rdflib import Graph, Namespace, RDF, Literal, URIRef

# Create a namespace
ns = Namespace("http://example.org/friends/")

# Create a new RDF graph
g = Graph()

# Load the JSON data into the RDF graph
data = [
        {"id": "1", "name": "Alice", "age": 25, "city": "New York", "friend_of": ["2", "3"]},
        {"id": "2", "name": "Bob", "age": 30, "city": "San Francisco", "friend_of": ["1", "3"]},
        {"id": "3", "name": "Charlie", "age": 28, "city": "Los Angeles", "friend_of": ["1", "2"]},
        {"id": "4", "name": "David", "age": 27, "city": "Chicago", "friend_of": ["5"]},
        {"id": "5", "name": "Eva", "age": 26, "city": "Boston", "friend_of": ["4"]},
        {"id": "6", "name": "Frank", "age": 32, "city": "Seattle", "friend_of": []},
        {"id": "7", "name": "Grace", "age": 29, "city": "Austin", "friend_of": []},
        {"id": "8", "name": "Helen", "age": 31, "city": "Denver", "friend_of": ["9"]},
        {"id": "9", "name": "Ivan", "age": 33, "city": "Portland", "friend_of": ["8"]},
        {"id": "10", "name": "Jack", "age": 24, "city": "Miami", "friend_of": []}
        ]

show_relation_between = ['Alice', 'Charlie', 'Ivan', 'Frank']

for friend in data:
    friend_uri = ns[friend["id"]]
    g.add((friend_uri, RDF.type, ns.Person))
    g.add((friend_uri, ns.name, Literal(friend["name"])))
    g.add((friend_uri, ns.age, Literal(friend["age"])))
    g.add((friend_uri, ns.city, Literal(friend["city"])))

    for friend_of_id in friend["friend_of"]:
        friend_of_uri = ns[friend_of_id]
        g.add((friend_uri, ns.friendOf, friend_of_uri))

# Save the RDF graph to a file
g.serialize(destination='friends.rdf', format='xml')




'''
create a flask project of recommendation system 
product item list = ['dj system', 'iphone 12', 'acer 5i gen11 laptop', 'i ball mouse', 'cs e-book', 'chat-gpt subscription']

data = [
        {
                "id": "1",
                "name": "Alice",
                "age": 25,
                "city": "New York",
                "friend_of": ["2", "3"],
                "purchases_list": [
                {"item": "dj system", "qty": 1},
                {"item": "iphone 12", "qty": 2}
                ]
        },...
        ]
        sample database... of users
        this database stored as clientsdb.rdf in xml format

based on user login recommend the product

give flask code and html code 
use tailwind css CDN for styling html page 

flow 
- route : index
get username 
if user name in db , list the relation of user with its friends , list the friends last purschase, then recommend the most related item to the username


'''















# # pip install rdflib

# from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef

# # Create a namespace
# n = Namespace("http://example.org/people/")

# # Create a new graph
# g = Graph()

# # Add some triples to the graph
# g.add((n.John, RDF.type, n.Person))
# g.add((n.John, n.age, Literal(30)))
# g.add((n.John, n.name, Literal("John Doe")))

# # Query the graph
# for s, p, o in g:
#    print(s, p, o)
