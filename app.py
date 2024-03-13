from flask import Flask, render_template, request
import os
from extractText import TextExtractor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if not os.path.exists('static'):
        os.makedirs('static')

    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        ruta_del_archivo = os.path.join('static', pdf_file.filename)
        pdf_file.save(ruta_del_archivo)

        extractor = TextExtractor(ruta_del_archivo)
        pages_text = extractor.extract_text()
        extractor.save_to_csv(pages_text)

        return render_template('extractview.html', pages_text=pages_text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
