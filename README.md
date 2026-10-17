# ApplyTrack - Smart Job Application Tracker

A beginner-friendly Flask web app for tracking job applications, recruitment stages, and follow-up dates. It stores records in SQLite and provides a small REST API for creating, reading, updating, and deleting applications.

## Features

- Add, edit, view, and delete applications, with a confirmation before deletion.
- Dashboard totals calculated from database records.
- Search by company or role and filter by application status.
- Follow-up labels: **Overdue**, **Due today**, and **Upcoming**. Selected and Rejected applications are excluded from reminders.
- JSON REST API with validation and useful HTTP status codes.
- Responsive HTML/CSS interface and automated tests using a separate temporary database.

> Follow-ups are calculated when the dashboard or API is requested. This project does not send emails and does not run background or scheduled jobs.

## Technologies

- Python 3.10 or newer
- Flask 3.x
- SQLite (included with Python)
- HTML, CSS, and a small amount of JavaScript
- Python `unittest` and Flask's test client

## Project structure

```text
smart-job-tracker/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── add_application.html
│   ├── edit_application.html
│   ├── 404.html
│   └── 500.html
├── static/
│   ├── css/style.css
│   └── js/script.js
└── tests/test_app.py
```

## Installation and run

Open a terminal in the project folder.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

If PowerShell blocks virtual-environment activation, use Command Prompt instead:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser. Stop the development server with `Ctrl+C`. Flask debug mode is enabled for local development; do not use this development server as a public production deployment.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

## Run automated tests

With the virtual environment activated and dependencies installed:

```bash
python -m unittest discover -s tests -v
```

Tests create a temporary SQLite database for each test and remove it afterward; they do not use the normal `job_tracker.db` file.

## Database

On startup, the app automatically creates `job_tracker.db` in the project folder and the `applications` table if they do not exist. The database contains company, role, application date, status, optional URL, notes, follow-up date, and creation timestamp. SQLite queries use placeholders for values. The local database file is ignored by Git so your personal application data is not committed.

To use a different database file, set `JOB_TRACKER_DATABASE` before starting the app. For example in PowerShell:

```powershell
$env:JOB_TRACKER_DATABASE = "D:\data\job_tracker.db"
python app.py
```

## REST API

All API request bodies must use `Content-Type: application/json`. Dates must be strings in `YYYY-MM-DD` format. Status must be one of `Applied`, `Online Assessment`, `Interview`, `Selected`, or `Rejected`.

| Method | Endpoint | Purpose | Success |
|---|---|---|---|
| GET | `/api/applications` | List applications | `200 OK` |
| GET | `/api/applications/<id>` | Retrieve one application | `200 OK` |
| POST | `/api/applications` | Create an application | `201 Created` |
| PATCH | `/api/applications/<id>` | Update supplied fields | `200 OK` |
| DELETE | `/api/applications/<id>` | Delete an application | `200 OK` |

Missing records return `404`; validation or malformed JSON errors return `400`; an incorrect content type returns `415`. API error responses use JSON such as `{"error":"Application not found."}`.

### Create example

```bash
curl -X POST http://127.0.0.1:5000/api/applications \
  -H "Content-Type: application/json" \
  -d '{"company_name":"Acme Technologies","job_role":"Software Engineer","application_date":"2026-10-17","status":"Applied","job_url":"https://example.com/jobs/123","notes":"Campus placement","follow_up_date":"2026-10-24"}'
```

Windows Command Prompt users can run the command on one line, or use PowerShell's `curl.exe` with the JSON body quoted appropriately.

### List and retrieve examples

```bash
curl http://127.0.0.1:5000/api/applications
curl http://127.0.0.1:5000/api/applications/1
```

### Update example

```bash
curl -X PATCH http://127.0.0.1:5000/api/applications/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"Interview","notes":"Technical interview scheduled"}'
```

### Delete example

```bash
curl -X DELETE http://127.0.0.1:5000/api/applications/1
```

### Postman

1. Start the app and create a request to `http://127.0.0.1:5000/api/applications`.
2. Select the required HTTP method and enter the endpoint.
3. For POST/PATCH, choose **Body → raw → JSON**, then paste one of the examples above.
4. Click **Send** and inspect the status code and JSON response.


## Limitations and possible future improvements

- This is a local, single-user portfolio project; it has no authentication or multi-user access control.
- Follow-up reminders appear when pages/API responses are requested; there are no email notifications or background scheduler.
- The app uses SQLite and is intended for local/demo use, not high-volume concurrent use.
- Possible improvements: pagination, CSV export, automated email reminders, authentication, and deployment with production security settings.
