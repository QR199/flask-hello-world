from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Quinn Ridgeway 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://quinn_lab_10_user:8qOkcdHE9bBlNyxrNFm9RWbqfj4uaHlu@dpg-cqlat6pu0jms7389hs0g-a/quinn_lab_10")
    conn.close()
    return "Database Connection Successful"