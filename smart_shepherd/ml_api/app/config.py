import os

from pydantic import BaseSettings


class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"
	PROJECT_NAME = "Animal Activity Prediction API"


settings = Settings()

class ProcessorConfig:
	# Real Time Weather Orion URL
	WEATHER_SERVICE_ORION_HOST = os.environ["WEATHER_SERVICE_ORION_HOST"]
	# for simplification reasons, temperature sensor id is constant
	TEMPERATURE_SENSOR_ID = "001"
	# Smart Shepherd Orion URL
	AI_PROVIDER_ORION_HOST = os.environ["AI_PROVIDER_ORION_HOST"]
	HEADER = {"Content-Type": "application/json"}


config = ProcessorConfig()

