# -*- coding: utf-8 -*- 

from flask import Flask

app = Flask(__name__)

#app->main->index.py
from app.main.index import main as main
from app.main.main import main as main
from app.test.test import test as test

#추가한 파일 연동. 이름을 main 이라 하였음
app.register_blueprint(main)
app.register_blueprint(test)