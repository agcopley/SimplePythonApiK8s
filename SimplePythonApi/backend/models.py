from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import current_app as app
from datetime import datetime


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://{}:{}@{}/{}'.format(app.config['POSTGRES_USER'],app.config['POSTGRES_PASSWORD'],app.config['POSTGRES_HOST'],app.config['POSTGRES_DB'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False           

db = SQLAlchemy(app)
ma = Marshmallow(app)



class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    blog = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow ,nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, type, source, blog, active):
        self.name=name
        self.type=type
        self.source=source
        self.blog=blog
        self.active=active

        
        


class DocumentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Document
    
    id = ma.auto_field()
    name = ma.auto_field()
    type = ma.auto_field()
    source = ma.auto_field()
    blog = ma.auto_field()
    create_date = ma.auto_field()
    active = ma.auto_field()
    create_date=ma.auto_field
    
db.create_all()
document_schema=DocumentSchema()     
    



