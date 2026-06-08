import requests
from config import BREVO_API_KEY


def send_brevo_email(
    recipient_email,
    recipient_name,
    subject,
    html_content
):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "Girish R",
            "email": "girishgowda0239@gmail.com"
        },
        "to": [
            {
                "email": recipient_email,
                "name": recipient_name
            }
        ],
        "subject": subject,
        "htmlContent": html_content
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.status_code, response.text