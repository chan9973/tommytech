# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| 0.1.x   | ✅ Yes    |
| < 0.1   | ❌ No     |

## Reporting a Vulnerability

We take security vulnerabilities seriously. Please do **not** open a public
GitHub issue if you discover a security vulnerability.

### Responsible Disclosure

1. **Report immediately** via one of these channels:
   - **Email:** security@tommytech.com
   - **GitHub Security Advisory:** https://github.com/tommytech/tommytech/security/advisories
   - **HackerOne:** https://hackerone.com/tommytech

2. **Include** as much detail as possible:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested remediation (if any)

3. **Do not** exploit or publicly disclose the vulnerability until a patch
   has been released.

### Response Timeline

| Step                    | SLA                          |
| ----------------------- | ---------------------------- |
| Acknowledgment          | Within 24 hours              |
| Triage & Initial Review | Within 48 hours              |
| Patch Development       | 1–2 weeks (severity depends) |
| Disclosure              | After patch release          |

### Vulnerability Classification

| Severity | Impact               | Response Time |
| -------- | -------------------- | ------------- |
| Critical | RCE, data breach     | < 4 hours     |
| High     | Privilege escalation | < 24 hours    |
| Medium   | Limited data leak    | < 1 week      |
| Low      | Info disclosure      | < 2 weeks     |

### Bug Bounty

We may offer rewards for valid security reports. See our
[HackerOne program](https://hackerone.com/tommytech) for details.

---

## Security Practices

### Secrets Management

- Secrets are stored in GitHub Encrypted Secrets, **never** in code.
- Secret scanning is enforced via GitHub's `secret-scanning` and
  `push-protection` features.
- A `.gitleaks.toml` configuration is provided for pre-commit scanning.

### Dependency Security

- Dependabot automatically submits PRs for vulnerable dependencies.
- CodeQL performs static analysis on every pull request.
- `npm audit` and `pip-audit` run in CI.

### Access Control

- Branch protection is enforced on `main` and `develop`.
- Only repository administrators can force-push.
- All PRs require 1+ approvals from CODEOWNERS.
