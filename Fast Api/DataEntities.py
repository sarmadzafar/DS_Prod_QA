from pydantic import BaseModel
import requests

class ModelArguments(BaseModel):
    context: str
    question:str



 
# wikipediaDataExtractor = WikipediaDataExtractor()
# wikipediaDataExtractor.ExtractText("Unix")


