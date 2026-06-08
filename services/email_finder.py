def find_email(contact):
    username = (
        contact["name"]
        .lower()
        .replace(" ", ".")
    )

    return f"{username}@company.com"