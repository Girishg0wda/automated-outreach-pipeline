from rich import print
from utils.logger import logger

def send_email(contact, email):

    logger.info(
        f"Sending email to {email}"
    )

    print(
        f"[green]Email sent to {email}[/green]"
    )