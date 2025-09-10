from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Route backend sederhana untuk memproses form
@app.route('/proses', methods=['POST'])
def proses():
    nama = request.form.get('nama')
    return render_template('hasil.html', nama=nama)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
