from flask import request
from flask_socketio import SocketIO, emit
from routes import app

socketio = SocketIO(app)
user_sockets={}

@socketio.on('connect')
def connect():
    print('User connected through socket')

@socketio.on('user-join')
def user_join(username):
    print(f'User {username} joined')
    user_sockets[username] = request.sid

@socketio.on('new-message')
def new_message(message):
    # print(message)
    username = ''
    for user in user_sockets:
        if user_sockets[user] == request.sid:
            username = user
    print(f'{message} received from {username}')

    emit("chat", {"message" : message, "username" : username},  broadcast=True)