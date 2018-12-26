# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask, request, render_template, make_response

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

@app.route('/index', methods=['GET', 'POST'])
def index():
    print(request.method) #GET
    print(request.args)  #url.query
    print(request.form)  #form
    print(request.json)  #json
    print(request.path) #/index
    print(request.full_path)  #/index?name=123
    print(request.base_url)  #http://127.0.0.1:5000/index
    print(request.url)  #http://127.0.0.1:5000/index?name=123
    print(request.cookies)
    # request.files
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(f.filename))
    response = make_response(render_template('index.html'))
    response.set_cookie('123', '456')
    response.headers['X-Something'] = 'hahaha'
    # response.delete_cookie('123')
    return response
    # return render_template('index.html')

if __name__ == "__main__":
    app.run()