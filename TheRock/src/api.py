
from flask import request, Flask, jsonify
from flask import redirect, url_for, send_from_directory


app = Flask(__name__)

@app.route("/hello")
def hello():
    result = {'msg':'hello'}
    return jsonify(result)


if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0', port=5000)
                                         
