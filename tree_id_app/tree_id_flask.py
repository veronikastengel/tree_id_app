import os
import numpy as np
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from prediction3 import predicting
from tree_info import tree_infos

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = os.path.join('static', 'test_inputs', 'class')
EXP_FOLDER = os.path.join('static', 'tree_examples')
trees = tree_infos()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template("index.html", merror="No file selected!", genvis="hidden", ac2vis="hidden", ac3vis="hidden")
        file = request.files['file']
        # If the user does not select a file / the right filetype, error message shows
        if file.filename == '':
            return render_template("index.html", merror="No file selected!", genvis="hidden", ac2vis="hidden", ac3vis="hidden")
        elif not allowed_file(file.filename):
            return render_template("index.html", merror="Image type not allowed!", genvis="hidden", ac2vis="hidden", ac3vis="hidden")
        if file and allowed_file(file.filename):
            #checking and saving the file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            for files_old in os.listdir(app.config['UPLOAD_FOLDER']):
                file_old = os.path.join(app.config['UPLOAD_FOLDER'], files_old)
                os.unlink(file_old)
            file.save(filepath)
            #after saving the image, predict the tree species
            (pred, acc, pred2, acc2, pred3, acc3) = predicting(filepath)
            #only make predictions visible if predition is strong enough
            if float(acc) > 35:
                if float(acc2) > 20: 
                    ac2vi = "visible"
                else:
                    ac2vi = "hidden"
                if float(acc2) > 20 and float(acc3) > 10:
                    ac3vi = "visible"
                else:
                    ac3vi = "hidden"
                return render_template("index.html", merror="", mimg=filepath, mpred=pred, macc=acc, mpred2=trees[pred2][0], macc2=acc2, mpred3=trees[pred3][0], macc3=acc3, genvis="visible", ac2vis=ac2vi, ac3vis=ac3vi, engl=trees[pred][0], pt=trees[pred][1], tree_add=trees[pred][2], tree_txt=trees[pred][3])
            else:
                msg = "Sorry. This image could not be classified, it did not reach a 35% probability for any tree species. Please try another image!"
                return render_template("index.html", merror=msg, mimg=filepath, mpred=pred, genvis="hidden", ac2vis="hidden", ac3vis="hidden", tree_add="cork_oak")
    else:
        return render_template("index.html", error_msg="", mimg="tree-icon.jpg", genvis="hidden", ac2vis="hidden", ac3vis="hidden", tree_add="cork_oak")

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True, threaded=False)