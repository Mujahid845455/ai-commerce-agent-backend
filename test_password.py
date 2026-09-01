from app.utils.security import (
    hash_password,
    verify_password
)


password = "StrongPassword123"

hashed = hash_password(password)

print("HASH:")
print(hashed)

print()

print("PASSWORD MATCH:")
print(
    verify_password(
        password,
        hashed
    )
)