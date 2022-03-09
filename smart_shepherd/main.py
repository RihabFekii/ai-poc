import requests

from preprocessor.config import config
from preprocessor.input_preprocessor import InputPreprocessor
from preprocessor.output_preprocessor import update_prediction
from ml_api.app.schemas.predict import PredictionResults


def predict(ip: InputPreprocessor) -> PredictionResults:

	temperature = ip.get_temperature()
	coordinates = ip.get_coordinates()
	input_data = ip.input_preprocessor(coordinates=coordinates,temperature=temperature)

	response = requests.request(
	"POST", url=config.PREDICT_URL, 
	headers=config.HEADER, 
	data=input_data.json()
	)

	prediction_result = PredictionResults(**response.json())

	return prediction_result



if __name__ == "__main__":

	ip = InputPreprocessor()
	prediction = predict(ip)
	print(prediction)
	update_prediction(predictions=prediction)


# todo

# write README about the Subscription on prediction update

