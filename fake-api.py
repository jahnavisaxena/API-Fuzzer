from flask import Flask, jsonify, request

app = Flask(__name__)

#  home route
@app.route('/')
def home():
    return "Fake API is running!", 200

# GET: Return list of users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return jsonify(users), 200

# POST: Create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({
        "message": "User created successfully",
        "user": data
    }), 201

# POST: Simple login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "admin" and password == "admin":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Login failed"}), 401

# 404 for undefined routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
