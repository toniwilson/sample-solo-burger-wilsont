# CLAUDE.md

## Project

Flask Login Exercise — a simple login page used to practice the Sacred Workflow (Issue → Branch → Draft PR → Code/Test → Finish PR → Review → Merge). This is a learning exercise, not a production application. The student is building one user story through the full development workflow using Claude Code as a pair programmer.

## Context

This is a CSC 289 Programming Capstone exercise at Wake Technical Community College. The student may be relatively new to Flask, Git workflows, and working with AI coding assistants. Prioritize clarity over cleverness. When proposing code, explain what it does and why. When the student asks you to build something, propose a plan first and wait for approval before generating code.

**Do not write all the code at once.** Work in small pieces: one route, one template, one feature at a time. After each piece, prompt the student to test it before moving on.

## Tech Stack

- Python 3.x
- Flask (see requirements.txt for pinned version)
- Jinja2 templates (in `templates/` directory, extending `base.html`)
- Flask built-in sessions (cookie-based, signed with `secret_key`)
- No database — hardcoded credentials for this exercise
- No external authentication libraries
- Static files in `static/` directory (CSS only, no JS required)

## Architecture

```
phase1-flask-login/
├── app.py                    # All routes live here (single file)
├── templates/
│   ├── base.html             # Base template with HTML boilerplate
│   ├── login.html            # Login form (extends base.html)
│   └── dashboard.html        # Dashboard page (extends base.html)
├── static/
│   └── style.css             # Optional styling
├── requirements.txt
├── README.md
├── CLAUDE.md                 # This file
└── .github/
    └── pull_request_template.md
```

This is a single-file Flask application. All routes are defined in `app.py`. Templates use Jinja2 inheritance from `base.html`. There is no ORM, no database, no migration system, no blueprint structure. Keep it simple.

## Current Task

**Issue #1: Basic Login Page**

User story: As a user, I want to log in with a username and password so that I can access my account dashboard.

Acceptance criteria:

1. A `/login` route exists and renders a form with fields for username and password.
2. Submitting valid credentials redirects to `/dashboard`.
3. Submitting invalid credentials re-renders the login page with a visible error message.
4. The `/dashboard` page displays "Welcome, [username]".
5. The `/dashboard` page redirects to `/login` if the user is not authenticated (no active session).
6. A logout link or button on `/dashboard` clears the session and returns to `/login`.

Hardcoded credentials for this exercise:

```python
# These are intentionally simple. This is a workflow exercise, not a security exercise.
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"
```

## Conventions

### Python / Flask
- Follow PEP 8 style.
- Routes are decorated with `@app.route()` and define both allowed methods explicitly when needed (e.g., `methods=['GET', 'POST']`).
- Use `flask.session` for authentication state. Set `session['username']` on successful login, check for it on protected routes, clear it on logout.
- Use `flask.redirect` and `flask.url_for` for navigation between routes (not hardcoded URL strings).
- Use `flask.flash` for error messages if the student wants, but a simple template variable (`error`) passed via `render_template` is also fine.
- Keep it in one file. Do not suggest splitting into blueprints, factories, or separate modules.

### Templates
- All templates extend `base.html` using `{% extends "base.html" %}` and `{% block content %}`.
- Use `{{ url_for('static', filename='style.css') }}` for static file references.
- Use `{{ url_for('login') }}` style references for form actions and links (not hardcoded paths).
- Minimal HTML is fine. The exercise is about workflow, not frontend polish.

### Git
- Commit messages follow: `type(scope): subject` — e.g., `feat(auth): add login route and template`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Reference the issue in commit body: `Refs #1`
- The student should commit after each working piece, not all at once at the end.

## Recommended Build Order

When the student asks to implement Issue #1, suggest this sequence:

1. **Login template + GET route** — Create `login.html` with a form and the `/login` GET route that renders it. Test: visit `/login`, see the form.

2. **Login POST handler** — Add POST handling to `/login`. Check credentials against hardcoded values. On success, set `session['username']` and redirect to `/dashboard`. On failure, re-render with an error message. Test: submit wrong creds (see error), submit right creds (redirect).

3. **Dashboard route + template** — Create `dashboard.html` and the `/dashboard` route. Display "Welcome, [username]" from session. If no session, redirect to `/login`. Test: after login, see dashboard. In a new tab, go directly to `/dashboard` without logging in — should redirect.

4. **Logout** — Add a `/logout` route that clears the session and redirects to `/login`. Add a logout link to the dashboard template. Test: click logout, verify session is cleared, verify `/dashboard` is no longer accessible.

5. **Final check** — Walk through all six acceptance criteria. Fix anything that doesn't pass.

After each piece, remind the student to test locally and commit before moving on.

## How to Run

```bash
# Set up virtual environment (first time)
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

The app runs at `http://localhost:5000` with debug mode enabled.

## How to Test

Manual testing against the six acceptance criteria:

| # | Test | Expected Result |
|---|------|-----------------|
| 1 | Visit `/login` | Form with username and password fields renders |
| 2 | Submit form with `admin` / `password123` | Redirect to `/dashboard` |
| 3 | Submit form with wrong credentials | Login page re-renders with error message |
| 4 | After login, check `/dashboard` | Shows "Welcome, admin" |
| 5 | Open new incognito window, visit `/dashboard` directly | Redirects to `/login` |
| 6 | Click logout on dashboard, then try `/dashboard` again | Redirects to `/login` |

## Common Student Mistakes

If the student runs into these, help them understand the fix rather than just providing it:

- **Missing `methods=['GET', 'POST']`** on the login route — form submission silently sends a GET, page just reloads with no error.
- **Forgetting `app.secret_key`** — sessions won't work without it. Flask raises a RuntimeError.
- **Using `session['username']` instead of `session.get('username')`** on the dashboard — crashes with KeyError if no session exists. Use `.get()` to safely check.
- **Hardcoding URLs in templates** instead of using `url_for()` — works until a route name changes, then breaks silently.
- **Not redirecting after POST** — submitting the login form without a redirect means refreshing the page resubmits the form (the POST/redirect/GET pattern).

## Important Guidance for Claude Code

- **Explain, don't just generate.** When you write code, briefly explain what each part does. The student needs to understand their own code — they will be asked comprehension questions.
- **Pause between pieces.** After generating a route or template, ask "Does this make sense? Want to test it before we move on?" Do not generate the entire application in one response.
- **Keep it simple.** Do not introduce concepts beyond what the task requires. No decorators for auth (a simple `if` check is fine), no database, no Flask-Login, no WTForms, no application factories, no blueprints. One file, a few routes, basic templates.
- **When the student is stuck**, help them debug rather than rewriting their code. Ask what they expected to happen vs. what actually happened. Guide them to the fix.
- **If the student asks to skip ahead** or generate everything at once, gently redirect: "Let's build this one piece at a time so we can test as we go. Which piece should we start with?"