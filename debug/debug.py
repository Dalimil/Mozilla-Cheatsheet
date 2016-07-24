from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
	k = getJson()
	k[0] = list(range(5))
	k[1] = { "p1": "s1", "p2": ["a1", "a2", "a3"], "s3": "s3", "p4": "s4" }
	return jsonify(k)

def getJson():
	return json.loads(open('demo.json').read())

app.run(port=8080, debug=True)
