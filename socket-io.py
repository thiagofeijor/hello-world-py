import socketio

sio = socketio.Client()

url = 'localhost'
port = 8000
channel = 'hi'

@sio.event
def connect():
    sio.emit('psubscribe', channel)
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect(f'http://{url}:{port}')
sio.wait()