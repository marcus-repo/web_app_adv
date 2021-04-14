import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.colors
from collections import OrderedDict
import requests


# default list of all countries of interest
country_default = OrderedDict([('Canada', 'CAN'), ('United States', 'USA'), 
  ('Brazil', 'BRA'), ('France', 'FRA'), ('India', 'IND'), ('Italy', 'ITA'), 
  ('Germany', 'DEU'), ('United Kingdom', 'GBR'), ('China', 'CHN'), ('Japan', 'JPN')])


def return_figures(countries=country_default):

	if not bool(countries):
		countries = country_default

	# prepare filter data for World Bank API
	# the API uses ISO-3 country codes separated by ;
	country_filter = list(countries.values())
	country_filter = [x.lower() for x in country_filter]
	country_filter = ';'.join(country_filter)

	# World Bank indicators
	# https://data.worldbank.org/indicator
	indicators = ['EN.ATM.CO2E.KT','EN.ATM.CO2E.PC','EG.USE.ELEC.KH.PC', 'EG.FEC.RNEW.ZS']


	data_frames = []
	urls = [] # url endpoints

	# pull data from World Bank API
	for indicator in indicators:
		url = 'http://api.worldbank.org/v2/countries/' + country_filter +\
		'/indicators/' + indicator +'?date=1990:2015&per_page=1000&format=json'
		urls.append(url)
		print(url)

		# example url 
		#http://api.worldbank.org/v2/countries/can;usa;bra;fra;ind;ita;deu;gbr;chn;jpn/indicators/AG.LND.FRST.ZS?date=1990:2015&per_page=1000&format=json

		try:
			r = requests.get(url)
			data = r.json()[1]
		except:
			print('could not load data ', indicator)

		for i, value in enumerate(data):
			value['indicator'] = value['indicator']['value']
			value['country'] = value['country']['value']

		data_frames.append(data)


	# CO2 emissions (kt)
	# first chart plots CO2 emissions metric tons per capita
	# as a line chart
	graph_one = []
	df = pd.DataFrame(data_frames[0])

	# filter and sort values for the visualization
	# filtering plots the countries in decreasing order by their values
	#df_one = df_one[(df_one['date'] == '2015') | (df_one['date'] == '1990')]
	#df_one.sort_values('value', ascending=False, inplace=True)
	df.sort_values(by=['country','date'], inplace=True)

	# this country list is re-used by all the charts to ensure legends have the same
	# order and color
	countrylist = df.country.unique().tolist()


	# chart 1
	for country in countrylist:
		x_val = df[df['country'] == country].date.tolist()
		y_val = df[df['country'] == country].value.tolist()
		graph_one.append(
			go.Scatter(
			x = x_val,
			y = y_val,
			mode = 'lines',
			name = country
			)
		)

	layout_one = dict(title = 'CO2 emissions (kt) <br> 1990 to 2015',
					xaxis = dict(title = 'Year',
						autotick=False, tick0=1990, dtick=5),
					yaxis = dict(title = 'kt'),
					)
	

	# second chart plots CO2 emissions metric tons per capita
	# as a line chart
	graph_two = []
	df = pd.DataFrame(data_frames[1])

	# filter and sort values for the visualization
	# filtering plots the countries in decreasing order by their values
	#df_one = df_one[(df_one['date'] == '2015') | (df_one['date'] == '1990')]
	#df_one.sort_values('value', ascending=False, inplace=True)
	df.sort_values(by=['country','date'], inplace=True)

	# chart 1
	for country in countrylist:
		x_val = df[df['country'] == country].date.tolist()
		y_val = df[df['country'] == country].value.tolist()
		graph_two.append(
			go.Scatter(
			x = x_val,
			y = y_val,
			mode = 'lines',
			name = country
			)
		)

	layout_two = dict(title = 'CO2 emissions <br> (metric tons per capita)* <br> 1990 to 2015',
					xaxis = dict(title = 'Year',
						autotick=False, tick0=1990, dtick=5),
					yaxis = dict(title = 'metric tons per capita'),
					)


	# third chart plots Electric power consumption (kWh per capita)
	# as a line chart
	graph_three = []
	df = pd.DataFrame(data_frames[2])

	# filter and sort values for the visualization
	# filtering plots the countries in decreasing order by their values
	#df_one = df_one[(df_one['date'] == '2015') | (df_one['date'] == '1990')]
	#df_one.sort_values('value', ascending=False, inplace=True)
	df.sort_values(by=['country','date'], inplace=True)

	# chart 1
	for country in countrylist:
		x_val = df[df['country'] == country].date.tolist()
		y_val = df[df['country'] == country].value.tolist()
		graph_three.append(
			go.Scatter(
			x = x_val,
			y = y_val,
			mode = 'lines',
			name = country
			)
		)

	layout_three = dict(title = 'Electric power consumption <br> (kWh per capita) <br> 1990 to 2015',
					xaxis = dict(title = 'Year',
						autotick=False, tick0=1990, dtick=5),
					yaxis = dict(title = 'kWh per capita'),
					)


	# fourth Renewable energy consumption (% of total final energy consumption)
	# as a line chart
	graph_four = []
	df = pd.DataFrame(data_frames[3])
	df.sort_values(by=['country','date'], inplace=True)
	

	# chart 4
	for country in countrylist:
		x_val = df[df['country'] == country].date.tolist()
		y_val = df[df['country'] == country].value.tolist()
		graph_four.append(
			go.Scatter(
			x = x_val,
			y = y_val,
			mode = 'lines',
			name = country
			)
		)

	layout_four = dict(title = 'Renewable energy consumption <br> (% of total final energy consumption)  <br> 1990 to 2015',
					xaxis = dict(title = 'Year',
						autotick=False, tick0=1990, dtick=5),
					yaxis = dict(title = '%'),
					)

	# append all charts
	figures = []

	figures.append(dict(data=graph_one, layout=layout_one))
	figures.append(dict(data=graph_two, layout=layout_two))
	figures.append(dict(data=graph_three, layout=layout_three))
	figures.append(dict(data=graph_four, layout=layout_four))

	return figures