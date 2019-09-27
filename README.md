# AirBnB Optimal Price
This is the API for a Flask web app that uses historical booking data to predict the optimal price for an AirBnB in Berlin. It is deployed to Heroku at [https://airbnb-optimal-price.herokuapp.com/](https://airbnb-optimal-price.herokuapp.com/).

The data science part consists of data cleaning, wrangling, and trained on a model. The model was pickled and passed to the data engineering team. 


We ([@justin-hsieh](https://github.com/justin-hsieh) and [@elliotgunn](https://github.com/elliotgunn)) created a Flask app, deployed on Heroku, to function as an API. The API connects to the backend where the web dev team took over for full-stack deployment.

The app works by processing incoming JSON data using the `request` object:

```{"feature":[{"id":3,"neighbourhood_group_cleansed":"maybe","description":"its is a description","property_type":"huge","accommodates":2,"bathrooms":1,"security_deposit":200,"cleaning_fee":3,"guests_included":0,"extra_people":0,"minimum_nights":1,"instant_bookable":false,"cancellation_policy":"big money","tv_cable":false,"pets_allowed":false,"bedrooms":1},{"id":2,"neighbourhood_group_cleansed":"maybe","description":"its is a description","property_type":"huge","accommodates":0,"bathrooms":1,"security_deposit":200,"cleaning_fee":3,"guests_included":0,"extra_people":0,"minimum_nights":1,"instant_bookable":false,"cancellation_policy":"big money","tv_cable":true,"pets_allowed":false,"bedrooms":7}]}```

It then converts it to a dictonary and dataframe, generates a prediction, and then returns it as JSON data. The Flask routes serve as the API endpoints.

Helpful resources:

[How to Process Incoming Request Data in Flask](https://www.youtube.com/watch?v=hAEJajltHxc&amp=&index=129)

