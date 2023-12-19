from flask import Flask, render_template, request
from rdflib import Graph, Namespace, RDF, Literal, URIRef, RDFS
from datetime import datetime

app = Flask(__name__)

# Load RDF graph from clientsdb.rdf
clients_db = Graph()
clients_db.parse('clientsdb.rdf', format='xml')

# Define namespaces
ns = Namespace("http://recomend.org/people/")
product_ns = Namespace("http://recomend.org/products/")


def get_user_data(username):
    user_data = {}
    for s, p, o in clients_db.triples((None, ns.name, Literal(username))):
        user_data["id"] = str(s).split("/")[-1]
        user_data["name"] = str(o)

        # Extract user's age and city
        for _, age_p, age_o in clients_db.triples((s, ns.age, None)):
            user_data["age"] = age_o
        for _, city_p, city_o in clients_db.triples((s, ns.city, None)):
            user_data["city"] = city_o

        # Extract user's friends
        user_data["friend_of"] = []
        for _, friend_p, friend_o in clients_db.triples((s, ns.friendOf, None)):
            friend_name = clients_db.value(friend_o, ns.name, default=None)

            # Extract friend's purchases
            friend_purchases = set(
                str(item_o).replace(str(product_ns), "")
                for _, _, item_o in clients_db.triples((friend_o, product_ns.purchased, None))
            )

            user_data["friend_of"].append({
                "friend_name": str(friend_name),
                "friend_id": str(friend_o).split("/")[-1],
                "purchase_list": list(friend_purchases)
            })

        # Extract user's purchases
        user_data["purchases_list"] = []
        for _, purchased_p, purchased_o in clients_db.triples((s, product_ns.purchased, None)):
            item_name = clients_db.value(purchased_o, RDFS.label)
            item_quantity = clients_db.value(purchased_o, product_ns.quantity)
            user_data["purchases_list"].append({"item": str(item_name), "qty": item_quantity})

    return user_data



def get_recommendation(username, user_data):
    recommended_item = []

    for index in range(len(user_data["friend_of"])):
        fri_pur_list = user_data["friend_of"][index]["purchase_list"]
        print("user_friend_item_list : ", fri_pur_list)
        recommended_item.extend(fri_pur_list[::-1])

    # Get unique items
    unique_recommended_item = list(set(recommended_item))

    item_list = [
        {"item": "dj_system", "id": 1},
        {"item": "iphone_12", "id": 2},
        {"item": "i_ball_mouse", "id": 3},
        {"item": "cs_e-book", "id": 4},
        {"item": "acer_5i_gen11_laptop", "id": 5},
        {"item": "chat-gpt_subscription", "id": 6}
    ]

    json_list = [
        {"item": item, "id": next((item_data["id"] for item_data in item_list if item_data["item"] == item), None)}
        for item in unique_recommended_item
    ]
    # print("JSON List:", json_list)
    return json_list



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommendation', methods=['POST'])
def recommendation():
    username = request.form['username']
    user_data = get_user_data(username)
    recommendation = get_recommendation(username, user_data)
    return render_template('recommendation.html', username=username, user_data=user_data, recommendation=recommendation)


if __name__ == '__main__':
    app.run(debug=True)
