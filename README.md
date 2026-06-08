# Automated Outreach Pipeline

## Overview

Automated Outreach Pipeline is a Python-based cold outreach automation system that discovers companies, generates contacts, resolves email addresses, exports prospect data, and sends personalized outreach emails through the Brevo Email API.

The project was developed as part of an SDE Internship assignment and demonstrates a complete end-to-end outreach workflow.

---

## Features

* Company Discovery
* Contact Discovery
* Email Resolution
* Contact Deduplication
* CSV Export
* Personalized Email Generation
* Safety Checkpoint Before Sending
* Logging
* Brevo Email API Integration
* Modular Architecture

---

## Project Structure

```text
automated-outreach-pipeline/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── company_finder.py
│   ├── contact_finder.py
│   ├── email_finder.py
│   ├── mailer.py
│   └── brevo.py
│
├── utils/
│   └── logger.py
│
├── templates/
│   └── outreach.txt
│
├── data/
│   └── companies.csv
│
├── outputs/
│   ├── companies.csv
│   ├── contacts.csv
│   └── emails.csv
│
└── tests/
    └── test_company_finder.py
```

---

## Workflow

```text
Input Domain
      │
      ▼
Company Discovery
      │
      ▼
Contact Discovery
      │
      ▼
Email Resolution
      │
      ▼
Deduplication
      │
      ▼
CSV Export
      │
      ▼
Safety Checkpoint
      │
      ▼
Brevo Email API
      │
      ▼
Email Delivery
```

---

## Technologies Used

* Python
* Pandas
* Requests
* Python Dotenv
* Rich
* Git
* GitHub
* Brevo API

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd automated-outreach-pipeline
```

Create virtual environment:

```bash
python -m venv env
```

Activate environment:

```bash
env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
BREVO_API_KEY=your_brevo_api_key
```

---

## Running the Project

```bash
python main.py
```

Example Input:

```text
openai.com
```

---

## Output Files

The pipeline generates:

```text
outputs/companies.csv
outputs/contacts.csv
outputs/emails.csv
```

---

## Screenshots

### Pipeline Execution

Add: `assets/pipeline-run.png`

### Contact Discovery

Add: `assets/contacts-preview.png`

### CSV Export

Add: `assets/csv-output.png`

### Brevo API Success

Add: `assets/brevo-success.png`

### Email Received

Add: `assets/email-received.png`

---

## Future Improvements

* Domain Verification
* Custom Business Email Sender
* Real Company Discovery APIs
* Real Contact Discovery APIs
* Batch Scheduling
* Analytics Dashboard
* Campaign Tracking

---

## Author

Girish Gowda

GitHub: https://github.com/<your-username>
