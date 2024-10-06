from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

Class User(db.Model):
    _tablename_='User'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False,)
    email = db.Column(db.String(100), nullable=False, unique=True)
    people = db.relationship('People', secondary="Favorites_people")
    planets = db.relationship('Planets', secondary="Favoreites_planets")
    vehicles = db.relationship('Vehicles', secondary="Favorites_vehicles")

Favorites_people = db.Table('Favorites_people',
    db.Column('people_id', db.Integer, db.Foreignkey('People.id'), primary_key=True),
    db.Column('users_id', db.Integer, db.Foreignkey('User.id'), primary_key=True)
)

Favorites_vehicles = db.Table('Favorites_vehicles',
    db.Column('vehicles_id', db.Integer, db.Foreignkey('Vehicles.is'), primary_key=True),
    db.Column('users_id', db.Integer, db.Foreignkey('User.id'), primary_key=True)
)

Favorites_planets = db.Table('Favorites_planets',
    db.Column('planets_id', db.Integer, db.Foreignkey('Planets.id'), primary_key=True),
    db.Column('users_id', db.Integer, db.Foreignkey('User.id'), primary_key=True)
)

def serialize(self):
    return {
        "id": self.id,
        "username": self.username
    }
def save(self):
    db.session.add(self)
    db.session.commit()

def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()

class People(db.Model):
    _tablename_= 'People'
    id = db.Column(db.Integer, primary_key=True)    
    Name = db.Column(db.String(100), nullable=False, unique=True)
    height = db.Column(db.Integer, nullable=False,)
    mass = db.Column(db.Integer, nullable=False,)
    hair_color = db.Column(db.String(100), )
    users = db.relationship('User', secondary=Favorites_people)

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()    

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planets(db.Model):
    _tablename_= 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False, unique=True)
    rotation_period = db.Column(db.Integer, nullable=False,)
    orbital_period = db.Column(db.Integer, nullable=False,)

    def serialize(self):
        return {
            "id":self.id,
            "Name": self.Name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Vehicles(db.Model):
    _tablename_= 'Vehicles'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False, unique=True)
    model = db.Column(db.String(100), )
    cost_in_credits = db.Column(db.Integer, nullable=False,)

      def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "model": self.model,    
            "cost_in_credits": self.cost_in_credits,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        