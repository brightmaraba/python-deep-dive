from fastapi import FastAPI
from scrape import run as scrape_runner

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Message": "Hello World"}

@app.get("/bye")
def bye_world():
    return {"Message": "Bye World"}

@app.get("/box-oofice-mojo-scraper")
def scrape_runner_view():
    scrape_runner()
    return {"Message": "Done"}