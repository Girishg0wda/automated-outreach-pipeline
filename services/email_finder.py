def find_email(contact):

    username = (
        contact["name"]
        .lower()
        .replace(" ", ".")
    )

    company_domain = contact["company"]

    return f"{username}@{company_domain}"