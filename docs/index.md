# TommyTech Technical Documentation

Welcome to the TommyTech technical documentation hub.

## Table of Contents

- [Architecture Overview](architecture.md)
- [Security Protocols](security.md)
- [CI/CD Pipeline](ci-cd.md)
- [Deployment Guide](deployment.md)
- [Environment Variables](environments.md)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/tommy/tommytech.git
cd tommytech

# Set up Python virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
npm test  # Node.js tests
pytest tests/  # Python tests
```

## Project Structure

```
tommytech/
├── .github/              # GitHub configs
│   ├── workflows/        # CI/CD pipeline definitions
│   ├── ISSUE_TEMPLATE/   # Issue templates
│   ├── CODEOWNERS        # Code ownership rules
│   ├── SECURITY.md       # Security policy
│   └── settings.yml      # Repository settings
├── src/                  # Application source code
│   └── main.py           # FastAPI application entry point
├── tests/                # Test suite
├── docs/                 # Documentation
├── scripts/              # Utility scripts
├── Dockerfile            # Production container image
├── docker-compose.yml    # Local development stack
├── requirements.txt      # Python dependencies
├── requirements-dev.txt  # Development dependencies
├── pyproject.toml        # Python project config
├── package.json          # Node.js tooling config
├── .eslintrc.json        # ESLint configuration
├── .prettierrc.json      # Prettier configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── .gitleaks.toml        # Secret scanning config
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
├── .dockerignore         # Docker ignore rules
├── .editorconfig         # Editor configuration
└── cto_decisions.md      # CTO technical decisions log
```
