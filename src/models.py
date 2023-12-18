from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Car %r>' % self.brand

    def serialize(self):
        return {
            "id": self.id,
            "brand": self.brand,
            # do not serialize the password, its a security breach
        }