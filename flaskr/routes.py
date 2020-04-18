from datetime import datetime
from flask import current_app as app
from flask import Blueprint, render_template

from flask_socketio import SocketIO, emit

socketio = SocketIO()

view = Blueprint("view", __name__)

@view.route("/")
def homepage():
    return render_template("homepage.html")

@socketio.on('dataToServer')
def on_dataToServer(data):
    field1=data['field1']
    emit('dataFromServer', {'datetime': str(datetime.now()), 'field1': field1})
