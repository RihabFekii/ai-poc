from pydantic import BaseSettings


class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"
	PROJECT_NAME = "Animal Activity Prediction API"

settings = Settings()

class ProcessorConfig:
	# Real Time Weather
	URL_WEATHER_ORION = "weather.orion.docker:1026"
	TEMPERATURE_SENSOR_ID = "001"
	URL_AI_PROVIDER_ORION = "ai.orion.docker:1026"
	ANIMAL_ID = "0001"
	HEADER = {"Content-Type": "application/json"}

config = ProcessorConfig()

