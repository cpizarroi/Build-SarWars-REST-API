from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade

@app.route('/')
def main():
    return jsonify({ "msg": "API REST FLASK" }), 200

@app.route("/api/users", methods=["GET","POST"])
def list_and_create_user():
    if request.method =="GET":
        user = User.query.all()
        user = list(map(lambda user: user.serialize(), user))
        return jsonify(user), 200

    if request.method =="POST":

        user_name = request.json.get('user_name')
        password = request.json.get('password')
        email = request.json.get('email')
        people = request.json.get('people')
        planets = request.json.get('planets')
        vehicles = request.json.get('vehicles')

        user = User()
        user.user_name = user_name
        user.email= email
        user.password = generate_password_hash(password)

        if people:
            for people_id in people:
                person = People.query.get(people_id)
                user.people.append(person)

        if planets:
            for planets_id in planets:
                planet = Planets.query.get(planets_id)
                user.planets.append(planet)

        if vehicles:
            for vehicles_id in vehicles:
                vehicle = Vehicles.query.get(vehicles_id)
                user.vehicles.append(vehicle)

        user.save()

        return jsonify(user.serialize()), 201


@app.route('/api/users/<int:id>', methods=['PUT','GET'])
def list_and_update_by_id(id):
    if request.method =="PUT":
        username = request.json.get('username')
        password = request.json.get('password')
        people_update = request.json.get('people')

        user = User.query.get(id)
        user.username = username
        user.password = generate_password_hash(password)

        if people_update:
            for person in user.people:
                if not person.id in people_update:
                    user.people.remove(person)

            for people_id in people_update:
                new_people = People.query.get(people_id)
                if not new_people in user.people:
                    user.people.append(new_people)


        user.update()

        return jsonify(user.serialize()), 200

    if request.method =="GET":

        user = User.query.get(id)
        return jsonify(user.serialize()), 200

@app.route('/api/users/<int:user_id>/people/<int:people_id>', methods=['POST', 'DELETE'])
def add_or_delete_fav_people(user_id, people_id):

    if request.method == 'POST':
        user = User.query.get(user_id)
        people_id = People.query.get(people_id)

        if not people_id in user.people:
            user.people.append(people_id)

        user.update()
        return jsonify(user.serialize()), 201
        

    if request.method == 'DELETE':
        user = User.query.get(user_id)
        people_id = People.query.get(people_id)

        user.people.remove(people_id )

        user.update()
        return jsonify(user.serialize()), 200

@app.route('/api/users/<int:user_id>/planets/<int:planets_id>', methods=['POST', 'DELETE'])
def add_or_delete_fav_planets(user_id, planets_id):

    if request.method == 'POST':
        user = User.query.get(user_id)
        planets_id = Planets.query.get(planets_id)

        if not planets_id in user.planets:
            user.planets.append(planets_id)

        user.update()
        return jsonify(user.serialize()), 201
        

    if request.method == 'DELETE':
        user = User.query.get(user_id)
        planets_id = Planets.query.get(planets_id)

        user.planets.remove(planets_id )

        user.update()
        return jsonify(user.serialize()), 200

@app.route('/api/users/<int:user_id>/vehicles/<int:vehicles_id>', methods=['POST', 'DELETE'])
def add_or_delete_fav_vehicles(user_id, vehicles_id):

    if request.method == 'POST':
        user = User.query.get(user_id)
        vehicles_id = Vehicles.query.get(vehicles_id)

        if not vehicles_id in user.vehicles:
            user.vehicles.append(vehicles_id)

        user.update()
        return jsonify(user.serialize()), 201
        

    if request.method == 'DELETE':
        user = User.query.get(user_id)
        vehicles_id = Vehicles.query.get(vehicles_id)

        user.vehicles.remove(vehicles_id )

        user.update()
        return jsonify(user.serialize()), 200


@app.route("/api/people", methods=["GET","POST"])
def list_and_create_people():
    if request.method =="GET":
        people = People.query.all()
        people = list(map(lambda people: people.serialize(), people))
        return jsonify(people), 200

    if request.method =="POST":
        data = request.get_json()
        people=People()
        people.Name = data["Name"]
        people.height = data["height"]
        people.mass = data["mass"]
        people.hair_color = data["hair_color"]

        db.session.add(people)
        db.session.commit()

        return jsonify(people.serialize()), 201

@app.route("/api/planets", methods=["GET","POST"])
def list_and_create_planets():
    if request.method =="GET":
        planets = Planets.query.all()
        planets = list(map(lambda planets: planets.serialize(), planets))
        return jsonify(planets), 200

    if request.method =="POST":
        data = request.get_json()
        planets=Planets()
        planets.Name = data["Name"]
        planets.rotation_period = data["rotation_period"]
        planets.orbital_period = data["orbital_period"]

        db.session.add(planets)
        db.session.commit()

        return jsonify(planets.serialize()), 201

@app.route('/api/planets/<int:id>', methods=['GET'])
def list_planets_by_id(id):

    planet = Planets.query.get(id)
    return jsonify(planet.serialize()), 200

@app.route('/api/people/<int:id>', methods=['GET'])
def list_people_by_id(id):

    person = People.query.get(id)
    return jsonify(person.serialize()), 200

@app.route('/api/vehicles/<int:id>', methods=['GET'])
def list_vehicles_by_id(id):

    vehicle = Vehicles.query.get(id)
    return jsonify(vehicle.serialize()), 200

@app.route("/api/vehicles", methods=["GET","POST"])
def list_and_create_vehicles():
    if request.method =="GET":
        vehicles = Vehicles.query.all()
        vehicles = list(map(lambda vehicles: vehicles.serialize(), vehicles))
        return jsonify(vehicles), 200

    if request.method =="POST":
        data = request.get_json()
        vehicles=Vehicles()
        vehicles.Name = data["Name"]
        vehicles.model = data["model"]
        vehicles.cost_in_credits = data["cost_in_credits"]

        db.session.add(vehicles)
        db.session.commit()

        return jsonify(vehicles.serialize()), 201


@app.route("/api/favorites_People", methods=["GET","POST"])
def list_and_create_favorites_People():
    if request.method =="GET":
        favorites_People = Favorites_People.query.all()
        favorites_People = list(map(lambda favorites_People: favorites_People.serialize(), favorites_People))
        return jsonify(favorites_People), 200

    if request.method =="POST":
        data = request.get_json()
        favorites_People=Favorites_People()
        favorites_People.planets_id = data["planets_id"]
        favorites_People.users_id = data["users_id"]


        db.session.add(favorites_People)
        db.session.commit()

        return jsonify(favorites_People.serialize()), 201

if __name__ == '__main__':
    app.run()