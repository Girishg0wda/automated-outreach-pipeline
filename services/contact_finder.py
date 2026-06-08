import random

CONTACTS = [
    ("Sarah Johnson", "CEO"),
    ("Michael Chen", "CTO"),
    ("David Brown", "VP Engineering"),
    ("Emma Wilson", "Head of Product"),
]

def find_contacts(company):

    name, title = random.choice(CONTACTS)

    return [
        {
            "name": name,
            "title": title,
            "linkedin": f"https://linkedin.com/in/{company.split('.')[0]}"
        }
    ]