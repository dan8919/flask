from flask import Flask,request,jsonify,current_app
from sqlalchemy import create_engin,text

def create_app(test_config = None):
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

#생성한 Engin 객체를 Flask 객체에 저장
    database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
    app.database = database
    
    
    






    # @app.route("/sign-up",methods=['post'])
    # def sign_up():
    #     new_user = request.json
    #     new_user_id = app.database.execute(text
    #     ("""  
    #     Insert into users(name,email,profile,hashed_password) values (:name, :email, :profile, :password)
    #     """),new_user).lastrowid
    #     row = current_app.database.execute(text
    #     ("""
    #     select id, name,email,profile from users where id = :user_id
    #     """),{'user_id':new_user_id}).fetchone()
        
    #     created_user = {
    #     'id':row['id'],
    #     'name':row['name'],
    #     'email':row['email'],
    #     'profile':row['profile']
    #     }if row else None


    #     return jsonify(created_user)


















#Flask 객체를 리턴.create_app 이라는 함수는 Flask가 자동 인지하여 Flask 객체를 찾아서 실행
    return app




