# Contributing

Even though this is a solo project, I follow a team-style workflow.

## Workflow

1. Create an issue (what and why)
2. Create a branch from `main`
3. Commit in small steps
4. Open a pull request and link the issue (`closes #123`)
5. Make sure CI passes
6. Review your own changes, then merge
7. The issue closes automatically

## Branches

Work on short-lived branches and merge them into `main` through a pull request.

| Branch | Purpose |
|:--|:--|
| `feature/*` | New features |
| `fix/*` | Bug fixes |
| `docs/*` | Documentation |
| `chore/*` | Tooling and cleanup |

Example: `feature/record-history`, `fix/empty-time-input`

## Commit messages (Conventional Commits)

Format: `<type>(scope): summary`

| Type | Use for | Example |
|:--|:--|:--|
| `feat` | A new feature | `feat(goal): add share link for weekly goal` |
| `fix` | A bug fix | `fix(record): handle empty time input` |
| `docs` | Documentation | `docs: add architecture notes` |
| `refactor` | Code change without behavior change | `refactor(goal): extract weekly total helper` |
| `test` | Adding or updating tests | `test(utils): cover weekly_total` |
| `chore` | Tooling and cleanup | `chore: add root .gitignore` |
| `ci` | CI configuration | `ci: add ruff lint job` |

Avoid messages like `fix`, `update` or `aaa`.

To use the commit message template:

```bash
git config commit.template .gitmessage
```

## Pull requests

- The PR title must follow the same format. The `pr-title` job in CI checks it.
- With squash merge, the PR title becomes the commit message.

Before opening a PR:

- [ ] CI passes
- [ ] I reviewed my own changes
- [ ] I updated the README or docs if needed
- [ ] No secrets are included (`.env`, Firebase keys)