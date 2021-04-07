# encoding:utf-8
# !/usr/bin/env python
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/up_photo1',methods=['post'],strict_slashes=False)
def api_upload1():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        f.save(os.path.join(file_dir, fname))
        # 输出图片上传后的文件地址
        path = file_dir + "\\" + fname
        return path

if __name__ == '__main__':
    app.run(debug=True, port=5000)
