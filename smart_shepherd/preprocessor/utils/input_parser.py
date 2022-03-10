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