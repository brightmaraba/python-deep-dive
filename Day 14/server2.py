from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Message": "Hello World"}

@app.get("/bye")
def bye_world():
    return {"Message": "Bye World"}