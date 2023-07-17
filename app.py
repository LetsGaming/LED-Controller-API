from flask import Flask, send_file
from flask_cors import CORS
import importlib
import os

app = Flask(__name__)
CORS(app)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    """This function handles the request for the favicon.ico file."""
    return send_file(path_or_file=ROOT_DIR+"/favicon.ico", mimetype='image/vnd.microsoft.icon')

# Dynamically import and register API blueprints
api_directory = 'api'
not_allowed_names = ['__init__.py', 'config.py']

api_files = [file[:-3] for file in os.listdir(ROOT_DIR + "/" + api_directory) if file.endswith('.py') and file not in not_allowed_names]
for api_file in api_files:
    module = importlib.import_module(f'{api_directory}.{api_file}')
    blueprint = getattr(module, f'{api_file}_api')
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host="192.168.1.116", port=5000)
