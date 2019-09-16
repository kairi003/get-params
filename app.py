from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            json_data = dict(request.form)
        else:
            json_data = dict(request.args)
    except Exception as e:
        json_data = {}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
