from application import db

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    message = db.Column(db.Text)
    