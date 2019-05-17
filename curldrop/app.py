import os
from flask import Flask, abort, request, send_file
from werkzeug.utils import secure_filename
from uuid import uuid4


app = Flask(__name__)


@app.route("/")
def index():
    return (
        '<a href="https://github.com/kennell/curldrop">curldrop</a> is up and running'
    )


@app.route("/<file>", methods=["PUT"])
def upload(file):
    uuid = uuid4().hex[:8]
    filename = uuid + "-" + secure_filename(file)
    savepath = os.path.join(app.config["UPLOAD_DIR"], filename)
    with open(savepath, "wb") as f:
        f.write(request.data)
    return app.config["BASE_URL"] + uuid


@app.route("/<uuid>", methods=["GET"])
def download(uuid):
    for file in os.listdir(app.config["UPLOAD_DIR"]):
        if file.startswith(uuid):
            return send_file(
                os.path.join(os.getcwd(), app.config["UPLOAD_DIR"], file),
                as_attachment=True,
                attachment_filename=file.split("-", 1)[1],
            )
    return abort(404)
