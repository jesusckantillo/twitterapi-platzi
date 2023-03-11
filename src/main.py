from fastapi import FastAPI

app = FastAPI()


#Models


@app.get(path="/")
def home():
    return {"Twitter API": "Working"}