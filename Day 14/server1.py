from flask import Flask
from scrape import run as scrape_runner


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, word. This is flask"

@app.route("/abc", methods=['GET'])
def abc_view():
    return "Hello, word. This is flask/abc"

@app.route("/box-oofice-mojo-scraper", methods=['GET'])
def box_office_scrapper():
    scrape_runner()
    return "Done"
