from flask import Flask,render_template,request,redirect,url_for,jsonify,abort
import glob
import time
import shutil
from travenityApi import searchTrains, checkTrain

app=Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
  json = request.get_json()
  destination = json["dest"]
  boarding = json["board"]
  result = searchTrains(boarding, destination)
  return result

@app.route('/check', methods=['POST'])
def check():
  json = request.get_json()
  metroId = json["metroId"]
  result = checkTrain(metroId)
  return result





if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)
