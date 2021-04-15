# Link to Webapp [https://climate-webapp.herokuapp.com](https://climate-webapp.herokuapp.com)

# World Bank API Data Dashboard - Climate Change

This is a flask app that visualizes data from the world bank API. Data is
pulled directly from the API and then visualized using Plotly.

The purpose of this project is to learn more about plotly and the 
deployment about web applications on heroku while giving some 
interesting insights about CO2 Emissions and Energy Consumption of the
Top 10 World Economies in 2015.

## About the data

The indicators displayed on the visualizations are the following:

- CO2 emissions (kt) *EN.ATM.CO2E.KT*
- CO2 emissions (metric tons per capita) *EN.ATM.CO2E.PC*
- Electric power consumption (kWh per capita) *EG.USE.ELEC.KH.PC*
- Renewable energy consumption (% of total final energy consumption) *EG.FEC.RNEW.ZS*

Link to World Bank Indicators Section Climate Change [https://data.worldbank.org/indicator](https://data.worldbank.org/indicator)

## Heroku deployment guide

Pre-Requesites: 
- Heroku Account
- Python Installation
- Git Installation

Process Steps:
- create virtual environment: python -m venv \<name>
- activate environment: .\\\<name>\Scripts\activate
- pip install flask pandas plotly gunicorn
- uncomment in myapp.py #app.run(host='127.0.0.1', port=5000, debug=True)
- touch Procfile, insert web gunicorn \<webapp-folder>:app
- pip freeze > requirements.txt
- git init
- git add .
- git commit -m "xyz"
- heroku create \<web-app-name>
- git remote -v
- git push heroku master

## Ressources
- https://www.udacity.com/
- https://devcenter.heroku.com/articles/heroku-cli
- https://plotly.com/nodejs/setting-graph-size/