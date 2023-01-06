from flask import Flask,request
import os

from flask.templating import render_template
from werkzeug.utils import send_from_directory
app = Flask(__name__)

@app.route("/")
def root():
    response=""
    list=[]
    # Öffnen der Workstation-Datei, um die Clients auszulesen
    workstations=open("./workstations","r")
    # Durchschleifen aller Workstations, um deren Inhalt in das Array für das Template aufzunehmen
    for line in workstations:
            splittedValues=line.split(";")
            list.append([splittedValues[0],splittedValues[1],splittedValues[2].replace(":","-")])
    data={"list":list}

    return render_template("index.html",data=data)

@app.route("/<mac>")
def wake(mac):
    # MAC-Adresse als URL auslesen und umwandeln
    mac=mac.replace('-',':')
    os.system("etherwake -i ens160 "+mac)

    return render_template("mac.html",mac=mac)

@app.route('/favicon.ico') 
def favicon():
        # Leeres Favicon zurückgeben, da dieses vom Browser angefordert wird
        return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081)