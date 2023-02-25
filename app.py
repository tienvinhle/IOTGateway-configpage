from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_MOSBUS_FOLDER'] = '/etc/modbus'
app.config['UPLOAD_MQTT_FOLDER'] = '/etc/mqtt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadmodbus', methods=['POST'])
def upload_modbus():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_MOSBUS_FOLDER'], file.filename))
    return 'File uploaded successfully'

@app.route('/viewmodbusconfig')
def view_modbus_config():
    filename = '/etc/modbus/deviceConfig.conf'
    try:
        with open(filename, 'r') as f:
            config = f.read()
    except FileNotFoundError:
        config = 'No config file found'
    return config

@app.route('/uploadmqtt', methods=['POST'])
def upload_mqtt():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_MQTT_FOLDER'], file.filename))
    return 'File uploaded successfully'

@app.route('/viewmqttconfig')
def view_mqtt_config():
    filename = '/etc/mqtt/appConfig.conf'
    try:
        with open(filename, 'r') as f:
            config = f.read()
    except FileNotFoundError:
        config = 'No config file found'
    return config

if __name__ == '__main__':
    app.run(debug=True)
