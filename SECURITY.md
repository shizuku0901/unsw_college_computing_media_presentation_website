# Security Policy

## Reporting a vulnerability

If you find a security issue, please do not open a public issue.
Report it privately through the repository's **Security** tab → **Report a vulnerability**.

## Handling of secrets

- `.env` files and Firebase service account keys are never committed (see `.gitignore`). A sample is provided in `.env.example`.
- If a secret is committed by mistake, **revoke or rotate it first**, then remove it from the Git history.