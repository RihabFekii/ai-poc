import requests

def test_get_coordinates():
	url = "http://localhost:1028/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:0001"

	headers= {"Content-Type": "application/json"}

	response = requests.request("GET", url, headers=headers)

	assert response.status_code == 200

