
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import numpy as np

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

model = mlflow.pyfunc.load_model("model")


class InputData(BaseModel):
    inputs: list[list[float]]


@app.post("/predict")
def predict(data: InputData):
    predictions = model.predict(np.array(data.inputs))
    return {"predictions": predictions.tolist()}
