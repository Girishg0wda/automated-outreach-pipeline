from rich import print
from utils.logger import logger


def generate_email(contact):

    with open(
        "templates/outreach.txt",
        "r",
        encoding="utf-8"
    ) as f:

        template = f.read()

    return template.format(
        name=contact["name"],
        company=contact["company"]
    )


def send_email(contact, email):

    email_body = generate_email(contact)

    logger.info(
        f"Sending email to {email}"
    )

    print("\n" + "=" * 50)
    print(f"TO: {email}")
    print("=" * 50)
    print(email_body)

    print(
        f"\n[green]Email sent to {email}[/green]"
    )