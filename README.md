# Link to Webapp [https://climate-webapp.herokuapp.com](https://climate-webapp.herokuapp.com)

# World Bank API Data Dashboard - Climate Change

This is a flask app that visualizes data from the world bank API. Data is
pulled directly from the API and then visualized using Plotly.

The purpose of this project is to learn more about plotly and the 
deployment about web applications on heroku while giving some 
interesting insights about CO2 Emissions and Energy Consumption of the
Top 10 World Economies.

## About the data

The indicators displayed on the visualizations are the following:

- CO2 emissions (kt) *EN.ATM.CO2E.KT*
- CO2 emissions (metric tons per capita) *EN.ATM.CO2E.PC*
- Electric power consumption (kWh per capita) *EG.USE.ELEC.KH.PC*
- Renewable energy consumption (% of total final energy consumption) *EG.FEC.RNEW.ZS*

Link to World Bank Indicators Section Climate Change [https://data.worldbank.org/indicator](https://data.worldbank.org/indicator)

## Heroku deployment guide

To install the flask app, you need:
- python3
- python packages in the requirements.txt file
 
 Install the packages with
``` 
 pip install -r requirements.txt
```

## Ressources

On a MacOS/linux system, installation is easy. Open a terminal, and go into 
the directory with the flask app files. Run `python worldbank.py` in the terminal.