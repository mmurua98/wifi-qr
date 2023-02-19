from flask import Flask, redirect, render_template, request, send_file
import os
import shutil
import qr

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/generateQR", methods=['POST'])
def generateQR():
    txtWifiname = request.form['wifiname']
    txtPassword = request.form['password']

    #send data to function from qr.py
    qr.wifiInfo(txtWifiname, txtPassword)

    global pathDir, origin, target, qrFilePath, qrFilename

    #get path of qr image
    qrFilename = qr.getFileName()
    print(qrFilename)

    pathDir = os.getcwd()
    origin = pathDir + '\\' + qrFilename
    target = os.path.join(pathDir, 'static', qrFilename)

    qrFilePath = f"static/{qrFilename}"

    if os.path.exists(origin):
        shutil.move(origin, target)
    

    return render_template('index.html', qrpath = qrFilePath)

@app.route("/download",  methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        return send_file(qrFilePath, as_attachment=True, attachment_filename=qrFilename)
    
    return render_template('index.html')

# @app.route("/getQR")
# def getAudio():
#     return render_template('audio.html', pathAudio=audioName)


if __name__ == "__main__":
    app.run()