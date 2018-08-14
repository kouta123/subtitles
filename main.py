# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, render_template, session, redirect, url_for,send_from_directory
from werkzeug import secure_filename
import os
from Picture import Picture

#import MeCab

UPLOAD_FOLDER = './uploads'
app = Flask(__name__, static_url_path='', static_folder='./static')
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'test'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
pic = Picture()

@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        imgFile = request.files['img_file']
        if imgFile:
            filename = secure_filename(imgFile.filename)
            imgFile = pic.writeDescription(imgFile)
            imgFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            imgUrl = "/uploads/" + filename 
            return render_template('index.html',url=imgUrl)
        else:
            return render_template('index.html',fobidden = True)
    else:
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()