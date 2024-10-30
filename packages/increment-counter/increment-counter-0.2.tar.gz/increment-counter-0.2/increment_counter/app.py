from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Initialize the counter variable
counter = 0

@app.route('/get_counter', methods=['GET'])
def retrieve_counter():
    """Return the current value of the counter as JSON."""
    global counter
    return jsonify({'counter': counter})

@app.route('/increment_counter', methods=['POST'])
def increment_counter():
    """Increase the counter by one and return the updated value."""
    global counter
    counter += 1
    return jsonify({'counter': counter})

@app.route('/reset_counter', methods=['POST'])
def reset_counter():
    """Reset the counter to zero and return the updated value."""
    global counter
    counter = 0
    return jsonify({'counter': counter})

@app.route('/')
def home():
    """Render the main HTML page."""
    return render_template('index.html')

if __name__ == "__main__":
    # Start the Flask application in debug mode on port 5000
    app.run(debug=True, port=5000)
