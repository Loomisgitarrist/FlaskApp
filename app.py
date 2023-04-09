from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/api/convert', methods=['POST'])
def convert_song():
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    os.system('your_conversion_command_here') # replace this with the command to convert the song using Falcon Cubase 12
    converted_file = filename + '.cpr' # replace this with the name of the converted file
    return send_file(converted_file, as_attachment=True)

if __name__ == '__main__':
    app.run()
