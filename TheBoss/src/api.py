import sys
import json
from flask import request, Flask, jsonify
from flask import redirect, url_for, send_from_directory
from apiHandler import ApiHandler


app = Flask(__name__)
commandDispatcher = ApiHandler()

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    result = {'msg':'hello boss'}
    return jsonify(result)

@app.route("/run", methods=['PUT'])
def add_new_run():
    #content = request.get_json(force=True) 
    #return jsonify(content)
    content = request.data
    result = json.loads(content)
    #result = {'a':content}                    
    return jsonify(result)
    return jsonify(result)


@app.route("/services", methods=['GET'])
def get_all_services():
    result ={'services':['a','b']}
    return jsonify(result)

@app.route("/service", methods=['PUT','POST'])
def add_new_service():
    #content = request.get_json(force=True)
    #content = request.data
    app.logger.error('??:'+ request.data)
   # return jsonify(json.loads(request.data))
    return {"a":"b"}
    #return jsonify(content)


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
                                         
