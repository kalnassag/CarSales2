from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from models import User, CarListing, Category, Garage, Order, ContactUs, AboutUs

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
