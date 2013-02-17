
import sys
from flask import request, Flask, jsonify
from flask import redirect, url_for, send_from_directory
from commandDispatcher import CommandDispatcher


app = Flask(__name__)
commandDispatcher = CommandDispatcher()

@app.route("/hello")
def hello():
    result = {'msg':'hello'}
    return jsonify(result)

@app.route("/command/<action>")
def action(action):
    if commandDispatcher.isAction(action):
        try: 
            result_from_action = commandDispatcher.execute(action)
            result = {"execution result":result_from_action}
        except :
            result = {"error": sys.exc_info()[0]}
    else:
        result = {"error":"no such action"}
    return jsonify(result)


if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0', port=5000)
                                         
