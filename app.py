from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/etc/modbus'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully'

@app.route('/viewconfig')
def view_config():
    filename = '/etc/modbus/deviceConfig.conf'
    try:
        with open(filename, 'r') as f:
            config = f.read()
    except FileNotFoundError:
        config = 'No config file found'
    return config

if __name__ == '__main__':
    app.run(debug=True)
