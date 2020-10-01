# -*- coding: utf-8 -*- 

from flask import Flask

app = Flask(__name__)

#app->main->index.py
from app.main.index import main as main

#추가한 파일 연동. 이름을 main 이라 하였음
app.register_blueprint(main)