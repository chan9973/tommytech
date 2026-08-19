# Contributing to TommyTech

## Development Workflow

1. **Fork** the repository and create a feature branch.
2. **Write tests** for any new functionality.
3. **Run the full CI check** locally before pushing:
   ```bash
   npm run ci
   ```
4. **Open a Pull Request** with a clear description.

## Branch Strategy

| Branch       | Purpose                              |
|-------------|--------------------------------------|
| `main`       | Production-ready code                |
| `develop`    | Integration branch for features     |
| `feature/*`  | New features                          |
| `fix/*`      | Bug fixes                             |
| `release/*`  | Release preparation                   |
| `hotfix/*`   | Emergency production fixes            |

## Code Review

All pull requests require **at least one approval** from a code owner
(see `.github/CODEOWNERS`). Reviews must verify:

- ✅ Tests pass
- ✅ Code follows style guidelines
- ✅ Security implications reviewed
- ✅ No secrets or sensitive data introduced

## Security Vulnerabilities

See [SECURITY.md](.github/SECURITY.md) for reporting instructions.
