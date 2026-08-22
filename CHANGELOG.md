# Version 0.1.0

## Added

- Initial repository structure
- CI pipeline (`.github/workflows/ci.yml`)
- CD pipeline (`.github/workflows/cd.yml`)
- Security scanning pipeline (`.github/workflows/security.yml`)
- Pre-commit hooks (`pre-commit` + `bandit` + `gitleaks` + `ruff` + `eslint`)
- Docker multi-stage production image (`Dockerfile`)
- Security policy (`SECURITY.md` + `CODEOWNERS`)
- Dependabot automation (`.github/dependabot.yml`)
- Secret scanning configuration (`.gitleaks.toml`)
- Repository settings (`.github/settings.yml`)
- Environment template (`.env.example`)
- Documentation (`docs/`)

## Security

- CodeQL static analysis on every PR
- GitLeaks secret scanning on every commit
- Trivy filesystem vulnerability scanning in CI
- pip-audit + npm audit in CI
- Branch protection: required reviews + CI + linear history
