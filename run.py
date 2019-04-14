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
    articlesHtml = scraper.scrapeCrisUMArticlesHtml("https://cris.maastrichtuniversity.nl/portal/en/persons/herm-martens(9e6f27d3-215b-4de6-bbcf-406d9d6b6e66)/publications.html")

    return render_template("physician_profile.html",
                twitter_profile_name="HermMartens",
                physician_name=contents["title"],
                contents=contents["content"],
                profile_pic_url=contents["image_url"],
                articles_html=articlesHtml,
                zorgkaart_id="dermatoloog-martens-h-302277")

@app.route("/physician_zorgkaart/<string:zorgverlener_id>")
def physicianZorgkaartReview(zorgverlener_id):
    return scraper.scrapeZorgkaartResponse("https://www.zorgkaartnederland.nl/zorgverlener/" + zorgverlener_id)

app.run(debug=True, host='0.0.0.0', port=5000)