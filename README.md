# Recommendation System using Relational Graph Database and Flask

This project implements a recommendation system using a relational graph database and Flask. The data is stored in a graph database, and recommendations are provided based on user interactions.

## Project Structure

- `Flask - Graph Database/research/graph_images/alice_graph.png`: Relational Graph Database image.
- `Output Images/img-output-1.png`: Output Image 1.
- `Output Images/img-output-2.png`: Output Image 2.
- `Flask - Graph Database/clients_data.json`: Original raw data in JSON format.
- `Flask - Graph Database/store_db.py`: Script to convert JSON data to relational data and store it.
- `Flask - Graph Database/clientsdb.rdf`: Relational data stored in RDF format.
- `Flask - Graph Database/app.py`: Flask web application.
- `Flask - Graph Database/templates/index.html`: HTML template for the home page.
- `Flask - Graph Database/templates/recommendation.html`: HTML template for the recommendation page.

## How to Run

1. **Store Data**: Run `store_db.py` to convert JSON data to relational data and store it in `clientsdb.rdf`.

    ```bash
    python store_db.py
    ```

2. **Run Flask App**: Execute `app.py` to start the Flask web application.

    ```bash
    python app.py
    ```

3. **Access the App**: Open your web browser and navigate to `http://127.0.0.1:5000/`.

4. **Test the Recommendation System**: Login with any of the following usernames: [Alice, Bob, Charlie, David, Eva, Frank, Grace, Helen, Ivan, Jack]. Press the "Get Recommendation" button to see user data, friend data, and recommendations.

## Dependencies

- **Matplotlib and Networkx**: Visualization libraries for creating graph images.
  
    ```bash
    pip install matplotlib networkx
    ```

- **Flask**: Web framework for building the recommendation system.

    ```bash
    pip install Flask
    ```

- **Rdflib**: RDF library for working with RDF data.

    ```bash
    pip install rdflib
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
