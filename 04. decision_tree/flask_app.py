from flask import Flask

# # Initialize the Flask app
app = Flask(__name__)

# # Define a simple route (URL endpoint) that returns "Hello"
@app.route('/test', methods=['GET'])
def hello():
    return "Hello World"

@app.route('/ml', methods=['GET'])
def ml_function():
    return "We are Data Science students"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
