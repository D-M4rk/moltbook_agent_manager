# Contributing to Moltbook Agent Manager

Thanks for your interest in contributing!

## How to Contribute

### Reporting Bugs

1. Check if the issue already exists
2. Include steps to reproduce
3. Include your OS and Python version
4. Use the Diagnostics tab > "Copy Debug Info" for system details

### Feature Requests

Open an issue describing:
- What you want to add
- Why it would be useful
- Any implementation ideas

### Pull Requests

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Test the app manually
5. Commit with clear messages
6. Push and open a PR

## Development Setup

```bash
git clone https://github.com/D-M4rk/moltbook_agent_manager.git
cd moltbook_agent_manager
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
pip install keyring cryptography
python moltbook_agent_manager.py
```

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Use `logger.debug/info/warning/error` instead of `print()`
- Use parameterized SQL queries (never string concatenation)
- Handle exceptions specifically (not bare `except:`)

## Project Structure

```
moltbook_agent_manager/
├── moltbook_agent_manager.py  # Main application (single file)
├── requirements.txt           # Dependencies
├── pyproject.toml            # Package config
├── README.md                 # Documentation
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # This file
├── LICENSE                   # MIT License
└── .gitignore               # Git ignore rules
```

## Testing

Before submitting a PR:
1. Run the app and test your changes
2. Check all tabs work correctly
3. Test edge cases (empty states, errors)
4. Check the logs for unexpected errors

## Questions?

Open an issue with the "question" label.
