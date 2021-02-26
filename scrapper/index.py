import requests
from flask import jsonify
from bs4 import BeautifulSoup
import scrapper
from db.index import Db
import re
from decouple import config

#Initializate database
database = Db()

def getData():
    """
    Get data of site finanzas.yahoo, get the first 5 days and save in DB
    """
    #Url of the site
    url = "https://es-us.finanzas.yahoo.com/quote/EURUSD%3DX/history?p=EURUSD%3DX"
    response = requests.get(url)
    #Get data of the site
    html = BeautifulSoup(response.text, 'html.parser')
    #Find html elements are contains the data
    data_badge = html.find_all('td', class_="Py(10px)")

    position = 1
    for i in range(0, 5):
        database.insert(re.split(r"><", data_badge[position].text)[0], re.split(r"><", data_badge[position - 1].text)[0])
        position = position + 7

    hitEndpoint()

def hitEndpoint():
    """
    Hit webhook with the new badges
    """
    data_to_return = []
    data_badge = database.get(5)
    for item in data_badge:
        data_json = {
            'value': item[0],
            'date': item[1]
        }
        data_to_return.append(data_json)
    requests.post(config("URL_POST", jsonify({'data': data_to_return})))