# AirBnB Optimal Price
A Flask web app that uses historical booking data to predict the optimal price for an AirBnB in Berlin.

This is the data engineering part of the data science MVP. It consists of creating a Flask app, deployed on Heroku, to function as an API. The API connects to the backend (to...?)

The data science part consists of data cleaning, wrangling, and trained on a model. The model was pickled for deployment.

The app works by processing incoming data in Flask using the `request` object:

```{"feature":[{"id":3,"neighbourhood_group_cleansed":"maybe","description":"its is a description","property_type":"huge","accommodates":2,"bathrooms":1,"security_deposit":200,"cleaning_fee":3,"guests_included":0,"extra_people":0,"minimum_nights":1,"instant_bookable":false,"cancellation_policy":"big money","tv_cable":false,"pets_allowed":false,"bedrooms":1},{"id":2,"neighbourhood_group_cleansed":"maybe","description":"its is a description","property_type":"huge","accommodates":0,"bathrooms":1,"security_deposit":200,"cleaning_fee":3,"guests_included":0,"extra_people":0,"minimum_nights":1,"instant_bookable":false,"cancellation_policy":"big money","tv_cable":true,"pets_allowed":false,"bedrooms":7}]}```

receives JSON data, converts it to a numpy array, generates a prediction, and then (sends to FE?) as JSON data again.

Create an endpoint for the user. The Flask routes serve as the API endpoints.

The app receives the JSON data in this format:

'''
accommodates:
bedrooms:

'''



Helpful resources:

[How to Process Incoming Request Data in Flask](https://www.youtube.com/watch?v=hAEJajltHxc&amp=&index=129)

To test and verify, run 'FLASK_APP=flask-api.py flask shell`

