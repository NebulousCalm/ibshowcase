from flask import Flask, render_template, send_file, request


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("key.json", scopes) # json key (left out for security reasons :) 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("ibshowcase") # sheet name (https://docs.google.com/spreadsheets/d/1UjMEkAzH5mcjDG-lLxtNse4xX31RRzdgyey_rMuB484/edit#gid=0)
sheet = sheet.sheet1 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def form():
  name = request.form['name']
  takeaway = request.form['takeaway']
  ask = request.form['ask']
  
  #print(name + ' - ' + takeaway + ' - ' + ask)
  sheet.append_row([name, takeaway, ask])
  return render_template('thankyou.html', name=name)


app.run(debug=True)
