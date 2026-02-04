import hashlib
import string

def hash(password):
    result = hashlib.md5(password.encode())
    return result.hexdigest()

print(hash("H"))
print(hash("A"))
print(hash("HA"))

password = "1d52647ab12310b725d310127d974065"

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
all_charachters = digits + uppercase_letters + lowercase_letters
print(all_charachters)


for char_1 in all_charachters:
    for char_2 in all_charachters:
        for char_3 in all_charachters:
            for char_4 in all_charachters:
                control_password = char_1 + char_2 + char_3 + char_4
                if hash(control_password) == password:
                    print(f"your password is: {control_password}")
                    break
