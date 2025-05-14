def check_registration(form):
    errors = []

    email = form["email"].strip()
    username = form["username"].strip()
    password = form["password"]
    confirm_password = form["confirm_password"]

    if not (username) or not (email) or not (password) or not (confirm_password):
        errors.append("All fields must be filled out")

    if password != confirm_password:
        errors.append("Passwords must match")

    if len(password) < 6:
        errors.append("Password must be greater than or equal to 6 characters")

    if len(username) < 3:
        errors.append("Username must be greater than or equal to 3 characters")

    if len(errors) > 0:
        raise Exception(errors)
