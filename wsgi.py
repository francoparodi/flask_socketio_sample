from flaskr import app as application
from flaskr import socketio

if __name__ == "__main__":
    socketio.run(application, debug=True)