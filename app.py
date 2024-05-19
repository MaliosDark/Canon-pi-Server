from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def gallery():
    files = os.listdir('static')
    files.sort(reverse=True)
    return render_template('index.html', files=files)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('static', filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    file_path = os.path.join('static', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('gallery'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
