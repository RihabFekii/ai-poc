from sklearn.preprocessing import LabelEncoder
import numpy as np 


def label_encode_target(target: str) -> np.ndarray:
	""" Encode the traget column """

	label_encoder = LabelEncoder()
	label_encoder = label_encoder.fit(target)
	encoded_target = label_encoder.transform(target)
	return encoded_target

