import json
import requests

class InferenceModel:

    def __init__(self) -> None:
        self.headers = {"Authorization": f"Bearer {apikey}"}
        self.API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"



    def query(self, payload):
        data = json.dumps(payload)
        response = requests.request("POST", self.API_URL, headers=self.headers, data=data)
        return json.loads(response.content.decode("utf-8"))

