import os
from flask import Flask, render_template, request, send_from_directory
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    downloads_folder = os.path.expanduser('~/Downloads')
    ys.download(downloads_folder)
    return f'Successfully downloaded {ys.default_filename} to {downloads_folder}.'

if __name__ == '__main__':
    app.run()
