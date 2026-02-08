def create_user_profile(**kwargs):
    if kwargs.get("name") == None or kwargs.get("email") == None:
        raise ValueError("name and email are required fields!")
    result = {}
    result["name"] = kwargs.get("name")
    result["email"] = kwargs.get("email")
    result["role"] = kwargs.get("role", "user")
    result["active"] = kwargs.get("active", True)
    for key, value in kwargs.items():
        if key != "name" or "email" or "role" or "active":
            result[key] = value
    return result



# Test cases:
print(create_user_profile(name="Alice", email="alice@example.com"))
# Should return: {'name': 'Alice', 'email': 'alice@example.com', 'role': 'user', 'active': True}

print(create_user_profile(name="Bob", email="bob@example.com", role="admin"))
# Should return: {'name': 'Bob', 'email': 'bob@example.com', 'role': 'admin', 'active': True}

print(create_user_profile(name="Charlie", email="charlie@example.com", age=30, city="Vancouver"))
# Should return: {'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'user', 'active': True, 'age': 30, 'city': 'Vancouver'}

# This should raise ValueError:
# create_user_profile(name="Dave")  # Missing email