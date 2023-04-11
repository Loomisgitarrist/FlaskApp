from flask import Flask, render_template, request, send_file
import qrcode
import os
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    # Generate QR code
    filename = f'{os.urandom(8).hex()}.png'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(os.path.join('static', 'qr_codes', filename))
    # Send QR code as attachment
    try:
        return send_file(os.path.join('static', 'qr_codes', filename),
                         as_attachment=True)
    except Exception as e:
        return str(e)
if __name__ == '__main__':
    app.run(debug=True)
