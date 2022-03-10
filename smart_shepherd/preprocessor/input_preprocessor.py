from typing import List

import requests
from classification_model.processing.validation import MultipleAnimalDataInputs

from config import config
from utils.input_parser import parse_coordinates, parse_temperature


# This class could be easily edited if
# you have a set of data with a specific structure 
# and you want to perform specific methods on it
class InputPreprocessor:

	def get_coordinates(self) -> dict:
		# get request of animal coordinates 

		orion = config.URL_FARM_ORION
		animal_id = config.ANIMAL_ID
		
		url = f"http://{orion}/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:{animal_id}"

		try:
			response = requests.request("GET", url, headers=config.HEADER)
		except requests.HTTPError as e:
			if e.response.status_code == 404:
				return e

		coordinates = parse_coordinates(response.json())
		
		return coordinates

	def get_temperature(self) -> dict:
		# get request of temperature data

		orion = config.URL_WEATHER_ORION
		sensor_id = config.TEMPERATURE_SENSOR_ID
		url = f"http://{orion}/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:{sensor_id}"

		headers= {"Content-Type": "application/json"}

		try:
			response = requests.request("GET", url, headers=headers)
		except requests.HTTPError as e:
			if e.response.status_code == 404:
				return e
		
		temperature = parse_temperature(response.json())

		return temperature


	def input_preprocessor(
			self, coordinates:List[float], temperature: float
		) -> MultipleAnimalDataInputs:
		""" 
		Appends the temperature to the coordinates list
		and makes list compatiable with the pydantic 
		trained model input format
		""" 
		coordinates.append(temperature)

		data = coordinates

		input_model = {
				"inputs" : [
					{
						"pos_x": data[0],
						"pos_y": data[1],
						"pos_z": data[2],
						"temp": data[3]
					}   
				]
			}

		input = MultipleAnimalDataInputs(**input_model)

		return input










