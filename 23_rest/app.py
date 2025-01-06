#Aditya and Stella
#Team YA
#SoftDev
#K23: NASA API
#2024-11-21
# Time Spent : .7 Hour

import urllib.request
import json
from flask import Flask, render_template

file = open('key_nasa.txt', 'r')
key = file.read()
file.close()

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + key
    UResp = urllib.request.urlopen(url)
    page_content = json.loads(UResp.read())
    return render_template('main.html', explanation = page_content['explanation'], image = page_content['hdurl'])

if __name__ == "__main__":
    app.debug = True 
    app.run()