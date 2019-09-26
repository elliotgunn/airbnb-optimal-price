from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
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
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

# the route() binds a function to a URL
@app.route('/api', methods=['POST', 'GET'])
def api():
    """
    Receives input data as JSON and returns optimal price of AirBnB unit.

    """

    # 1. access data
    # force = True: Ignore the mimetype and always try to parse JSON
    req_data = request.get_json(force=True)

    # Assign incoming data to variables for use in model
    desc = req_data['description']

    # Run description through tokenize function
    description_length = len(tokenize(desc))


    # TO DO: fill in inputs
    neighbourhood_group_cleansed = req_data['neighbourhood_group_cleansed']
    property_type = req_data['property_type']
    accommodates = req_data['accommodates']
    bathrooms = req_data['bathrooms']
    bedrooms = req_data['bedrooms']
    security_deposit = req_data['security_deposit']
    cleaning_fee = req_data['cleaning_fee']
    guests_included = req_data['guests_included']
    extra_people = req_data['extra_people']
    minimum_nights = req_data['minimum_nights']
    instant_bookable = req_data['instant_bookable']
    cancellation_policy = req_data['cancellation_policy']
    tv_cable = req_data['tv_cable']
    pets_allowed = req_data['pets_allowed']

    # 2. convert to list for model
    features = [description, neighbourhood_group_cleansed, property_type, accommodates,
                bathrooms, bedrooms, security_deposit, cleaning_fee, guests_included,
                extra_people, minimum_nights, instant_bookable, cancellation_policy,
                tv_cable, pets_allowed]

    # run the features through the encoder
    features_transformed = encoder.transform(features)

    # predict optimal price using the prediction function
    price = model.predict(features_transformed)

    return jsonify({'prediction': price})

if __name__ == '__main__':
    # can also load pickled file here

    # e.g. modelfile = 'models/final_prediction.pickle'
    # model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, port=5000)
