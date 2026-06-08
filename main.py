from services.company_finder import find_similar_companies
from services.contact_finder import find_contacts
from services.email_finder import find_email
from services.mailer import send_email

import pandas as pd
import os


def main():

    print("\n===== AUTOMATED OUTREACH PIPELINE =====\n")

    seed_domain = input("Enter company domain: ").strip()

    # STAGE 1 - COMPANY DISCOVERY

    print("\n[STAGE 1] Company Discovery")

    try:
        companies = find_similar_companies(seed_domain)

        if not companies:
            print("No companies found.")
            return

        print(f"Found {len(companies)} companies")

    except Exception as e:
        print(f"Company discovery failed: {e}")
        return

    # STAGE 2 - CONTACT DISCOVERY

    print("\n[STAGE 2] Contact Discovery")

    all_contacts = []

    for company in companies:

        try:

            contacts = find_contacts(company)

            for contact in contacts:

                email = find_email(contact)

                contact["company"] = company
                contact["email"] = email

                all_contacts.append(contact)

        except Exception as e:

            print(
                f"Failed processing {company}: {e}"
            )

            continue

    print(f"Found {len(all_contacts)} contacts")

    # STAGE 3 - DEDUPLICATION

    print("\n[STAGE 3] Deduplication")

    seen = set()
    unique_contacts = []

    for contact in all_contacts:

        if contact["email"] not in seen:

            seen.add(contact["email"])
            unique_contacts.append(contact)

    all_contacts = unique_contacts

    print(f"Unique contacts: {len(all_contacts)}")

    # STAGE 4 - EXPORT RESULTS

    print("\n[STAGE 4] Export Results")

    os.makedirs("outputs", exist_ok=True)

    contacts_df = pd.DataFrame(all_contacts)

    companies_df = pd.DataFrame(
        {"company": companies}
    )

    emails_df = pd.DataFrame(
        {
            "email": [
                contact["email"]
                for contact in all_contacts
            ]
        }
    )

    companies_df.to_csv(
        "outputs/companies.csv",
        index=False
    )

    contacts_df.to_csv(
        "outputs/contacts.csv",
        index=False
    )

    emails_df.to_csv(
        "outputs/emails.csv",
        index=False
    )

    print("Saved:")
    print("  ✓ outputs/companies.csv")
    print("  ✓ outputs/contacts.csv")
    print("  ✓ outputs/emails.csv")

    # SUMMARY

    print("\n===== SUMMARY =====")

    print(f"Companies Found : {len(companies)}")
    print(f"Contacts Found  : {len(all_contacts)}")
    print(f"Emails Found    : {len(all_contacts)}")

    # CONTACT PREVIEW

    if not contacts_df.empty:

        print("\n===== CONTACT PREVIEW =====\n")

        print(
            contacts_df[
                [
                    "name",
                    "title",
                    "company",
                    "email"
                ]
            ]
        )

    # SAFETY CHECKPOINT

    confirm = input(
        "\nProceed with email sending? (y/n): "
    )

    if confirm.lower() != "y":

        print("\nPipeline cancelled.")
        return

    # STAGE 5 - OUTREACH

    print("\n[STAGE 5] Outreach")

    for contact in all_contacts:

        try:

            send_email(
                contact,
                contact["email"]
            )

        except Exception as e:

            print(
                f"Failed sending email to "
                f"{contact['email']}: {e}"
            )

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()