from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app


main = Blueprint('main',__name__,url_prefix='/')

@main.route('/createAccount')
def createAccount():
    return render_template('/main/createAccount.html')


@main.route('/result',methods =['POST','GET'])
def result():
    if request.method =='POST':
        result = request.form
        return render_template('/main/createAccountSuccess.html',result = result)

@main.route('/maintest2')
def index():
    return render_template('/test/test1.html')