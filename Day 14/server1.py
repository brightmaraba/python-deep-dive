from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, word. This is flask"

@app.route("/abc", methods=['GET'])
def abc_view():
    return "Hello, word. This is flask/abc"

@app.route("/box-ofice-mojo-scraper", methods=['POST'])
def box_office_scrapper():
    trigger_log_save()
    scrape_runner()
    return {"Message": "Done"}
