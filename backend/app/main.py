from fastapi import FastAPI
from enum import Enum

# Providing the options for the model_name path parameter
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# Create FastAPI instance
# Add openapi_url later go to FastAPI defition to see how to add openapi_url
app = FastAPI(title="Risk Scoring Engnine API", 
              description="This is a risk scoring engine API", 
              version="1.0.0")

# tells FastAPI that the function right below is in charge of handling requests that go to: the path / using a get operation
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# 
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
    # Defining the response body
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}