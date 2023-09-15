from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_cat_gif():
    url = "https://cataas.com/cat/gif?json=true"
    response = requests.request("GET", url)
    body = json.loads(response.text)
    gif_link = "https://cataas.com" + body["url"]
    return gif_link

def get_quote():
    url = "https://zenquotes.io/api/quotes"
    response = requests.request("GET", url)
    body = json.loads(response.text)
    quote = body[0]['q'] + " - " + body[0]['a']
    return quote

@app.route("/")
def index():
    quote = get_quote()
    cat_gif = get_cat_gif()
    return render_template("cat-index-fancy.html", cat_gif=cat_gif, quote=quote)

if __name__ == "__main__":
    app.run()
