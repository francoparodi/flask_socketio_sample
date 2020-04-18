# Flask SocketIO Sample

## Getting Started
A sample socketIO with Flask, using Application Factory.

### Prerequisites

### Installing

## Running

__as app__

```sh
export FLASK_APP=flaskr
flask run
```

__as wsgi server__

```sh
gunicorn --worker-class eventlet -w 1 -b localhost:8080 wsgi
```

## Deployment

As seen above (gunicorn...)

## Authors 

## License

This project is licensed under the MIT License