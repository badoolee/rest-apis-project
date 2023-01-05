from db import db

class BlockListModel(db.Model):
    __tablename__ = "blocklist"

    id = db.Column(db.Integer, primary_key=True)
    blocklist = db.Column(db.String(100), unique=True, nullable=False)