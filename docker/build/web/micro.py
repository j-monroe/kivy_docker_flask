from flask import Flask, Response, redirect, url_for, request, session, abort, render_template, jsonify, flash
app = Flask(__name__)
import requests
import json
import re



def getCurrentWeather(place):
        tempArray = dict()
        whatToWear=dict()
        if place=='work':
                url = "http://api.openweathermap.org/data/2.5/weather/?zip=94107,us&APPID=6bffff6b452e9a774e9c3c05b60df33b"
        request = requests.get(url)
        if request.ok:
                tempArray = request.json()
                currentTempK = tempArray['main']['temp']
                currentTemp = currentTempK * 9/5 - 459.67
                if currentTemp <= 65.0 and currentTemp >= 60.0:
                        whatToWear['coat'] = "wind breaker"
                elif currentTemp <= 59.9 and currentTemp >= 55.0:
                        whatToWear['coat'] = "medium coat"
                elif currentTemp <= 54.9:
                        whatToWear['coat'] = "layers"
                return jsonify(whatToWear)





@app.route('/clothing')
def clothing():
        place = False
        inputToFilter = request.args.get('place')
        for char in inputToFilter:
                if not re.match(r'^[a-zA-Z]+$',inputToFilter):
                        return abort(405)
                else:
                        place = inputToFilter
                        return getCurrentWeather(place)



if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)
