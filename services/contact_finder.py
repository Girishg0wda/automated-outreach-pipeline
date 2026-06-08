import random
CONTACTS = [
    ("Sarah Johnson", "CEO"),
    ("Michael Chen", "CTO"),
    ("David Brown", "VP Engineering"),
    ("Emma Wilson", "Head of Product"),
    ("Alex Morgan", "Founder"),
]

counter = 0

def find_contacts(company):

    global counter

    name, title = CONTACTS[
        counter % len(CONTACTS)
    ]

    counter += 1

    return [
        {
            "name": name,
            "title": title,
            "linkedin": (
                f"https://linkedin.com/in/"
                f"{name.lower().replace(' ', '-')}"
            )
        }
    ]