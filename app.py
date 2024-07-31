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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://quinn_lab_10_user:8qOkcdHE9bBlNyxrNFm9RWbqfj4uaHlu@dpg-cqlat6pu0jms7389hs0g-a/quinn_lab_10")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://quinn_lab_10_user:8qOkcdHE9bBlNyxrNFm9RWbqfj4uaHlu@dpg-cqlat6pu0jms7389hs0g-a/quinn_lab_10")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

    