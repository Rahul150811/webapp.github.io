from flask import Flask
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post" action="/download">
            <label for="url">Enter YouTube video URL:</label>
            <input type="text" name="url" id="url">
            <button type="submit">Download</button>
        </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    filename = f'{video.title}.mp4'
    stream.download(filename)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
