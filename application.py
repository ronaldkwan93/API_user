from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.password}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/users')
def get_users():
    users = User.query.all()

    output = []
    for user in users:
        user_data = {'name': user.name, 'password': user.password}

        output.append(user_data)
    return {"users" : output}

@app.route('/users/<id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return {"name": user.name, "password": user.password}

@app.route('/users', methods=['POST'])
def add_user():
    user = User(name=request.json['name'], password=request.json['password'])
    db.session.add(user)
    db.session.commit()
    return {'id': user.id}

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "not found"}
    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted"}

