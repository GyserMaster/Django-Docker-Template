from flask import Flask, jsonify
from users import users

def myapp():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def ping():
        return jsonify({"response": "hello world"})

    @app.route('/users', methods=['GET'])
    def usersHandler():
        return jsonify({"users": users})

    return app
'''if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
# /bin/sh -c "python3 app.py"    
'''