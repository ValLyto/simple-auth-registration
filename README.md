# Simple Auth Registration System

A command-line Python application for user registration and authentication 
with persistent data storage.

## Features

- **New user registration** — auto-generates a username based on first 
name, last name, and date of birth
- **User login** — password validation with a 3-attempt lockout
- **Password validation** — enforces complexity rules (uppercase, 
lowercase, digit, 6–12 chars)
- **Persistent storage** — user data is saved to a local `.pkl` file 
between sessions

## Requirements

- Python 3.x
- No external libraries required (uses `re` and `pickle` from the standard 
library)

## Getting Started

```bash
git clone https://github.com/your-username/simple-auth-registration.git
cd simple-auth-registration
python simple-auth-registration.py
```

## Usage

On launch, a menu is displayed:

```
Welcome to the System
1. Existing customers - Login
2. New customers - Register
0. Exit
```

### Registering a New User

Select option `2` and provide:
- First name
- Last name
- Date of birth (DD/MM/YYYY)
- Password

A username is automatically generated in the format 
`[first3][last3][year]` (e.g. `johsmi2001`).

### Logging In

Select option `1`, enter your username and password. After 3 failed 
attempts, access is denied.

## Password Requirements

| Rule | Detail |
|------|--------|
| Length | 6–12 characters |
| Uppercase | At least 1 uppercase letter |
| Lowercase | At least 1 lowercase letter |
| Digit | At least 1 number |
| Allowed characters | Letters and digits only |

## Data Storage

User credentials are stored locally in `user_data.pkl` using Python's 
`pickle` module.

> ⚠️ **Note:** Passwords are stored in plain text. This project is 
intended for educational purposes only and is **not suitable for 
production use**.

## Project Structure

```
simple-auth-registration/
├── simple-auth-registration.py   # Main application
├── user_data.pkl                 # Auto-generated user data file 
(gitignored)
└── README.md
```

## .gitignore Recommendation

```
user_data.pkl
__pycache__/
*.pyc
```

## License

This project is for educational use only.

