from flask import Flask, jsonify, render_template, request
import pandas as pd

df = pd.read_csv('aula-12/api-rest/users.csv')

users = [
  {
    "id": 1,
    "name": 'Paulo',
    "occupation": 'Designer',
    "avatar_url": "https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"
  },
  {
    "id": 2,
    "name": 'Ana',
    "occupation": 'Software developer',
    "avatar_url": "https://images.unsplash.com/photo-1542103749-8ef59b94f47e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"
  },
  {
    "id": 3,
    "name": 'Carla',
    "occupation": 'Software developer',
    "avatar_url": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80"
  },
  {
    "id": 4,
    "name": 'Bruna',
    "occupation": 'Software developer',
    "avatar_url": "https://images.unsplash.com/photo-1554151228-14d9def656e4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=633&q=80"
  }
]

users_data_frame = pd.DataFrame(users)

users_data_frame.to_csv('aula-12/api-rest/users.csv')

api = Flask(__name__)

@api.route('/')
def home():
  return render_template('home.html')

@api.route('/users', methods=['GET', 'POST'])
def users_route():
  if request.method == 'GET':
    return jsonify(users)
  if request.method == 'POST':
    # new_user_id = len(users) + 1
    # new_user_name = 'Felipe'
    # new_user_occupation = 'Teacher'
    # new_user_avatar_url = 'https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'

    new_user = {
      "id": len(users) + 1,
      "name": request.json["name"],
      "occupation": request.json["occ"],
      "avatar_url": request.json["avatar_url"]
    }

    users.append(new_user)

    users_data_frame = pd.DataFrame(users)
    print(users_data_frame)
    users_data_frame.to_csv('aula-12/api-rest/users.csv')

    return jsonify(new_user)

@api.route('/users-view')
def render_users():
  return render_template('list_users.html', users=users)


# if __name__ == '__main__':
api.run()