# coding: utf-8
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from os import path, makedirs, remove

from app.utils import *

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['Secret'] = "Secret"
app.config['UPLOAD_FOLDER'] = "./app/server/static/"


@app.route('/', methods=['GET'])  # To prevent Cors issues
@cross_origin(supports_credentials=True)
def index():
    # Build the response
    response = jsonify({'status': 'success', 'message': 'Welcome to Ogram API.'})
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')  # To prevent Cors issues
    return response


@app.route('/upload', methods=['POST'])  # To prevent Cors issues
@cross_origin(supports_credentials=True)
def upload():
    if not path.exists("./app/server/static/"):
        makedirs("./app/server/static/")

    try:
        chat_id = request.form.get("chat_id")
        file = request.files['file']
        response = {}

        if file and chat_id:
            if file.filename == '':
                print('No file selected for uploading !')
                response = jsonify({'status': 'error', 'message': 'No file selected for uploading !'})

            else:
                print("[+] Uploading file in static !")
                filename = secure_filename(file.filename)
                file.save(path.join(app.config['UPLOAD_FOLDER'], filename))

                json_path = send_file(chat_id, "./app/server/static/" + filename)

                response = jsonify({
                    'status': 'success',
                    'message': 'Your file ' + filename + ' have been saved successfully !',
                    'file_key': json_path.split("/")[-1].split("_")[1].split(".")[0],
                    'json_map': json.loads(open(json_path).read())
                })

                # We delete the original file
                remove("./app/server/static/" + filename)
        else:
            print("[x] Some parameters are missing, check your request again!")
            response = jsonify({
                "status": "error",
                "message": "Some parameters are missing, check your request again !"
            })
        # Let's allow all Origin requests
        response.headers.add('Access-Control-Allow-Origin', '*')  # To prevent Cors issues

        return response

    except Exception as es:
        print(es)


@app.route('/download/<file_key>', methods=['GET'])  # To prevent Cors issues
@cross_origin(supports_credentials=True)
def index2(file_key):
    json_map_file = "./json_maps/m_" + file_key + ".json"
    if not path.exists(json_map_file):
        print("[x] This json_map doesn't exist in the server !")
        # Build the response
        response = jsonify({'status': 'error',
                            "file_key": file_key,
                            'message': "This json_map doesn't exist in the server !"})
    else:
        saving_path = get_file(json_map_file)

        # Build the response
        response = jsonify({'status': 'success',
                            "file_key": file_key,
                            'message': 'file restored successfully !',
                            'download_link': request.host_url +
                            saving_path.replace("./", "/").replace("/app/server/", "")})
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')  # To prevent Cors issues
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
