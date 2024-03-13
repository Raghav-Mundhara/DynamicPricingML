from flask import Flask, request, jsonify
import joblib
import math
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r"/getPrice": {"origins": "http://localhost:3000"}})

model = joblib.load('DynamicPricingFinal.joblib')
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getPrice", methods=['POST'])
def getPrice():
    response = request.get_json()
    print(response)
    service = response['service']
    if service == 'App':
        service = 0
    elif service == 'Docs':
        service = 2
    elif service == 'PPT':
        service = 5
    elif service == 'Website':
        service = 6
    elif service == 'Backend':
        service = 1
    elif service == 'Frontend':
        service = 4
    elif service == 'Figma':
        service = 3
    pages = response['no_of_pages']
    deadline = response['days']
    print(service, pages, deadline)
    price = model.predict([[service, pages, deadline]])
    return jsonify({'price': math.ceil(price[0])})



if __name__ == "__main__":
    app.run(debug=True)
