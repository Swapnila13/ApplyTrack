# ApplyTrack – Smart Job Application Tracker

ApplyTrack is a web application that helps job seekers organize and manage their job applications in one place. Users can record company details, track application statuses, add notes, and manage follow-up dates through a simple dashboard.

## Features

- **Application Management:** Add, view, edit, and delete job applications.
- **Status Tracking:** Track applications through Applied, Online Assessment, Interview, Selected, and Rejected statuses.
- **Follow-up Reminders:** Identify follow-ups that are overdue, due today, or upcoming.
- **Input Validation:** Validate required fields, dates, and application statuses.
- **REST API:** Manage job application records through HTTP requests.
- **Data Storage:** Store application records using SQLite.
- **Automated Testing:** Test application functionality and input validation using Python's `unittest` framework.
- **User-Friendly Dashboard:** Manage applications through a web interface built with HTML, CSS, and JavaScript.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **API:** REST API
- **Testing:** Python `unittest`
- **Deployment:** Planned

## Project Structure

```text
ApplyTrack/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── add_application.html
│   ├── edit_application.html
│   ├── 404.html
│   └── 500.html
└── tests/
    └── test_app.py
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible newer version
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Swapnila13/ApplyTrack.git
cd ApplyTrack
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local address displayed in your terminal, typically:

http://127.0.0.1:5000

## REST API

ApplyTrack provides API endpoints for managing job applications.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/applications` | Retrieve applications |
| POST | `/api/applications` | Create an application |
| PATCH | `/api/applications/<id>` | Update an application |
| DELETE | `/api/applications/<id>` | Delete an application |

The API supports input validation and appropriate error responses for invalid data and nonexistent application records.

## Running Automated Tests

Run the test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The project currently has **10 automated tests passing** in the local development environment.

## Learning Outcomes

Through this project, I practised:

- Building a web application using Flask.
- Performing CRUD operations with SQLite.
- Designing and testing REST API endpoints.
- Validating user input and handling errors.
- Writing automated tests.
- Using Git and GitHub for version control.

## Future Improvements

- Deploy the application online.
- Add secure user authentication and individual user accounts.
- Configure persistent cloud database storage.
- Add job search analytics and application statistics.
- Improve follow-up notifications.

## Author

**Swapnila**

GitHub: [Swapnila13](https://github.com/Swapnila13)

