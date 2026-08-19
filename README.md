# TommyTech

> Technical infrastructure for TommyTech — initialized by the CTO agent.

## Overview

TommyTech is a multi-service technology platform. This repository houses the
canonical infrastructure: repository conventions, CI/CD pipelines, security
protocols, and shared tooling.

## Repository Structure

```
tommytech/
├── src/                     # Application source code
├── tests/                   # Automated test suites
├── docs/                    # Technical documentation
│   ├── architecture/        # Architecture decision records (ADRs)
│   └── runbooks/            # Operational runbooks
├── scripts/                 # Build, deploy, and maintenance scripts
├── .github/                 # GitHub-specific config
│   ├── workflows/           # CI/CD workflows
│   ├── ISSUE_TEMPLATE/      # Issue templates
│   ├── dependabot.yml       # Automated dependency updates
│   ├── dependabot-security/ # Security-specific dependency updates
│   ├── CODEOWNERS           # Ownership rules
│   └── SECURITY.md          # Security policy
├── .gitignore
├── .editorconfig
├── CONTRIBUTING.md
└── cto_decisions.md         # CTO infrastructure decisions log
```

## Quick Start

```bash
# Clone and install
git clone <repo-url>
cd tommytech

# Python services
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Node.js tooling
npm install
```

## Infrastructure Decisions

All infrastructure decisions are documented in [`cto_decisions.md`](./cto_decisions.md).
