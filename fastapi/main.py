from fastapi import FastAPI
from dataentities.dataEntities import ModelArguments
from inferencemodel.inferenceModel import InferenceModel
from textextractor.textextractor import WikipediaDataExtractor

app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/getanswers")
def getinference(modelArguments: ModelArguments):
    wikipediaDataExtractor = WikipediaDataExtractor()
    text = wikipediaDataExtractor.ExtractText("Unix")
    inferenceModel = InferenceModel()
    data = inferenceModel.query(
        {
            "inputs": {
                "question": modelArguments.question,
                "context": text,
            }
        }
    )
    return data





