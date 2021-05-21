from flask import Flask, jsonify, render_template, request
import pandas as pd

users = pd.read_csv('aula-12/api-rest/users.csv').to_dict('records')

api = Flask(__name__)

@api.route('/')
def home():
  return render_template('home.html')

@api.route('/users', methods=['GET', 'POST'])
def users_route():
  if request.method == 'GET':
    return jsonify(users)
  if request.method == 'POST':
   
    new_user = {
      "id": len(users) + 1,
      "name": request.json["name"],
      "occupation": request.json["occupation"],
      "avatar_url": request.json["avatar_url"]
    }

    users.append(new_user)

    users_data_frame = pd.DataFrame(users)
    users_data_frame.to_csv('aula-12/api-rest/users.csv', index=False)

    return jsonify(new_user)

@api.route('/users-view')
def render_users():
  return render_template('list_users.html', users=users)

# if __name__ == '__main__':
api.run()