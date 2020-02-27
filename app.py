from flask import Flask

UPLOAD_FOLDER = '/file_upload_app/file_upload'

app = Flask(__name__)
app.secret_key = "Revo-Ex"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024