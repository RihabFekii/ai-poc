import json

import requests
from ml_api.app.schemas.predict import PredictionResults

from config import config
from utils.output_parser import prediction_parser_to_ngsild


def update_prediction(predictions: PredictionResults):

	orion = config.URL_AI_PROVIDER_ORION
	animal_id = config.ANIMAL_ID

	url = f"http://{orion}/ngsi-ld/v1/entities/urn:ngsi-ld:Animal:{animal_id}/attrs"

	header = config.HEADER

	prediction = prediction_parser_to_ngsild(predictions)

	response = requests.request("POST", url=url, headers=header, data=json.dumps(prediction))

	return response.text

