from rich import print
from utils.logger import logger
from services.brevo import send_brevo_email


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

    status_code, response = send_brevo_email(
    recipient_email=email,
    recipient_name=contact["name"],
    subject="Automated Outreach Demo",
    html_content=email_body.replace("\n", "<br>")
    )

    print(f"Status Code: {status_code}")
    print(f"Response: {response}")

    logger.info(
        f"Email to {email} - {status_code}"
    )

    if status_code == 201:
        print(
            f"[green]✓ Email sent to {email}[/green]"
        )
    else:
        print(
            f"[red]✗ Email failed ({status_code})[/red]"
        )