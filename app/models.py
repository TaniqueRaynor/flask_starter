from . import db 
class PropertyFile(db.Model):     
    
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)    
    ptitle = db.Column(db.String(80))
    rooms =  db.Column(db.Integer())
    bathrooms = db.Column(db.Integer())
    location = db.Column(db.String(80))
    price = db.Column(db.Integer())
    descr = db.Column(db.String(255))
    ptype = db. Column(db.String())
    photo = db.Column(db.Text())

     
def __init__(self, ptitle, rooms,bathrooms,location,price,descr,ptype,photo): 
        self.ptitle = ptitle
        self.rooms =  rooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.descr = descr
        self.ptype = ptype
        self.photo = photo