from typing import List

def parse_coordinates(payload: dict) -> List[float]:
	""" 
	Parses the payload of the get_coordinates request 
	and returns a list of animal coordinates
	"""

	location = payload["location"]["value"]
	coordinates = location["coordinates"]

	return coordinates

def parse_temperature(payload: dict) -> float:
	""" 
	Parses the payload of the get_temperature request 
	and returns the temperature value
	"""

	temperature = payload["temperature"]["value"]

	return temperature


def parse_notification(payload: dict):
	
	list = payload["data"]

	location = list[0]["location"]

	coordinates = location["coordinates"]

	# list of aninal dict keys 
	keys = ["pos_x","pos_y","pos_z"]

	# creating a dict from 2 lists of keys and values 
	coord_dict = dict(zip(keys,coordinates))

	return coord_dict