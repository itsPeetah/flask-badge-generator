import os
from flask import Flask, request, send_file
from generate_image import generate_image

app = Flask(__name__)


def get_image_path(name):
    img_dir = "/static/images"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, name)
    return img_path


@app.route("/")
def make_img():
    args = request.args
    if "text" not in args:
        return
    text = args["text"]
    imgName = get_image_path(text + ".png")
    if not os.path.exists(imgName):
        generate_image("images/badge.png", "fonts/Impact.ttf", text, imgName)
    return send_file(imgName, mimetype='image/png')


@app.route("/badge")
def serve_static():
    args = request.args
    if "text" not in args:
        return
    text = args["text"]
    imgName = get_image_path(text + ".png")
    if not os.path.exists(imgName):
        generate_image("images/badge.png", "fonts/Impact.ttf", text, imgName)
    return f'<img alt="badge" src="{imgName}" />'