# Phase 1: Flask Login Exercise

A starter repo for the Solo Burger exercise — your first user story through the Sacred Workflow.

## What This Is

A minimal Flask application that returns "Hello World." Your job is to implement a login page with session-based authentication, following the instructions in `instructions/solo-burger-instructions.md`.

## Getting Started

```bash
# Clone your copy of the repo
git clone <your-repo-url>
cd phase1-flask-login

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser. You should see "Hello, World! Your Flask app is running."

If you see that message, you're ready to start. If not, check the Troubleshooting section in the instructions.

## Project Structure

```
├── app.py                    # Flask app (all routes live here)
├── templates/
│   └── base.html             # Base template with HTML boilerplate
├── static/
│   └── style.css             # Your styles (empty to start)
├── requirements.txt          # Flask dependency
├── CLAUDE.md                 # Project context for Claude Code
├── instructions/
│   └── solo-burger-instructions.md  # Full assignment instructions
├── .github/
│   └── pull_request_template.md     # PR template
└── README.md                 # This file
```

## Your Task

**Issue #1: Basic Login Page**

Implement a login page with these acceptance criteria:

1. `/login` route renders a form with username and password fields
2. Valid credentials redirect to `/dashboard`
3. Invalid credentials show an error message on the login page
4. `/dashboard` displays "Welcome, [username]"
5. `/dashboard` redirects to `/login` if not authenticated
6. Logout clears session and returns to `/login`

Read `instructions/solo-burger-instructions.md` for the full walkthrough.
