from flask import Flask, jsonify, request
import csv

all_articles = []

with open("articles.csv","r",encoding = 'utf-8') as f:
    articles = csv.reader(f)
    articles_list = list(articles)
    all_articles = articles_list[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)
@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success!!"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success!!"
    }),201

@app.route("/disliked-articles", methods=["POST"])
def disliked_articles():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonfiy({
        "status":"success!!"
    }),201

if __name__=="__main__":
    app.run()