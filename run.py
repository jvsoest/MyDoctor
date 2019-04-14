from flask import Flask, Response, request, render_template
import json
import scraper

app = Flask('MyDoctor')

@app.route("/")
def index():
    return render_template("index_search.html")

@app.route("/physician")
def physicianPage():
    contents = scraper.scrapeWebPageMumc("https://dermatologie.mumc.nl/medewerkers/martens")

    return render_template("physician_profile.html",
                twitter_profile_name="HermMartens",
                physician_name=contents["title"],
                contents=contents["content"],
                profile_pic_url=contents["image_url"])

app.run(debug=True, host='0.0.0.0', port=5000)