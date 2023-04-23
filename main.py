import flask

app = flask.Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = flask.request.json
    print(data) # Do something with the data received
    return 'Data received'

app.run(host='localhost', port=8080)
