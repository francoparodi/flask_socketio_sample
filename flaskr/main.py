from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('dataToServer')
def on_dataToServer(data):
    field1=data['field1']
    emit('dataFromServer', {'datetime': str(datetime.now()), 'field1': field1})

if __name__ == '__main__':
    socketio.run(app, debug=True)