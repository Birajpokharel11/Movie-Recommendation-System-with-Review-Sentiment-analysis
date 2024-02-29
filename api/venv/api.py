from flask import Flask, jsonify
import pickle
import pandas as pd
import json
app = Flask(__name__)

def convert_to_json(data):
    """
    Convert DataFrame to JSON format where each entry contains a dictionary with 'movie_id' and 'title'.
    
    Parameters:
    - data (DataFrame): DataFrame containing 'movie_id' and 'title' columns.
    
    Returns:
    - json_data (str): JSON formatted string.
    """
    # Convert DataFrame to list of dictionaries
    movie_list = data.to_dict(orient='records')

    # Convert list of dictionaries to JSON
    json_data = json.dumps(movie_list)
    
    return json_data
# Load the pandas DataFrame from the pickle file
df = pd.read_pickle('movie_list.pkl')
Movie_id = pd.read_pickle('movie_id.pickle')

@app.route('/a')
def get_movie_titles():
    """Endpoint to retrieve the titles of all movies."""
    # Extract the titles from the DataFrame
    hello = convert_to_json(Movie_id)
    print(hello, 'sucka')

    titles = df['title'].tolist()
    return hello

if __name__ == '__main__':
    app.run(debug=True)
