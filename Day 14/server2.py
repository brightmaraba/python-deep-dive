from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Message": "Hello World"}

@app.get("/bye")
def bye_world():
    return {"Message": "Bye World"}

@app.get("/box-office-mojo-scraper")
def scrape_runner_view():
    trigger_log_save()
    scrape_runner()
    return {"Message": "Done"}