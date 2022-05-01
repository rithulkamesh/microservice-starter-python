from flask import Flask
from database import Database

config = {
    'user': "localhost", 'password': "password", 'host': "localhost", 'database': "testDatabase"
}

app = Flask(__name__)
db = Database(config)
cursor = db.get_cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS testTable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
