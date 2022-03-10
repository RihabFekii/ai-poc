
from ml_api.app.schemas.predict import PredictionResults


def prediction_parser_to_ngsild(data: PredictionResults):

	prediction = data.predictions[0]
	#prediction = {"animalActivity" : prediction}
	prediction = {
		"animalActivity": {
			"type": "Property",
			"value": prediction
		}
		}
		
	return prediction
