import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = make_webhook_result(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def make_webhook_result(req):
    if req.get("result").get("action") != "health":  # result of action being checked against health
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    health = parameters.get("health")
    reply = {"Hey": "what's up!"}   # so i added dependency for flask framework as a text file to the project.
    response = "it is" + str(reply[health])
    print(response)
    return {
            "fulfillmentText": response,
            "source": "pythonProject"
        }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')




