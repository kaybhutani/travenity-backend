from flask import Flask,render_template,request,redirect,url_for,jsonify,abort
import glob
import time
import shutil
from travenityApi import searchTrains, checkTrain

app=Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
  board = request.form.get('board')
  dest = request.form.get('dest')
  print(board,dest)
  result = searchTrains(board, dest)
  return result

@app.route('/check', methods=['POST'])
def check():
  result = checkTrain(metroId)
  return result





if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)
