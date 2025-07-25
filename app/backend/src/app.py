from flask import Flask, request, jsonify
import boto3
import jwt
import json

app = Flask(__name__)

JWT_SECRET = 's$V8p&!eV2A94x!2G8Ndl@9x#Qp72Ld3Zf!vN!rTgH9L6D7k'
dynamodb = boto3.resource('dynamodb')
table_name = 'Users'
table = dynamodb.Table(table_name)

# ---------------- JWT Utility Functions ----------------

def generate_access_token(username):
    return jwt.encode({'username': username}, JWT_SECRET, algorithm='HS256')

def get_username_from_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return payload.get('username')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# ------------------- LOGIN -------------------

@app.route('/login', methods=['POST'])
def login():
    event = request.json
    username = event.get('username')
    password = event.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    try:
        response = table.get_item(Key={'username': username})
        item = response.get('Item')

        if not item or item.get('password') != password:
            return jsonify({'error': 'Invalid username or password'}), 401

        token = generate_access_token(username)
        return jsonify({'access_token': token}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ------------------- SIGNUP -------------------

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    required_fields = ['username', 'password']
    
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400

    try:
        # Check if user exists
        response = table.get_item(Key={'username': data['username']})
        if 'Item' in response:
            return jsonify({'error': 'User already exists'}), 400

        # Create new user
        table.put_item(Item={
            'username': data['username'],
            'password': data['password']
        })

        return jsonify({'message': 'User registered successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ------------------- TOKEN VALIDATION -------------------

@app.route('/validate_token', methods=['GET'])
def validate_token():
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.split('Bearer ')[-1] if 'Bearer ' in auth_header else auth_header

    username = get_username_from_token(token)
    if not username:
        return jsonify({'error': 'Invalid or expired token'}), 401

    return jsonify({'user': username}), 200

# ------------------- MAIN -------------------

if __name__ == '__main__':
    app.run(debug=True)

