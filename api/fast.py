from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"greeting": "Aguante RiBer"}


@app.get("/predict")
def predict(uploaded_file):
    return 'metal'
