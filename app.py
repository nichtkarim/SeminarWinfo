from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL Verbindung herstellen
conn = psycopg2.connect(
    dbname='postgres', user='postgres', password='mysecretpassword',
    host='localhost', port='5432'
)
cur = conn.cursor()

# API Endpoint
@app.route('/')
def index():
    cur.execute('SELECT * FROM users;')
    data = cur.fetchall()
    users = [{'id': row[0], 'name': row[1]} for row in data]
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
