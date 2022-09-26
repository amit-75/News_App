from flask import Flask, render_template, request,json
import requests
import urllib.request

app = Flask(__name__)
@app.route('/')
def home():
    return "hello world"


@app.route('/india')
def india():
    url_in = "https://newsapi.org/v2/top-headlines?country=in&apiKey=46f394326e794dc1be07338bff5c5744"
    response = urllib.request.urlopen(url_in)
    data = response.read()
    dict = json.loads(data)
    articles_in = dict['articles']
    return render_template('news.html',articles=articles_in)


@app.route('/america')
def america():
    url_us = "https://newsapi.org/v2/top-headlines?country=us&apiKey=46f394326e794dc1be07338bff5c5744"

    response = urllib.request.urlopen(url_us)
    data = response.read()
    dict = json.loads(data)
    articles_us = dict['articles']
    return render_template('news.html',articles=articles_us)


if __name__ == '__main__':
    app.run(debug=True)