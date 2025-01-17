from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

from routes import main

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(main.bp)




if __name__ == '__main__':
    app.run(debug=True)

