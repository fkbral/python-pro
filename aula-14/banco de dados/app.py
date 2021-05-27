import json
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()

class User(db.Model, SerializerMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)

  def __repr__(self) -> str:
      return f'Usuário de id = {self.id}, nome = {self.name} e email = {self.email}\n'

db.create_all()

def objectListToDict(objectList): 
  list = []
  for object in objectList:
    objectDict = object.to_dict()
    list.append(objectDict)
  return list

@app.route('/users')
def listAllUsers():
  users = User.query.all()
  # Alternativa para fazer a mesma pesquisa em SQL:
  # users = db.engine.execute('SELECT id, email FROM user')
  # for user in users:
  #   print(user)

  return jsonify(objectListToDict(users))

@app.route('/users', methods=['POST'])
# Criação de usuário
def storeUser():
  name = request.json["name"]
  email = request.json["email"]

  userExists = User.query.filter_by(email=email).first()

  if userExists:
    return f"Usuário com email {email} já está cadastrado no Banco de Dados"

  newUser = User(name=name, email=email)
  db.session.add(newUser)
  db.session.commit()
  return jsonify(newUser.to_dict())

@app.route('/users', methods=['PUT'])
# Atualização de usuário
def updateUser():
  name = request.json["name"]
  email = request.json["email"]
  new_email = request.json["new_email"]

  userToUpdate = User.query.filter_by(email=email).first()

  if not userToUpdate:
    return 'Usuário não encontrado'

  userExists = User.query.filter_by(email=new_email).first()

  if userExists:
    return f"Usuário com novo email fornecido ({email}) já está cadastrado no Banco de Dados"

  userToUpdate.name = name
  userToUpdate.email = new_email
  db.session.commit()

  return jsonify(userToUpdate.to_dict())

@app.route('/users', methods=['DELETE'])
# Deleção de usuário
def deleteUserByEmail():
  email = request.json["email"]

  userToDelete = User.query.filter_by(email=email).first()

  if not userToDelete:
    return "Usuário não encontrado"

  db.session.delete(userToDelete)
  db.session.commit()
  return jsonify()

app.run()

# deleteUserByEmail("fulano2@email.com")