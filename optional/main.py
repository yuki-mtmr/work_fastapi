from typing import Optional


def get_profile(
        email: str,
        username: str,
        age: int
) -> dict:
    profile = {"email": email}
    if username:
        profile["username"] = username
    if age:
        profile["age"] = age
    return profile


user_profile = get_profile(email="user@examle.com")
print(user_profile)

complete_profile = get_profile(email="user@example.com", username="元太", age=30)

print(complete_profile)
