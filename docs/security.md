# Security Architecture

## Overview

TommyTech implements a defense-in-depth security model with automated scanning
at every stage of the development lifecycle.

## Security Controls

### 1. Secret Scanning
- **Tool:** GitLeaks
- **Coverage:** All commits (pre-commit hook + CI pipeline)
- **Config:** `.gitleaks.toml`
- **Patterns monitored:**
  - Private API keys (`ttk_` prefix)
  - AWS credentials
  - GitHub tokens
  - Private keys
  - Generic API key/password assignments

### 2. Static Application Security Testing (SAST)
- **CodeQL:** Multi-language static analysis (Python, JavaScript/TypeScript)
  - Runs on every PR and push to `main`/`develop`
  - Extended security queries enabled
  - Results uploaded to GitHub Security tab
- **ESLint Security Plugin:** Runtime vulnerability rules
- **Bandit:** Python security linting (pre-commit + CI)

### 3. Dependency Vulnerability Scanning
- **pip-audit:** Scans Python dependencies for CVEs
- **npm audit:** Scans Node.js dependencies for CVEs
- **Dependabot:** Automated dependency updates with weekly cadence
- **Severity threshold:** High and Critical trigger alerts

### 4. Container Security
- **Trivy:** Filesystem vulnerability scanning (CI pipeline)
- **Multi-stage Dockerfile:** Minimal production image
- **Non-root user:** Container runs as `appuser`
- **No new capabilities:** Docker hardening flags
- **SBOM generation:** Software bill of materials for each build

### 5. Branch Protection
- `main` branch: requires 1 approval + CI + Security checks
- `develop` branch: requires 1 approval + CI checks
- `required_linear_history`: enforced on all branches
- `allow_force_pushes`: disabled
- `enforce_admins`: enabled on `main`

## Incident Response

Contact: `security@tommytech.com`

See `.github/SECURITY.md` for the full reporting process.
