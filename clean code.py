# data user (bisa dikembangkan)
USERS = {
    "admin": "123",
    "user1": "abc"
}


def validate_login(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False


def show_success(username):
    print("Login berhasil")
    print(f"Selamat datang {username}")


def show_error():
    print("Login gagal")
    print("Coba lagi")


# input
username_input = input("Username: ")
password_input = input("Password: ")

# process
is_valid = validate_login(username_input, password_input)

# output
if is_valid:
    show_success(username_input)
else:
    show_error()