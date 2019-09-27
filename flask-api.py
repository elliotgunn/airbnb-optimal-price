from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
import requests
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

# initialize Flask app
app = Flask(__name__)

# load pickled model and encoder
model = pickle.load(open('finalized_model.pkl','rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

# Function used for processing description
STOPWORDS = set(STOPWORDS).union(set(['and']))


def tokenize(text):
    return [
        token for token in simple_preprocess(text) if token not in STOPWORDS
        ]

# Connect to backend
@app.route('/', methods=['POST', 'GET'])
def responses():
    response = requests.get(
        'https://bnb-web-backend.herokuapp.com/api/features')
    return str(response.text)

# the route() binds a function to a URL
@app.route('/api', methods=['POST', 'GET'])
def predict():
    """
    Receives input data as JSON and returns optimal price of AirBnB unit.
    """
    # retrieve json user input data
    data = request.get_json(force=True)

    # assign incoming data to variables for use in model
    desc = data['feature'][0]['description']

    # run description through tokenize function
    description_length = len(tokenize(desc))

    # continue to assign incoming data to variables for use in model
    neighbourhood_group_cleansed = (
        data['feature'][0]['neighbourhood_group_cleansed'])
    property_type = data['feature'][0]['property_type']
    accommodates = data['feature'][0]['accommodates']
    bathrooms = data['feature'][0]['bathrooms']
    bedrooms = data['feature'][0]['bedrooms']
    security_deposit = data['feature'][0]['security_deposit']
    cleaning_fee = data['feature'][0]['cleaning_fee']
    guests_included = data['feature'][0]['guests_included']
    extra_people = data['feature'][0]['extra_people']
    minimum_nights = data['feature'][0]['minimum_nights']
    instant_bookable = data['feature'][0]['instant_bookable']
    cancellation_policy = data['feature'][0]['cancellation_policy']
    tv_cable = data['feature'][0]['tv_cable']
    pets_allowed = data['feature'][0]['pets_allowed']

    # create dict for model
    feature_dict = {
        'neighbourhood_group_cleansed': neighbourhood_group_cleansed,
        'property_type': property_type,
        'accommodates': accommodates,
        'bathrooms': bathrooms,
        'bedrooms': bedrooms,
        'security_deposit': security_deposit,
        'cleaning_fee': cleaning_fee,
        'guests_included': guests_included,
        'extra_people': extra_people,
        'minimum_nights': minimum_nights,
        'instant_bookable': instant_bookable,
        'cancellation_policy': cancellation_policy,
        'description_length': description_length,
        'tv': tv_cable,
        'pets': pets_allowed
        }

    # create dataframe
    features = pd.DataFrame(feature_dict, index=[1])

    # run the features through the encoder
    features_transformed = encoder.transform(features)

    # predict optimal price using the prediction function
    price = model.predict(features_transformed)

    # return prediction in json format
    return jsonify({'prediction': price})

if __name__ == '__main__':

    app.run(debug = True)
