# Low-Code Project Restart

A small Flask web page that displays “Hello from Suzanne.”

## Routes

- `/` displays the “Hello from Suzanne” home page.
- `/about` presents the idea behind a delivery-driver web application:
  - Drivers submit their availability and preferred locations; managers assign
    shifts, resolve scheduling conflicts, and approve shift-cover requests.
  - Drivers scan delivery dockets to extract addresses, Eircodes, and contact
    details, open a preferred navigation app, and track deliveries, payment
    status, fees, and earnings.
  - Administrators, managers, and drivers have separate dashboards and
    role-based permissions.
  - The goal is to use AI-assisted development and low-code tools to quickly
    build an MVP that reduces administration and improves delivery operations.
- `/contact` provides a name, email, and message form. The server rejects
  missing fields and invalid email addresses, and displays a confirmation for
  valid submissions. Messages are not stored.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
.venv/bin/python app.py
```

Open <http://127.0.0.1:5000>.
