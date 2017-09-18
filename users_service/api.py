"""Initiates Flask's application and implements API endpoints"""


from flask import Flask, request, Response
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from config import get_config


app = Flask(__name__)
app.config.from_object(get_config())
mongo = PyMongo(app)


@app.route('/users', methods=['GET'])
def get_users():
    """Returns dict with all users
    :return: {'id': 'name', ...}
    """
    users = mongo.db.users.find()
    response = {str(user['_id']): user['name'] for user in users}
    return Response(response=json_util.dumps(response),
                    status=200,
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype='application/json')


@app.route('/users', methods=['POST'])
def create_user():
    """Add new user to the db."""
    data = request.get_json(force=True)
    if not data.get('name'):
        return Response(status=400,
                        headers={'Access-Control-Allow-Origin': '*'})
    mongo.db.users.insert_one(data)
    return Response(status=201,
                    headers={'Access-Control-Allow-Origin': '*'})


@app.route('/users/<user_id>', methods=['GET'])
def delete_user(user_id):
    """Remove selected user from db.
    :param str user_id: id of the user in db.
    """
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    return Response(status=204,
                    headers={'Access-Control-Allow-Origin': '*'})
