# Adaptive Learning Intelligence System (ALIS)

ALIS is a Streamlit-based adaptive learning dashboard designed to help students record study topics, scores, revision counts, and monitor a simple retention score.

## Features

- User registration and login
- SHA-256 password hashing
- Session-based login state using Streamlit
- Student profile fields: name and class
- Subject-wise topic tracking
- 16 school subjects
- Score entry from 0–100%
- Per-user CSV data storage
- Retention calculation
- Revision-status alerts
- Dashboard metrics
- Memory/retention trend chart
- Subject performance chart
- Logout functionality

## System Workflow

```text
Register / Login
       ↓
Add Subject + Topic + Score
       ↓
CSV Storage
       ↓
Retention Calculation
       ↓
Revision Status
       ↓
Alerts + Dashboard + Recommendations
```

## Retention Formula

The current implementation uses:

```text
Retention = (Score × 0.8) + (Revision Count × 5)
```

The value is clipped to the range 0–100%.

### Status thresholds

| Retention | Status |
|---:|---|
| < 40 | 🔴 Revise Now |
| 40–69.99 | 🟡 Revise Soon |
| ≥ 70 | 🟢 Good |

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- hashlib
- CSV

## Run Locally

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

The application creates `users.csv` and user-specific `<username>_data.csv` files in the working directory.

## Project Scope

This repository documents the supplied ALIS implementation. The current retention calculation is a simple rule-based model; it is not a validated cognitive-science forgetting-curve model.

## Security Note

This is an academic/portfolio prototype. Although passwords are hashed with SHA-256, the current application stores PINs directly in CSV and uses local CSV files for authentication/data storage. A production version should use a database, salted password hashing such as Argon2/bcrypt, secure secret handling, validation, and proper access control.
