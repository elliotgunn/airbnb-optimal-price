from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

# initialize Flask app
app = Flask(__name__)

# load pickled model
model = pickle.load(open('finalized_model.sav','rb'))

# the route() binds a function to a URL
@app.route('/api', methods=['POST'])
def api():
    """
    Receives input data as JSON and returns optimal price of AirBnB unit.

    """

    # 1. access data
    # force = True: Ignore the mimetype and always try to parse JSON
    req_data = request.get_json(force=True)

    # TO DO: fill in inputs
    accomodates = req_data['accomodates']
    bedrooms = req_data['bedrooms']

    # 2. convert to numpy array for model
    user_input = np.array([[accomodates, bedrooms]])

    # 3. return prediction using model
    prediction = model.predict(user_input)
    # optimal_price = list(prediction[0])[0]

    # jsonify(results) returns list
    # op_price = list(optimal_price)
    return jsonify(results=op_price)

if __name__ == '__main__':
    # can also load pickled file here

    # e.g. modelfile = 'models/final_prediction.pickle'
    # model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, port=5000)
