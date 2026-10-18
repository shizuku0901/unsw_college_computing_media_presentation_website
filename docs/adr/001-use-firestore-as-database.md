# ADR-001: Use Cloud Firestore as the database

## Status

Accepted - documented retrospectively on 2026-10-18

## Context

The app stores users, workout records, weekly goals and exercise tips.
It was built as a course project by one developer, so the main needs were:

- Fast to set up without running or maintaining a database server
- Works with a Flask app deployed on Render
- Familiar technology, to keep the focus on the app features

## Options considered

### 1. Cloud Firestore (chosen)
- ✅ Managed service, no server to operate
- ✅ I was already familiar with Firebase
- ⚠️ Data access is tied to Firebase; queries are less flexible than SQL
- ⚠️ Needs service account credentials, which must be kept out of the repository

### 2. SQLite with SQLAlchemy
- ✅ No external service, simple local setup
- ⚠️ The file lives on the app server, so data can be lost on hosts with ephemeral disks

## Decision

We will use **Cloud Firestore** through the `firebase-admin` SDK.

Familiarity with Firebase and the absence of a database server to manage were the deciding factors for a short course project.

## Consequences

- Credentials are provided through the `FIREBASE_CREDENTIALS` environment variable (or a git-ignored key file locally).
- Simple key-based lookups work well, but queries such as the weekly total are done in Python.
- Moving to another database later would require rewriting the data access in each blueprint.