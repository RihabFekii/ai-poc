from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"

	# CORS or "Cross-Origin Resource Sharing" 
	# See: https://fastapi.tiangolo.com/tutorial/cors/
	BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
		"http://localhost:2027",
		"http://localhost:2028",
		"http://localhost:8001",
	]

	PROJECT_NAME = "Animal Activity Prediction API"



settings = Settings()

