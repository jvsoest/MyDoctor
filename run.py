from flask import Flask, Response, request, render_template
import json

app = Flask('MyDoctor')

@app.route("/")
def index():
    return render_template("index_search.html")

@app.route("/physician")
def physicianPage():
    return render_template("physician_profile.html",
                twitter_profile_name="HermMartens",
                physician_name="Herm Martens")

app.run(debug=True, host='0.0.0.0', port=5000)