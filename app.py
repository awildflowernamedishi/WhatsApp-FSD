# app.py 
# from flask import Flask, render_template, request
# from flask_socketio import SocketIO, emit
from routes import app
# from socket_events import SocketIO


# app = Flask(__name__) # __main__ or app.py
# socketio = SocketIO(app)

# python <filename> -> __main__
# python <some> -> import app.py -> app.py

# user_sockets = {}

# @app.route('/') # decorator
# def home():
#     # return 'Hello World'
#     return render_template('index.html')

# @socketio.on('connect')
# def connect():
#     print('User connected through socket')

# @socketio.on('user-join')
# def user_join(username):
#     print(f'User {username} joined')
#     user_sockets[username] = request.sid

# @socketio.on('new-message')
# def new_message(message):
#     # print(message)
#     username = ''
#     for user in user_sockets:
#         if user_sockets[user] == request.sid:
#             username = user
#     print(f'{message} received from {username}')

#     emit("chat", {"message" : message, "username" : username},  broadcast=True)


if __name__ == "__main__":
    # app.run()
    app.run(app)

# Run the code with `python app.py` in the virtual environment. 