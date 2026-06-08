from services.company_finder import find_similar_companies
from services.contact_finder import find_contacts
from services.email_finder import find_email
from services.mailer import send_email

import pandas as pd
import os


def main():

    seed_domain = input("Enter company domain: ")

    companies = find_similar_companies(seed_domain)

    all_contacts = []

    for company in companies:

        contacts = find_contacts(company)

        for contact in contacts:

            email = find_email(contact)

            contact["company"] = company
            contact["email"] = email

            all_contacts.append(contact)

    os.makedirs("outputs", exist_ok=True)

    df = pd.DataFrame(all_contacts)

    df.to_csv(
        "outputs/contacts.csv",
        index=False
    )

    print("\nSaved contacts.csv")

    print("\n=== CONTACTS FOUND ===\n")
    print(df)

    confirm = input(
        "\nSend emails? (y/n): "
    )

    if confirm.lower() == "y":

        for contact in all_contacts:

            send_email(
                contact,
                contact["email"]
            )


if __name__ == "__main__":
    main()