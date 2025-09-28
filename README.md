# Bat Password Manager

A simple command-line tool to generate strong passwords and analyze their strength. It also includes a basic OPSEC guide and optional password security insights.

---

## Features

- Generate random passwords with letters, digits, and symbols.
- Choose from multiple generated passwords.
- Save passwords to a file.
- Analyze selected password:
  - Length
  - Character classes used
  - Estimated charset size
  - Entropy (per character and total)
  - Approximate number of combinations
  - Estimated time to brute-force under various scenarios
- Optional OPSEC guidance to help protect your accounts.
- Displays contents of `bat.txt` for optional instructions or info.

---

## Requirements

- Python 3.7+
- Standard library modules (`os`, `platform`, `time`, `secrets`, `string`, `math`)

---
## Notes
- Please always save your password files and do daily backups
- I used AI to translate code and ident it to english
- Enjoy :) 
## Installation

1. Clone the repository:

```bash
git clone https://github.com/jcosta-oaz/bat-manager.git
cd bat-manager
python bat-manager.py
