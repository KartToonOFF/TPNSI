from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

IMAGE_FOLDER = './static/images'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def download_upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image trouvée dans la requête'}), 400
    file = request.files['image']


    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) 
        filepath = os.path.join(app.config['IMAGE_FOLDER'], filename)
        file.save(filepath)

        results = True
        return jsonify({'message': 'Image téléchargée avec succès', 'results': results})

    else:
        return jsonify({'error': 'Fichier non autorisé ou invalide'}), 400
    

if __name__ == "__main__":
    app.run(debug=True)
