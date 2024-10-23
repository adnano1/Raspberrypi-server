from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/')
def home():
    return "Welcome to your Raspberry Pi Server!"

@app.route('/status')
def status():
    return jsonify({
        'status': 'Server is running!',
        'message': 'This is served from a Raspberry Pi 4 Model B.'
    })

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)

