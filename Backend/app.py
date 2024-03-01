from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# with open ('DynamicPrice.pkl','rb') as file:
#     model = pickle.load(file)

model = joblib.load('DynamicPrice.joblib')
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
        service = 1
    elif service == 'PPT':
        service = 2
    elif service == 'Website':
        service = 3
    pages = response['no_of_pages']
    deadline = response['days']
    print(service, pages, deadline)
    price = model.predict([[service, pages, deadline]])
    return jsonify({'price': price[0]})



if __name__ == "__main__":
    app.run(debug=True)
