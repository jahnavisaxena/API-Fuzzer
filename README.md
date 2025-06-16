# 🛠️ API Endpoint Enumnerator (GET Only)

A basic Python-based API fuzzer that tests a list of potential REST API endpoints using only the GET method. Useful for developers and beginners in security testing to discover accessible routes in Flask (or similar) web APIs.

---

## 🚀 What It Does

- Reads a list of endpoints from a wordlist file
- Sends HTTP GET requests to each endpoint
- Prints:
  - The HTTP status code (e.g. 200 OK, 404 Not Found, 405 Method Not Allowed)
  - The response content (parsed as JSON if possible, or raw text otherwise)

---

## 📂 Project Structure

```
simple-api-fuzzer/
├── fuzz.py                 # Python script that performs API fuzzing
├── custom_wordlist.txt     # Sample wordlist containing paths to test
└── README.md               # This file (project documentation)
```

---

## 🔧 Requirements

- Python 3.x
- `requests` library

To install the required package:

```bash
pip install requests
```

---

## ▶️ How to Use

1. Make sure your target Flask API is running on `http://127.0.0.1:5000`  
2. Create or edit the wordlist (`custom_wordlist.txt`) with possible endpoint paths:

```
api
api/users
api/login
```

3. Run the script using:

```bash
cat custom_wordlist.txt | python3 fuzz.py
```

---

## 📄 Code Explanation (`fuzz.py`)

```python
import requests
import sys

for word in sys.stdin:
    res = requests.get(f"http://127.0.0.1:5000/{word.strip()}")
    print(res)

    try:
        data = res.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response not in JSON")
        print(res.text)
```

### 💡 What It Does

| Line | Description |
|------|-------------|
| `import requests` | Imports the requests library to send HTTP requests |
| `import sys` | Allows reading input from the terminal (stdin) |
| `for word in sys.stdin:` | Loops through each line in the wordlist |
| `requests.get(...)` | Sends a GET request to the target path |
| `res.json()` | Tries to parse the response as JSON |
| `except...` | If response is not JSON, prints raw response text |

---

## 🧪 Sample Output

```
<Response [200]>
[{'name': 'Alice'}, {'name': 'Bob'}]

<Response [404]>
Response not in JSON
{"error": "Not found"}

<Response [405]>
Response not in JSON
Method Not Allowed
```

---

## 🧑‍💻 Sample Flask API (for Testing)

Here’s a minimal Flask server to test this script:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Fake API is running!", 200

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify([{"name":"Alice"}, {"name":"Bob"}]), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify({"message": "User created"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    return jsonify({"message": "Login successful"}), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
```

---

## 💡 Ideas for Future Improvement

- Add support for other HTTP methods (POST, PUT, DELETE)
- Include headers, authentication tokens
- Add concurrency with `threading` or `asyncio`
- Output to CSV or JSON file

---

## 👩‍💻 Author

**Jahnavi Saxena**  
💻 Python | Cybersecurity | Dev Enthusiast  
🌐 GitHub: [github.com/YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).
