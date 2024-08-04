from pymongo import MongoClient

# Encode special characters in the password
client = MongoClient("mongodb+srv://manishkumar:manish%40792002@cluster0.gdt7y2m.mongodb.net/")

db = client["ManishDB"]
users_collection = db["Users"]

def store_user_data():
    # Get user input
    user_name = input("Enter user name: ")
    user_email = input("Enter user email: ")
    user_age = int(input("Enter user age: "))

    # Create a user document
    user_data = {
        "name": user_name,
        "email": user_email,
        "age": user_age
    }

    # Insert the user document into the collection
    result = users_collection.insert_one(user_data)
    print(f"User added with id: {result.inserted_id}")

# Call the function to store user data
store_user_data()