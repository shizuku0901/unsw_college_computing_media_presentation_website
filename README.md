# Fitness App

[![CI](https://github.com/shizuku0901/unsw_college_computing_media_presentation_website/actions/workflows/ci.yml/badge.svg)](https://github.com/shizuku0901/unsw_college_computing_media_presentation_website/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-Flask-3776AB?logo=python&logoColor=white)

> A Flask + Firebase web app for logging workouts and tracking weekly goals, built for the media presentation in UNSW College FNDN304 *Computing for Business* (2026).

**Live demo:** <https://unsw-college-computing-media.onrender.com>
(The demo may be hosted on a free tier, so the first load can take a while.)

<!-- ![Screenshot](docs/images/demo.png) -->

## Overview

The course only required AI-generated mockup images and an idea presentation.
I went further and implemented the working website myself.

## Features

- **Home**: member information and today's total exercise time
- **Tips**: exercise tips loaded from Firestore
- **Facility**: finds sports facilities (gyms, pools, parks, etc.) within 2 km using the browser's location and the OpenStreetMap Overpass API
- **Record**: log an activity (Running, Swimming, Cycling, Yoga) and its duration
- **Goal**: set a weekly target in minutes, see progress, and create a read-only share link
- **Accounts**: register and log in

## Tech stack

| Category | Technology |
|:--|:--|
| Language | Python, JavaScript |
| Framework | Flask (application factory + blueprints), Jinja2 |
| UI | Tailwind CSS (CDN) |
| Database | Cloud Firestore (firebase-admin) |
| External data | OpenStreetMap Overpass API |
| Server / Hosting | gunicorn on Render |
| CI | GitHub Actions (ruff, compile check) |

See [docs/architecture.md](docs/architecture.md) for the design.

## Getting started

### Prerequisites

- Python 3.10+
- A Firebase project with Firestore enabled and a service account key

### Setup

```bash
git clone https://github.com/shizuku0901/unsw_college_computing_media_presentation_website.git
cd unsw_college_computing_media_presentation_website/fitness_app

python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Provide Firebase credentials in one of two ways (see `.env.example`):

1. Set the `FIREBASE_CREDENTIALS` environment variable to the key's JSON string, or
2. Save the key as `fitness_app/unsw-college-website-firebase.json` (git-ignored).

Optionally set `SECRET_KEY`, then:

```bash
python seed.py   # load sample tips into Firestore (optional)
python app.py    # http://localhost:5001
```

> `app.py` runs with `debug=True` for local development only. In production the app is served by gunicorn.

## Known limitations

This project was built as a course prototype, so some parts are intentionally simple:

- **Login is ID-only.** There is no password or email verification, and registering with an existing ID overwrites that user. Please do not enter real personal information in the public demo.
- There are no automated tests yet.
- Dependency versions in `requirements.txt` are not pinned.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT License](LICENSE)