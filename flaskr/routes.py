from datetime import datetime
import threading, time
from flask import current_app as app
from flask import Blueprint, render_template, copy_current_request_context, request, session

from flask_socketio import SocketIO

socketio = SocketIO()
stop_event = threading.Event()
daemon = threading.Thread()
isDaemonStarted = False

view = Blueprint("view", __name__)

@view.route("/")
def homepage():
    return render_template("homepage.html")

@socketio.on('dataToServer')
def on_dataToServer(data):
    field1 = data['field1']
    requestSid = request.sid
    socketio.emit('dataFromServer', {'datetime': str(datetime.now()), 'field1': field1, 'requestSid': requestSid})

@socketio.on('handleDaemon')
def on_handleDaemon(data):
    name=data['name']
    action=data['action']
    requestSid=request.sid

    @copy_current_request_context
    def daemonProcess(name, action, stop_event):
        while not stop_event.is_set():
            socketio.emit('daemonProcess', {'datetime': str(datetime.now()), 'name': name, 'action': action, 'requestSid': requestSid} )
            time.sleep(1)

    global isDaemonStarted
    if action == 'START':
        if not isDaemonStarted:
            daemon.__init__(target=daemonProcess, args=(name, action, stop_event), daemon=True)
            daemon.start()
            isDaemonStarted = True
    else:
        stop_event.set()
        daemon.join()
        stop_event.clear()
        isDaemonStarted = False
