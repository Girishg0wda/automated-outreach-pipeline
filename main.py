from services.company_finder import find_similar_companies
from services.contact_finder import find_contacts
from services.email_finder import find_email
from services.mailer import send_email

import pandas as pd
import os


def main():

    print("\n===== AUTOMATED OUTREACH PIPELINE =====\n")

    seed_domain = input("Enter company domain: ")

    print("\n[STAGE 1] Company Discovery")

    companies = find_similar_companies(seed_domain)

    print(f"Found {len(companies)} companies")

    all_contacts = []

    print("\n[STAGE 2] Contact Discovery")

    for company in companies:

        contacts = find_contacts(company)

        for contact in contacts:

            email = find_email(contact)

            contact["company"] = company
            contact["email"] = email

            all_contacts.append(contact)

    print(f"Found {len(all_contacts)} contacts")

    print("\n[STAGE 3] Deduplication")

    seen = set()
    unique_contacts = []

    for contact in all_contacts:

        if contact["email"] not in seen:

            seen.add(contact["email"])
            unique_contacts.append(contact)

    all_contacts = unique_contacts

    print(f"Unique contacts: {len(all_contacts)}")

    print("\n[STAGE 4] Export Results")

    os.makedirs("outputs", exist_ok=True)

    contacts_df = pd.DataFrame(all_contacts)

    contacts_df.to_csv(
        "outputs/contacts.csv",
        index=False
    )

    companies_df = pd.DataFrame(
        {"company": companies}
    )

    companies_df.to_csv(
        "outputs/companies.csv",
        index=False
    )

    emails_df = pd.DataFrame(
        {"email": [c["email"] for c in all_contacts]}
    )

    emails_df.to_csv(
        "outputs/emails.csv",
        index=False
    )

    print("Saved:")
    print(" - outputs/companies.csv")
    print(" - outputs/contacts.csv")
    print(" - outputs/emails.csv")

    print("\n===== SUMMARY =====")

    print(f"Companies Found : {len(companies)}")
    print(f"Contacts Found  : {len(all_contacts)}")
    print(f"Emails Found    : {len(all_contacts)}")

    print("\n===== CONTACT PREVIEW =====\n")

    print(
        contacts_df[
            ["name", "title", "company", "email"]
        ]
    )

    confirm = input(
        "\nProceed with email sending? (y/n): "
    )

    if confirm.lower() == "y":

        print("\n[STAGE 5] Outreach")

        for contact in all_contacts:

            send_email(
                contact,
                contact["email"]
            )

        print("\nPipeline completed successfully!")

    else:

        print("\nPipeline cancelled.")


if __name__ == "__main__":
    main()