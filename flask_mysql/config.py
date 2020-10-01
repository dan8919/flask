db = {
    'user':'ca1',
    'password':'ca1',
    'host':'localhost',
    'database':'test'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"