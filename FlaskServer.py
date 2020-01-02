#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author　: Lemon pineapple
# @FileName: FlaskServer.py.py
# @Software: PyCharm
# @Github  : SkyBlueEternal.github.io Or skyblueeternal.gitee.io/blog

import os
from datetime import timedelta
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify
from lib_script import LookAppOs


app = Flask(__name__)

# 输出
@app.route('/')
def hello_world():
    return render_template('upload.html')


# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['apk'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)

# 添加路由
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # 通过file标签获取文件
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "文件类型：apk"})
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        # 保存文件
        f.save(upload_path)
        pack_name = LookAppOs.app_os_name_list(upload_path)
        # 返回上传成功界面
        return """
                     <html>
                        <body background='http://pic1.win4000.com/wallpaper/2019-12-29/5e086e329cec3.jpg'>
                             <h3>查壳情况：{0}</h3>
                             <a href="javascript:history.back(-1)">
                                 返回上一页
                             </a>
                        </body>
                     </html>
                  """.format(pack_name)
    # 重新返回上传界面
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")
