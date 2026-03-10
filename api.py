from flask import Flask, request

app = Flask(__name__)

# read pickle file hier (add before the file)

@app.route("/")
def hello_world():
    return "<h2>Hello, World! My name is Gerli, whats your name?</h2>"

@app.route("/api", methods=["POST"])
def sentiment():
    body_data = request.get_json()
    print("Body data:")
    print(body_data["data"])
    return {"message": "Hello from localproject - api!!!"}