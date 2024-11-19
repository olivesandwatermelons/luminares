import pymongo
import bcrypt

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["login_db"]
users = db["users"]

def insert_user(email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        "email": email,
        "password": hashed_password
    }
    users.insert_one(user_data)

def check_credentials(email, password):
    user = users.find_one({"email": email})
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return True
    return False

# Example usage:
insert_user("user@example.com", "password123")
if check_credentials("user@example.com", "password123"):
    print("Login successful")
else:
    print("Login failed")