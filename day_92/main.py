import os
from flask import Flask, request, render_template
from PIL import Image
from collections import Counter

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_top_colors(image_path, num_colors=10):
    """Extracts the top common colors from an image."""
    image = Image.open(image_path).convert("RGB")
    image = image.resize((100, 100))  # Resize for faster processing
    pixels = list(image.getdata())
    color_counts = Counter(pixels)
    return color_counts.most_common(num_colors)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            colors = get_top_colors(file_path)
            return render_template('result.html', colors=colors, image=file.filename)
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
